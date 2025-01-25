import streamlit as st

age = st.slider("คุณอายุเท่าไหร่?", min_value= 0, max_value=100, value=25)
st.write("คุณอายุ", age, "ปี")