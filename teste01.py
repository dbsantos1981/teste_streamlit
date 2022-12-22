import streamlit as st
from spleeter.separator import Separator

st.title("Hello World")

# Using embedded configuration.
separator = Separator('spleeter:2stems')

st.balloons()
