import streamlit as st
import spleeter as sp

# from spleeter.separator import Separator

st.title("Hello World")
separator_lib = sp.separator.Separator("spleeter:2stems", multiprocess=False)
st.balloons()
