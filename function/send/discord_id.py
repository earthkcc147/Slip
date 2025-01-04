import os
import requests
from dotenv import load_dotenv

# โหลดค่าจากไฟล์ .env
load_dotenv()

# ดึง Token ของ Discord Bot จากไฟล์ .env
BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

def send_to_discord_user(user_id, image_path, message):
    if not BOT_TOKEN:
        print("ไม่พบ Discord Bot Token ในไฟล์ .env ❌")
        return

    # URL สำหรับสร้าง DM Channel
    url_create_channel = "https://discord.com/api/v9/users/@me/channels"

    # สร้าง DM Channel กับผู้ใช้
    payload = {"recipient_id": user_id}
    headers = {"Authorization": f"Bot {BOT_TOKEN}"}
    response = requests.post(url_create_channel, json=payload, headers=headers)

    if response.status_code == 200:
        channel_id = response.json()["id"]

        # ส่งข้อความพร้อมรูปภาพไปยัง DM Channel
        with open(image_path, 'rb') as image_file:
            files = {"file": image_file}
            data = {"content": message}
            url_send_message = f"https://discord.com/api/v9/channels/{channel_id}/messages"
            message_response = requests.post(url_send_message, headers=headers, data=data, files=files)

            if message_response.status_code == 200:
                print("ส่งข้อความและรูปภาพสำเร็จ ✅")
            else:
                print(f"ไม่สามารถส่งข้อความได้ (Error: {message_response.status_code}) ❌")
    else:
        print(f"ไม่สามารถสร้าง DM Channel ได้ (Error: {response.status_code}) ❌")