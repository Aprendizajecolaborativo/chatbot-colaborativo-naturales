import streamlit as st

st.set_page_config(page_title="Chatbot Colaborativo de Ciencias Naturales")

st.title("🤖 BioBot: Tu Asistente Colaborativo en Ciencias Naturales")
st.markdown("### ¡Bienvenidos estudiantes! Vamos a trabajar juntos en grupo 🧪")

# Paso 1: Ingreso de nombres
group = st.text_input("Escribe los nombres del grupo (separados por comas)")

if group:
    st.success(f"¡Hola {group}! 👋")
    st.markdown("#### Estos son sus roles sugeridos:")
    members = group.split(",")
    roles = ["Investigador/a", "Redactor/a", "Diseñador/a", "Expositor/a"]
    for i, name in enumerate(members):
        st.write(f"- **{name.strip()}**: {roles[i % len(roles)]}")

    # Paso 2: Actividad
    st.markdown("### 🧪 Actividad del día")
    st.info("Investiguen el impacto del **cambio climático** en un ecosistema local. Luego, creen una infografía o presentación en grupo.")

    # Paso 3: Subida de trabajo
    file = st.file_uploader("📤 Suban su trabajo aquí (PDF, imagen o presentación)")
    if file:
        st.success("¡Trabajo recibido! ✅")

    # Paso 4: Retroalimentación
    if st.button("🧠 Quiero una sugerencia para mejorar"):
        st.markdown("💡 *Agreguen una conclusión clara y referencias confiables. ¿Desean ejemplos de fuentes académicas?*")
