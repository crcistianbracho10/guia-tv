import streamlit as st
import subprocess
import json

st.set_page_config(page_title="Extractor Canal C - NTN24", layout="centered")

st.title("📺 Extractor de Enlaces M3U8 en Vivo")
st.subheader("Canal C del Zulia - Módulo de Prueba Continua")

# Enlace en vivo de NTN24 solicitado por el usuario para la prueba
YOUTUBE_URL_NTN24 = "https://www.youtube.com/@ntn24/live"

def extraer_m3u8_ntn24():
    """
    Ejecuta yt-dlp en el servidor en la nube de Streamlit para extraer
    la URL cruda del archivo .m3u8 oculto en la transmisión en vivo de NTN24.
    """
    try:
        # Comando para extraer directamente el enlace del flujo HLS nativo (.m3u8)
        comando = ["yt-dlp", "-g", "--match-filter", "is_live", YOUTUBE_URL_NTN24]
        resultado = subprocess.run(comando, capture_output=True, text=True, timeout=15)
        
        url_cruda = resultado.stdout.strip()
        # Verificamos que la salida contenga el formato m3u8 correcto
        if url_cruda and ".m3u8" in url_cruda:
            return url_cruda
    except Exception as e:
        return f"Error en la extracción automática: {str(e)}"
    
    return "El canal de prueba no está transmitiendo en vivo o se alcanzó el límite de solicitudes."

# Botón manual para obligar al servidor a refrescar el enlace
if st.button("🔄 Forzar Regeneración de Enlace M3U8"):
    st.rerun()

st.divider()

st.markdown("### 🔗 Enlace Maestro M3U8 (NTN24 - Señal de Prueba)")
st.write("Copia el contenido del recuadro negro de abajo. Este es el enlace directo HLS listo para tus reproductores o paneles de IPTV:")

# El servidor ejecuta la extracción en este instante
enlace_final_m3u8 = extraer_m3u8_ntn24()

# Se muestra el enlace limpio en la interfaz web con opción de copiado rápido
st.code(enlace_final_m3u8, language="text")

st.divider()

# Añadimos un monitor de control visual para verificar que la señal de YouTube esté en línea
if "http" in enlace_final_m3u8:
    with st.expander("👁️ Ver Monitor Técnico de Señal (Espejo YouTube)"):
        # ID de canal interno de NTN24 para incrustar el reproductor nativo de respaldo
        html_preview = """
        <iframe width="100%" height="350" src="https://youtube.com" frameborder="0" allowfullscreen style="border-radius:12px;"></iframe>
        """
        st.components.v1.html(html_preview, height=360)

st.caption("Aviso técnico: Recuerda que los enlaces .m3u8 generados por los servidores de YouTube caducan cada pocas horas por seguridad de Google. Al usar esta aplicación en Streamlit, el canal garantiza que con solo recargar la URL web se obtendrá un enlace de transmisión completamente nuevo y funcional.")
