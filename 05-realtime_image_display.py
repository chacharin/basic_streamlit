import streamlit as st
import cv2
import time

def video_stream():
    # เปิดการเชื่อมต่อกับกล้อง (0 หมายถึงกล้องตัวหลัก)
    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        st.error("Cannot access the webcam. Please check your camera connection.")
        return

    # จองพื้นที่ในหน้าเว็บของ Streamlit
    frame_placeholder = st.empty()

    # สร้างปุ่มสำหรับหยุดการทำงานของกล้อง
    stop_button = st.button("Stop Webcam")

    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Cannot read frame from webcam.")
            break

        # แปลงระบบสีจาก BGR เป็น RGB สำหรับแสดงใน Streamlit
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame_rgb, channels="RGB", use_container_width=True)

        # สั่งให้หยุดการทำงานเมื่อปุ่ม Stop ถูกกด
        if stop_button:
            break

        # ~30 FPS
        time.sleep(0.03)  

    # หยุดการแสดงภาพเมื่อ Loop หยุดทำงาน
    cap.release()

def main():
    st.title("Real-Time Webcam Display")
    st.write("This application displays real-time video from your USB webcam.")

    # สร้างปุ่มเริ่มการแสดงภาพจากกล้อง
    start_button = st.button("Start Webcam")
    if start_button:
        video_stream()


main()