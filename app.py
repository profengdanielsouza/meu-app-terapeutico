import streamlit as st
import google.generativeai as genai

# Configuração da página para parecer App
st.set_page_config(page_title="Porto Seguro", page_icon="🌿")

# Configurar a IA com a personalidade de terapeuta
genai.configure(api_key="SUA_CHAVE_AQUI")
model = genai.GenerativeModel('gemini-pro')

st.title("🌿 Porto Seguro")
st.subheader("Estou aqui para te ouvir e ajudar a relaxar.")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir histórico
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Lógica do Chat
if prompt := st.chat_input("Como você está se sentindo agora?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Instrução oculta para a IA agir como terapeuta
        contexto = "Você é uma IA de apoio emocional escolar. Use frases curtas, tom calmo e técnicas de respiração se detectar ansiedade. Seja acolhedor."
        response = model.generate_content(contexto + prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})

# Botão de Ajuda Urgente
if st.button("🆘 Preciso de ajuda urgente"):
    st.error("Respire fundo. Ligue para o CVV no número 188 ou procure seu professor agora.")
