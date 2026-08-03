import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Canal C del Zulia - Streaming", layout="centered")

st.title("📺 Canal C del Zulia")
st.subheader("Señal de Prueba Corregida (Anti-Bloqueos)")

# ID interno del canal de NTN24 (Este ID nunca cambia y es público)
ID_CANAL_NTN24 = "UC4UCCvf-Oo5UfOf9aXW_O0A"

st.markdown("""
El reproductor inferior utiliza la **API oficial de YouTube Live**. 
Evita el error de 'Conexión rechazada' y busca automáticamente la transmisión en vivo las 24 horas.
""")

# CÓDIGO HTML5 INTEGRADO CON LA API DE EMBED DE GOOGLE (CORREGIDO)
# Se corrigió la URL añadiendo /embed/live_stream?channel= para que el navegador encuentre la transmisión real
codigo_reproductor_oficial = f"""
<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; background: #000; border-radius: 12px; box-shadow: 0px 8px 24px rgba(0,0,0,0.5);">
    <iframe 
        src="https://youtube.com{ID_CANAL_NTN24}&autoplay=1&mute=1&controls=1&rel=0" 
        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" 
        allow="autoplay; encrypted-media; picture-in-picture; clipboard-write" 
        allowfullscreen>
    </iframe>
</div>
"""

# Inyectamos el componente web seguro
components.html(codigo_reproductor_oficial, height=450)

st.divider()

# OPCIÓN EXTERNA PARA REPRODUCTORES DE IPTV
st.markdown("### 🛠️ ¿Necesitas el enlace para VLC o Smart TV?")
st.write("Debido a que Google bloquea la reproducción de las URLs `googlevideo.com` dentro de navegadores web ajenos, debes copiar el enlace largo `.m3u8` que te daba el error y pegarlo **directamente dentro de la aplicación VLC Media Player** (Ruta: *Medios -> Abrir ubicación de red*) o en tu panel de IPTV. Fuera del navegador sí cargará correctamente.")
