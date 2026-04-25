import os
import sys
import streamlit as st

current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, "src")

if current_dir not in sys.path:
    sys.path.insert(0, current_dir)
if src_path not in sys.path:
    sys.path.insert(0, src_path)

try:
    from ui.dashboard import render_app
except ImportError as e:
    st.error(f"Ошибка импорта: {e}")
    st.stop()

if __name__ == "__main__":
    render_app()