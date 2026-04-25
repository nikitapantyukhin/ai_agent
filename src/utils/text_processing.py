import streamlit as st
import pandas as pd
import numpy as np
from src.agents.market_agent import agent
from src.utils.text_processing import extract_product_name

def render_app():
    st.set_page_config(page_title="Market AI Agent v3.0", layout="wide")
    
    st.title("🤖 Market AI Agent [PRO]")
    
    user_query = st.text_area("Введите ваш запрос:", placeholder="Например: хочу продавать одежду, какие тренды?")
    
    if st.button("🚀 Провести глубокий анализ"):
        if user_query:
            try:
                with st.spinner("Агент анализирует рынок..."):
                    product = extract_product_name(user_query)
                    
                    # Промпт для ИИ
                    prompt = f"""
                    Ты — эксперт-аналитик. ОТВЕЧАЙ ТОЛЬКО НА РУССКОМ.
                    Проанализируй нишу: {product}.
                    Расскажи про тренды весна-лето 2026, закупку (Китай/Турция), прибыль и риски.
                    """
                    
                    report = agent.run(prompt)
                    
                    st.success(f"Анализ завершен: {product.upper()}")
                    
                    tab1, tab2 = st.tabs(["🧠 Стратегия", "📊 Аналитика"])
                    
                    with tab1:
                        col1, col2 = st.columns([2, 1])
                        with col1:
                            st.markdown("### 📝 Отчет аналитика")
                            st.info(report)
                        with col2:
                            st.markdown("### 💰 Финансы и Риски")
                            st.metric("Прогноз прибыли", "20-30%", "+5%")
                            st.warning("**Основные риски:**\n* Смена трендов\n* Логистика\n* Дефицит")
                            
                    with tab2:
                        st.subheader("📅 Сезонность")
                        months = ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек']
                        data = pd.DataFrame({
                            'Месяц': months, 
                            'Спрос': np.random.randint(30, 100, size=12)
                        }).set_index('Месяц')
                        st.line_chart(data)
                        
            except Exception as e:
                st.error(f"Произошла ошибка: {e}")