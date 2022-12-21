import streamlit as st
from spleeter.separator import Separator

st.title("Hello World")
separator_lib = Separator("spleeter:2stems", multiprocess=False)
st.balloons()
