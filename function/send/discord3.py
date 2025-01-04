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

    # สร้างข้อมูล Embed
    embed_data = {
        "embeds": [
            {
                "title": "🎉 สลีปปลอมถูกสร้างเรียบร้อย! 🎉",
                "description": (
                    f"📄 รายละเอียด: \n"
                    f"👤 ผู้โอน: {name_user_id}\n"
                    f"👥 ผู้รับ: {name_me_id}\n"
                    f"📞 เบอร์ผู้รับ: {phone_me_id}\n"
                    f"💵 จำนวนเงิน: {money_id}.00 บาท"
                ),
                "color": 3066993,  # ใช้สีเขียว (สามารถปรับสีได้)
                "fields": [
                    {
                        "name": "ผู้โอน",
                        "value": name_user_id,
                        "inline": True
                    },
                    {
                        "name": "ผู้รับ",
                        "value": name_me_id,
                        "inline": True
                    },
                    {
                        "name": "เบอร์โทรศัพท์",
                        "value": phone_me_id,
                        "inline": True
                    },
                    {
                        "name": "จำนวนเงิน",
                        "value": f"{money_id}.00 บาท",
                        "inline": True
                    }
                ],
                "footer": {
                    "text": "สลีปปลอมโดยระบบ"
                },
                "image": {
                    "url": f"attachment://{os.path.basename(image_path)}"  # ใช้ไฟล์ภาพที่แนบไปกับการส่ง
                }
            }
        ]
    }

    # สร้างข้อมูลที่ต้องการส่ง
    data = {
        "content": "🎉 สลีปปลอมถูกสร้างเรียบร้อย!"  # ข้อความหลัก
    }

    # เปิดไฟล์รูปภาพ
    with open(image_path, 'rb') as image_file:
        files = {
            'file': image_file
        }

        # ส่งข้อมูลไปที่ Discord ผ่าน Webhook
        response = requests.post(webhook_url, data=data, json=embed_data, files=files)

        # ตรวจสอบผลลัพธ์จากการส่ง
        if response.status_code == 200:
            print("ส่งข้อมูลและรูปภาพไปยัง Discord สำเร็จ ✅")
        else:
            print(f"ไม่สามารถส่งข้อมูลไปที่ Discord ได้ (Error: {response.status_code}) ❌")