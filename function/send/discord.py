# function/send/discord.py
import os
import requests
from dotenv import load_dotenv

# โหลดค่าจากไฟล์ .env
load_dotenv()

def send_to_discord(image_path, message):
    # ดึง Webhook URL จากไฟล์ .env
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL_SLIP")

    if not webhook_url:
        print("ไม่พบ Webhook URL ในไฟล์ .env ❌")
        return

    # สร้างข้อความที่จะส่ง
    data = {
        "content": message  # ข้อความที่จะส่งไปยัง Discord
    }

    # เปิดไฟล์รูปภาพ
    with open(image_path, 'rb') as image_file:
        files = {
            'file': image_file
        }

        # ส่งข้อมูลไปที่ Discord ผ่าน Webhook
        response = requests.post(webhook_url, data=data, files=files)

        # ตรวจสอบผลลัพธ์จากการส่ง
        if response.status_code == 200:
            print("ส่งข้อมูลและรูปภาพไปยัง Discord สำเร็จ ✅")
        else:
            print(f"ไม่สามารถส่งข้อมูลไปที่ Discord ได้ (Error: {response.status_code}) ❌")