import streamlit as st
import pandas as pd
import numpy as np

st.header("Page 1", divider="gray")
subject = st.text_input("Enter a subject name")
submit_button = st.button("Enter")

if submit_button:
    st.write(f"You'll pass {subject}. Goodluck! :smile:")