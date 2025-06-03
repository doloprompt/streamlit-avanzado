"""
STREAMLIT NIVEL AVANZADO 2 - MÓDULO 1.1
Entornos virtuales y gestión de librerías
Tiempo estimado: 45 minutos
"""

import streamlit as st
import subprocess
import sys
import os
from pathlib import Path

st.set_page_config(
    page_title="Módulo 1.1 - Entornos Virtuales",
    page_icon="🔧",
    layout="wide"
)

st.title("🔧 Módulo 1.1: Entornos Virtuales y Gestión de Librerías")

# Sidebar con navegación
st.sidebar.title("📚 Contenido del Módulo")
seccion = st.sidebar.selectbox(
    "Selecciona una sección:",
    [
        "Introducción a entornos virtuales",
        "Creación y activación de entornos",
        "Instalación de librerías específicas",
        "Gestión de dependencias con requirements.txt",
        "Ejemplo práctico"
    ]
)

if seccion == "Introducción a entornos virtuales":
    st.header("🎯 ¿Por qué usar entornos virtuales?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("✅ Ventajas")
        st.markdown("""
        - **Aislamiento de dependencias**: Cada proyecto tiene sus propias librerías
        - **Evitar conflictos**: Diferentes versiones de la misma librería
        - **Reproducibilidad**: Garantizar que el proyecto funcione en cualquier máquina
        - **Limpieza**: No ensuciar el sistema Python global
        """)
    
    with col2:
        st.subheader("🔗 Conceptos clave")
        st.markdown("""
        - **venv**: Módulo estándar de Python 3.3+
        - **pip**: Gestor de paquetes de Python
        - **requirements.txt**: Lista de dependencias
        - **activate/deactivate**: Comandos para manejar el entorno
        """)
    
    st.info("💡 **Consejo**: Siempre crear un entorno virtual antes de comenzar un nuevo proyecto Streamlit")

elif seccion == "Creación y activación de entornos":
    st.header("🚀 Creación y Activación de Entornos Virtuales")
    
    st.subheader("📝 Comandos paso a paso")
    
    # Tabs para diferentes sistemas operativos
    tab1, tab2, tab3 = st.tabs(["🪟 Windows", "🐧 Linux/Mac", "🐍 Conda"])
    
    with tab1:
        st.code("""
# 1. Crear entorno virtual
python -m venv streamlit_avanzado

# 2. Activar entorno
streamlit_avanzado\\Scripts\\activate

# 3. Verificar activación
where python
where pip

# 4. Desactivar (cuando termine)
deactivate
        """, language="bash")
    
    with tab2:
        st.code("""
# 1. Crear entorno virtual
python3 -m venv streamlit_avanzado

# 2. Activar entorno
source streamlit_avanzado/bin/activate

# 3. Verificar activación
which python
which pip

# 4. Desactivar (cuando termine)
deactivate
        """, language="bash")
    
    with tab3:
        st.code("""
# 1. Crear entorno con Conda
conda create -n streamlit_avanzado python=3.11

# 2. Activar entorno
conda activate streamlit_avanzado

# 3. Verificar activación
conda info --envs

# 4. Desactivar
conda deactivate
        """, language="bash")
    
    st.warning("⚠️ **Importante**: Siempre verificar que el entorno esté activado antes de instalar paquetes")

elif seccion == "Instalación de librerías específicas":
    st.header("📦 Instalación de Librerías Específicas para Streamlit")
    
    st.subheader("🎯 Librerías esenciales para este curso")
    
    # Mostrar la lista de paquetes necesarios
    paquetes_esenciales = {
        "streamlit": "Framework principal",
        "pandas": "Manipulación de datos",
        "numpy": "Cálculos numéricos",
        "sqlite3": "Base de datos (incluido en Python)",
        "requests": "Peticiones HTTP para APIs",
        "asyncio": "Programación asíncrona",
        "aiohttp": "Cliente HTTP asíncrono",
        "plotly": "Gráficos interactivos",
        "python-dotenv": "Variables de entorno"
    }
    
    for paquete, descripcion in paquetes_esenciales.items():
        st.markdown(f"- **{paquete}**: {descripcion}")
    
    st.subheader("⚡ Comando de instalación completo")
    st.code("""
pip install streamlit pandas numpy requests aiohttp plotly python-dotenv
    """, language="bash")
    
    # Verificación de instalación
    st.subheader("🔍 Verificar instalación")
    if st.button("Verificar paquetes instalados"):
        try:
            import pandas as pd
            import numpy as np
            import requests
            import plotly.graph_objects as go
            
            st.success("✅ Todos los paquetes están correctamente instalados")
            
            # Mostrar versiones
            versiones = {
                "Streamlit": st.__version__,
                "Pandas": pd.__version__,
                "NumPy": np.__version__,
                "Requests": requests.__version__
            }
            
            for lib, version in versiones.items():
                st.text(f"{lib}: {version}")
                
        except ImportError as e:
            st.error(f"❌ Error: {e}")

elif seccion == "Gestión de dependencias con requirements.txt":
    st.header("📄 Gestión de Dependencias con requirements.txt")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("✨ Generar requirements.txt")
        st.code("""
# Generar desde entorno actual
pip freeze > requirements.txt

# Ver el contenido
cat requirements.txt  # Linux/Mac
type requirements.txt  # Windows
        """, language="bash")
    
    with col2:
        st.subheader("📥 Instalar desde requirements.txt")
        st.code("""
# Instalar todas las dependencias
pip install -r requirements.txt

# Actualizar paquetes
pip install -r requirements.txt --upgrade
        """, language="bash")
    
    st.subheader("📝 Ejemplo de requirements.txt para este curso")
    st.code("""
streamlit==1.45.0
pandas==2.1.4
numpy==1.26.2
requests==2.31.0
aiohttp==3.9.1
plotly==5.17.0
python-dotenv==1.0.0
    """, language="text")
    
    st.info("💡 **Buena práctica**: Siempre incluir versiones específicas para garantizar reproducibilidad")

else:  # Ejemplo práctico
    st.header("🎯 Ejemplo Práctico: Configuración Completa")
    
    st.subheader("📋 Checklist de configuración")
    
    # Simulación de checklist interactivo
    if 'checklist_estado' not in st.session_state:
        st.session_state.checklist_estado = {
            'entorno_creado': False,
            'entorno_activado': False,
            'streamlit_instalado': False,
            'dependencias_instaladas': False,
            'requirements_generado': False
        }
    
    tareas = [
        ('entorno_creado', '🔧 Crear entorno virtual'),
        ('entorno_activado', '⚡ Activar entorno virtual'),
        ('streamlit_instalado', '🎨 Instalar Streamlit'),
        ('dependencias_instaladas', '📦 Instalar dependencias adicionales'),
        ('requirements_generado', '📄 Generar requirements.txt')
    ]
    
    for key, descripcion in tareas:
        st.session_state.checklist_estado[key] = st.checkbox(
            descripcion, 
            value=st.session_state.checklist_estado[key],
            key=f"check_{key}"
        )
    
    # Progress bar
    completado = sum(st.session_state.checklist_estado.values())
    progreso = completado / len(st.session_state.checklist_estado)
    
    st.progress(progreso)
    st.write(f"Progreso: {completado}/{len(st.session_state.checklist_estado)} tareas completadas")
    
    if progreso == 1.0:
        st.balloons()
        st.success("🎉 ¡Configuración completa! Ya puedes continuar con el desarrollo")

# Footer con información adicional
st.markdown("---")
st.markdown("**📚 Recursos adicionales:**")
st.markdown("""
- [Documentación oficial de venv](https://docs.python.org/3/library/venv.html)
- [Guía de pip](https://pip.pypa.io/en/stable/user_guide/)
- [Best practices para entornos virtuales](https://realpython.com/python-virtual-environments-a-primer/)
""")
