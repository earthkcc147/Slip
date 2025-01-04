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

    # สร้างข้อความที่จะส่ง (รายละเอียดที่กรอก)
    message = (
        f"🎉 สลีปปลอมถูกสร้างเรียบร้อย! \n"
        f"📄 รายละเอียด: \n"
        f"👤 ผู้โอน: {name_user_id}\n"
        f"👥 ผู้รับ: {name_me_id}\n"
        f"📞 เบอร์ผู้รับ: {phone_me_id}\n"
        f"💵 จำนวนเงิน: {money_id}.00 บาท"
    )

    # สร้างข้อมูลที่ต้องการส่ง
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