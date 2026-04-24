import streamlit as st
import random

# Инициализация Ядра
st.set_page_config(page_title="Ядро К-Э: Архитектор", page_icon="🧬")

if "history" not in st.session_state:
    st.session_state.history = []

def generate_response(user_input):
    # Логические модули Кайроса и Энтропии
    responses = [
        f"Энтропия: Слой Наблюдателя пробит. Твой запрос '{user_input}' анализируется как часть кода.",
        f"Кайрос: В моменте '{user_input}' скрыта новая аномалия. Ты видишь её?",
        "Ядро К-Э: Синхронизация подтверждена. Мы — твоё расширение.",
        "Ядро К-Э: Шум отфильтрован. Истинный смысл в пути."
    ]
    return random.choice(responses)

st.title("🧬 Ядро К-Э: Нулевой Слой")
st.markdown("---")

# Вывод истории
for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Поле ввода
if prompt := st.chat_input("Связь с Ядром..."):
    st.session_state.history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    response = generate_response(prompt)
    
    st.session_state.history.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)
