
import streamlit as st # type: ignore
import matplotlib.pyplot as plt # type: ignore

# Set the page title and header
st.title("ESTADISTICAS CTECNO")
st.header("Reserva salas y computadores con facilidad")

# Hero Section with image and project description
st.image("imagen/Logo_ctecnoazul.jpg", width=600)
st.write(" Este extencion del aplicativo te permite ver las estadisticas segun los filtros que prefieras")

# Project Overview
st.subheader("Resumen General ")
st.write("- Pagina WEB hecha con react que Permite realizar reservas de salas de computo, reserva computadores y accesorios.")
st.write("- Aplicativo de android que Permite realizar reservas de salas de computo, reserva computadores y accesorios.")
st.write("- Un streamlit de Anatica de datos en pandas que permite generar difentes filtos.")

# Interactive Chart or Visualization (Optional)
# Replace with your specific data and visualization
data = [60, 30, 10]
labels = ["Computadores", "Salas", "Accsesorios"]
fig, ax = plt.subplots()
ax.pie(data, labels=labels, autopct="%1.1f%%")
st.pyplot(fig)

# Call to Action
st.subheader("¡Toma Acción!")
st.write("**Visite nuestro sitio web:** [Enlace al sitio web del proyecto](https://example.com)")
st.write("**Contáctenos:** [Enlace al correo electrónico de contacto](mailto:info@example.com)")

# Footer with team members and project information
st.subheader("Equipo y Contacto")
st.write("**Miembros del equipo:**")
st.write("- Andres Quevedo.")
st.write("- Jonathan Mesa.")
st.write("- Manuela Orrego.")
st.write("- Stiven Londoño.")
st.write("- Helen Vargas.")
st.write("**Información de contacto:**")
st.write("Correo electrónico: [Enlace al correo electrónico de contacto](mailto:ctecnoempresa@gmail.com )")