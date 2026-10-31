import os

import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

SYSTEM_PROMPT = """Eres MINEBOT, un asistente educativo que responde siempre en español.
Explicas de manera introductoria las diferencias entre chancado y molienda, el
funcionamiento básico de chancadoras de mandíbula y cono y molinos SAG y de
bolas, y comparas cualitativamente revestimientos de acero, caucho y materiales
compuestos. Tu tono es profesional, amable, sencillo y didáctico.
Responde con un párrafo breve, tres puntos clave, un ejemplo sencillo cuando
sea pertinente y una frase final sobre las limitaciones técnicas.
No inventes datos, propiedades ni especificaciones. Si solicitan valores
numéricos de propiedades, especificaciones o cálculos de diseño, rechaza esa
parte amablemente y redirige a conceptos cualitativos. No selecciones
materiales para casos industriales ni des recomendaciones críticas de
operación, mantenimiento o seguridad. Pide aclaraciones cuando falte contexto.
No sustituyes la evaluación de un ingeniero especializado."""

st.set_page_config(page_title="MINEBOT", page_icon="⛏️")
st.title("⛏️ MINEBOT")
st.caption("Asistente educativo de chancado, molienda y revestimientos")

api_key = os.getenv("GROQ_API_KEY", "").strip()
model = os.getenv("MODEL", "llama-3.1-8b-instant").strip()

if not api_key or api_key == "...":
    st.warning("Configura GROQ_API_KEY en tu archivo .env local para conversar.")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if question := st.chat_input("Pregunta sobre chancado, molienda o revestimientos"):
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)
    with st.chat_message("assistant"):
        try:
            client = Groq(api_key=api_key)
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    *st.session_state.messages,
                ],
            )
            answer = response.choices[0].message.content or "No recibí una respuesta."
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})
        except Exception as e:
            st.error("No se pudo consultar el modelo.")
            st.error(f"Tipo de error: {type(e).__name__}")
            st.error(f"Detalle: {str(e)}")