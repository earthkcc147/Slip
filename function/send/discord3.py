import os
import requests
from dotenv import load_dotenv

# โหลดค่าจากไฟล์ .env
load_dotenv()

def send_to_discord(image_path, name_user_id, name_me_id, phone_me_id, money_id):
    # ดึง Webhook URL จากไฟล์ .env
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL_SLIP")

    if not webhook_url:
        print("ไม่พบ Webhook URL ในไฟล์ .env ❌")
        return

    # สร้าง embed message
    embed_data = {
        "embeds": [
            {
                "title": "🎉 สลีปปลอมถูกสร้างเรียบร้อย!",
                "description": "📄 รายละเอียด: ",
                "fields": [
                    {
                        "name": "👤 ผู้โอน",
                        "value": name_user_id,
                        "inline": True
                    },
                    {
                        "name": "👥 ผู้รับ",
                        "value": name_me_id,
                        "inline": True
                    },
                    {
                        "name": "📞 เบอร์ผู้รับ",
                        "value": phone_me_id,
                        "inline": True
                    },
                    {
                        "name": "💵 จำนวนเงิน",
                        "value": f"{money_id}.00 บาท",
                        "inline": True
                    }
                ],
                "color": 3066993  # สีของ Embed
            }
        ]
    }

    # สร้างข้อมูลที่จะส่ง
    data = embed_data

    # เปิดไฟล์รูปภาพ
    with open(image_path, 'rb') as image_file:
        files = {
            'file': image_file
        }

        # ส่งข้อมูลไปที่ Discord ผ่าน Webhook
        response = requests.post(webhook_url, json=data, files=files)

        # ตรวจสอบผลลัพธ์จากการส่ง
        if response.status_code == 200:
            print("ส่งข้อมูลและรูปภาพไปยัง Discord สำเร็จ ✅")
        else:
            print(f"ไม่สามารถส่งข้อมูลไปที่ Discord ได้ (Error: {response.status_code}) ❌")