import re

def extract_product_name(text):
    text = text.lower()

    stop_words = ['хочу', 'начать', 'продавать', 'какая', 'сейчас', 'популярная', 'подскажи', 'нишу']

    words = re.sub(r'[^\w\s]', '', text).split()
    
    filtered = [w for w in words if w not in stop_words]
    
    if 'одежд' in text: 
        return "одежда"

    return " ".join(filtered[:2]) if filtered else "товар"