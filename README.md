# basic_streamlit

#สร้าง Environment

python -m venv venv

#เข้าถึง Environment

.\venv\Scripts\activate (Windows)

source venv/bin/activate (MacOS)

#ติดตั้ง Library ตามรายการที่ระบุไว้ในไฟล์ txt

pip install -r requirements.txt

#ใช้งานโปรแกรม

streamlit run [program.py]

#เผยแพร่โปรแกรม https://ngrok.com/

ngrok http 8501
