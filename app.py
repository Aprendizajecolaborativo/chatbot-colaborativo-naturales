import streamlit as st

st.set_page_config(page_title="Chatbot Colaborativo de Ciencias Naturales")

st.title("🤖 BioBot: Tu Asistente Colaborativo en Ciencias Naturales")
st.markdown("### ¡Bienvenidos estudiantes de bachillerato! Vamos a trabajar juntos en grupo 🧪")

# Selección de año
year = st.selectbox(
    "Selecciona tu nivel:",
    [
        "Primer año de bachillerato",
        "Segundo año de bachillerato",
        "Tercer año de bachillerato"
    ]
)

# Temas por año
topics = {
    "Primer año de bachillerato": [
        "La célula: Estructura, función y tipos de células",
        "Química orgánica: Macromoléculas (proteínas, carbohidratos, lípidos, ácidos nucleicos)",
        "Genética: Herencia, ADN, ARN",
        "Sistemas del cuerpo humano: Estructura y función de los principales sistemas"
    ],
    "Segundo año de bachillerato": [
        "Reproducción: sexual y asexual, desarrollo embrionario",
        "Ecología: Interacciones, dinámica de poblaciones, cadenas alimentarias",
        "Evolución: Teorías, pruebas evolutivas, selección natural",
        "Biodiversidad: Clasificación de los seres vivos, diversidad biológica"
    ],
    "Tercer año de bachillerato": [
        "Biología molecular y celular: Ácidos nucleicos, expresión génica",
        "Bioquímica: Metabolismo, enzimas, reacciones bioquímicas",
        "Evolución y selección natural: Mecanismos, adaptaciones",
        "Ecosistemas: Estructura, función e interacciones"
    ]
}

st.markdown(f"#### {year}")
subject = st.selectbox("Elige un tema:", topics[year])

# Ingreso de nombres de grupo
group = st.text_input("Escribe los nombres del grupo (separados por comas)")
if group:
    members = [m.strip() for m in group.split(",") if m.strip()]
    st.success(f"¡Hola {', '.join(members)}! 🎓")
    st.markdown("**Roles sugeridos:**")
    roles = ["Investigador/a", "Redactor/a", "Diseñador/a", "Expositor/a"]
    for i, name in enumerate(members):
        st.write(f"- **{name}**: {roles[i % len(roles)]}")

    # Presentación de actividad
    st.markdown("### 🧪 Actividad del día")
    st.info(f"Investiga sobre **{subject}**. Luego, trabajen en grupo para crear una presentación o infografía.")

    # Subida de trabajo
    file = st.file_uploader("📤 Suban su trabajo aquí (PDF, imagen o presentación)")
    if file:
        st.success("¡Trabajo recibido! ✅")

    # Retroalimentación
    if st.button("🧠 Quiero una sugerencia para mejorar"):
        st.markdown(
            "💡 Agreguen una introducción clara y asegúrense de citar fuentes confiables. ¿Necesitan ejemplos de referencias académicas?"
        )
