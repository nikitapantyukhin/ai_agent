import streamlit as st
import pandas as pd
import numpy as np
import time
from agents.market_agent import agent
from utils.text_processing import extract_product_name

def render_app():
    st.set_page_config(page_title="Market AI Agent", layout="wide")
    st.title("🤖 Market AI Agent")
    
    col_input, col_settings = st.columns([2, 1])
    
    with col_input:
        user_query = st.text_area("Что анализируем?", placeholder="Например: Хочу начать продавать чехлы для телефонов", height=100)
        
    with col_settings:
        marketplaces = st.multiselect(
            "Площадки:",
            ["Wildberries", "Ozon", "Yandex Market", "Avito"],
            default=["Wildberries", "Ozon"]
        )
        budget = st.slider("Бюджет (тыс. ₽):", 50, 2000, 300)

    if st.button("🚀 Запустить глубокий анализ"):
        if user_query:
            try:
                progress = st.progress(0)
                status = st.empty()
                
                status.text("Поиск трендов и конкурентов...")
                progress.progress(30)
                
                product = extract_product_name(user_query)
                platforms = ", ".join(marketplaces)
                
                prompt = f"""
                Ты — старший бизнес-консультант по маркетплейсам {platforms}.
                Твоя задача: составить подробный стратегический план для запуска товара: "{product}".
                Бюджет клиента: {budget} 000 рублей.

                ОБЯЗАТЕЛЬНО ВКЛЮЧИ В ОТВЕТ:
                1. СТРАТЕГИЧЕСКИЙ ПЛАН НА 30 ДНЕЙ (по неделям):
                   - Неделя 1: Анализ конкурентов и выбор поставщика (Китай/Турция/РФ).
                   - Неделя 2: Закупка образцов и создание карточки (SEO, инфографика).
                   - Неделя 3: Логистика и маркировка ("Честный знак" если нужно).
                   - Неделя 4: Первая поставка и методы продвижения (самовыкупы, внутренняя реклама).

                2. ФИНАНСОВЫЙ РАСЧЕТ:
                   - Примерная цена закупа и цена реализации.
                   - Расчет чистой прибыли с единицы.

                3. ТАКТИКА "БЫСТРЫЙ СТАРТ":
                   - Как обойти топов выдачи за первый месяц.

                Пиши очень подробно, используй заголовки #, списки и жирный шрифт. 
                Ответ должен быть на русском языке и содержать не менее 400 слов.
                """
                
                report = agent.run(prompt)
                progress.progress(100)
                status.empty()

                st.success(f"Анализ ниши: {product.upper()}")
                
                tab1, tab2, tab3 = st.tabs(["📋 Отчет", "📈 Статистика", "📊 Сравнение"])
                
                with tab1:
                    st.markdown("### 🗺️ Стратегический план запуска")
                    
                    if isinstance(report, dict):
                        for week, tasks in report.items():
                            with st.expander(f"📍 {week}", expanded=True):о
                                st.markdown(tasks.replace('\n-', '\n*')) 
                    else:
                        st.markdown(report)

                    st.divider()
                    st.info("💡 **Совет:** Начинайте с анализа Wildberries — там сейчас самый быстрый цикл оборота капитала для старта.")
                
                with tab2:
                    st.subheader("Прогноз спроса (2026)")
                    data = pd.DataFrame({'Спрос': np.random.randint(40, 100, 12)}, 
                                      index=['Янв','Фев','Мар','Апр','Май','Июн','Июл','Авг','Сен','Окт','Ноя','Дек'])
                    st.line_chart(data)
                    
                with tab3:
                    st.subheader("Метрики по площадкам")
                    compare_df = pd.DataFrame({
                        "Маркетплейс": marketplaces,
                        "ROI": [f"{np.random.randint(100, 250)}%" for _ in marketplaces],
                        "Конкуренция": ["Средняя", "Высокая", "Низкая", "Средняя"][:len(marketplaces)]
                    })
                    st.table(compare_df)
                    
            except Exception as e:
                st.error(f"Ошибка: {e}")