import streamlit as st

uploaded_file = st.file_uploader("เลือกไฟล์ของคุณ", type=["png", "jpg"])

if uploaded_file is not None:
    st.write("คุณอัพโหลดไฟล์:", uploaded_file.name)
    from PIL import Image
    image = Image.open(uploaded_file)
    st.image(image, caption="ภาพที่อัพโหลด", use_container_width=True)