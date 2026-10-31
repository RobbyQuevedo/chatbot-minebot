# MINEBOT

Asistente educativo en español sobre chancado, molienda y materiales de revestimiento. Ofrece explicaciones introductorias y comparaciones cualitativas; no sustituye la evaluación de un ingeniero.

## Ejecutar localmente

1. Abre la carpeta `MINEBOT` en VS Code y abre una terminal.
2. Crea un entorno virtual (opcional si ya usas un entorno Conda):
   ```powershell
   python -m venv .venv
   ```
   Actívalo en PowerShell:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
   Si usas Conda, activa tu entorno en lugar de crear `.venv`.
3. Instala las dependencias:
   ```powershell
   python -m pip install -r requirements.txt
   ```
4. En el archivo `.env` local, reemplaza `GROQ_API_KEY=...` por tu clave real de Groq. Verifica que `MODEL` sea un identificador disponible en tu cuenta. **No compartas ni subas `.env` a GitHub.**
5. Inicia la aplicación:
   ```powershell
   python -m streamlit run app.py
   ```
6. Abre la dirección local que aparezca en la terminal (habitualmente `http://localhost:8501`).

## Publicación

Para desplegar en Streamlit Community Cloud, configura `GROQ_API_KEY` y `MODEL` en **Secrets** de la aplicación. Nunca incluyas claves en el repositorio.
