# Streamlit app entry point placeholder

import os
import streamlit as st

PIN = os.environ.get("APP_PIN", "Lugano-250k")  # default PIN or from Streamlit Secrets

def gate():
    if "ok" in st.session_state:
        return
    st.title("Private Demo")
    pin = st.text_input("Enter access PIN", type="password")
    if st.button("Enter"):
        if pin == PIN:
            st.session_state["ok"] = True
            st.experimental_rerun()
        else:
            st.error("Wrong PIN")
    st.stop()

gate()
