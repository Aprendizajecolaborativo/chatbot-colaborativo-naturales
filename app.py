import streamlit as st

st.set_page_config(page_title="Chatbot Colaborativo de Ciencias Naturales")

st.title("🤖 BioBot: Tu Asistente Colaborativo en Ciencias Naturales")
st.markdown("### ¡Bienvenidos estudiantes de bachillerato! Vamos a trabajar juntos en grupo 🧪")

# Selección de nivel
year = st.selectbox(
    "Selecciona tu nivel:",
    [
        "Primer año de bachillerato",
        "Segundo año de bachillerato",
        "Tercer año de bachillerato"
    ]
)

# Temas por nivel
topics = {
    "Primer año de bachillerato": [
        "La célula: Estructura, función y tipos de células",
        "Química orgánica: Macromoléculas",
        "Genética: Herencia, ADN, ARN",
        "Sistemas del cuerpo humano"
    ],
    "Segundo año de bachillerato": [
        "Reproducción: sexual y asexual",
        "Ecología: Interacciones y dinámica",
        "Evolución y selección natural",
        "Biodiversidad y clasificación"
    ],
    "Tercer año de bachillerato": [
        "Biología molecular y celular",
        "Bioquímica: Metabolismo y enzimas",
        "Ecosistemas: estructura e interacciones",
        "Genética: Mendel y genómica"
    ]
}

# Mostrar tema según nivel
st.markdown(f"#### {year}")
subject = st.selectbox("Elige un tema:", topics[year])

# Nombres de grupo
group = st.text_input("Escribe los nombres del grupo (separados por comas)")
if group:
    members = [m.strip() for m in group.split(",") if m.strip()]
    st.success(f"¡Hola {', '.join(members)}! 🎓")
    st.markdown("**Roles sugeridos:**")
    roles = ["Investigador/a", "Redactor/a", "Diseñador/a", "Expositor/a"]
    for i, name in enumerate(members):
        st.write(f"- **{name}**: {roles[i % len(roles)]}")

    # Actividad
    st.markdown("### 🧪 Actividad del día")
    st.info(f"Investiga sobre **{subject}**. Luego, trabajen en grupo para crear una presentación o infografía.")

    # Subir trabajo
    file = st.file_uploader("📤 Suban su trabajo aquí (PDF, imagen o presentación)")
    if file:
        st.success("¡Trabajo recibido! ✅")

    # Sugerencia rápida
    if st.button("🧠 Quiero una sugerencia para mejorar"):
        st.markdown("💡 Agreguen una introducción clara y citen fuentes confiables. ¿Necesitan ejemplos de referencias académicas?")

    # 🧠 ZONA DE CHAT (Tipo ChatGPT simulado)
    st.markdown("---")
    st.header("💬 Conversa con BioBot")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    for chat in st.session_state.chat_history:
        with st.chat_message(chat["role"]):
            st.markdown(chat["message"])

    user_input = st.chat_input("Escribe tu mensaje aquí...")

    if user_input:
        st.chat_message("user").markdown(user_input)
        st.session_state.chat_history.append({"role": "user", "message": user_input})

        # Respuesta simulada según contenido
        if "cita" in user_input.lower():
            response = "📚 Una cita en APA incluye autor, año y página. Ejemplo: (García, 2020, p. 45)."
        elif "plagio" in user_input.lower():
            response = "🧐 Evita el plagio parafraseando y citando bien. ¿Quieres que te ayude con eso?"
        elif "mejorar" in user_input.lower():
            response = "✏️ Puedes mejorar usando conectores, redacción clara y fuentes confiables. ¿Quieres un ejemplo?"
        else:
            response = "🤖 Gracias por tu mensaje. Pronto podré responder con inteligencia artificial real."

        with st.chat_message("assistant"):
            st.markdown(response)

        st.session_state.chat_history.append({"role": "assistant", "message": response})
