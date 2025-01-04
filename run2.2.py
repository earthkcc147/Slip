import os
from colorama import init, Fore, Style
from function import login
from function import create_fake_receipt
from function.send.discord import send_to_discord
from banners import print_intro
from function.input import get_user_input  # นำเข้าฟังก์ชันจาก input.py

# เริ่มต้นการใช้งาน colorama
init(autoreset=True)

def clear_console():
    # ตรวจสอบว่ากำลังทำงานในระบบปฏิบัติการใด
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux หรือ macOS หรือ Termux
        os.system('clear')


print_intro()
input(Fore.GREEN + "\nกด Enter เพื่อดำเนินการต่อ...")
clear_console()

# เรียกใช้ฟังก์ชัน login ก่อนการสร้างสลีปปลอม
if login():

    # เรียกใช้ฟังก์ชันในการรับข้อมูลจากผู้ใช้
    name_user_id, name_me_id, phone_me_id, money_id = get_user_input()

    # เรียกใช้ฟังก์ชันในการสร้างสลีปปลอม
    image_path = create_fake_receipt(name_user_id, name_me_id, phone_me_id, money_id)

    # แสดงข้อความยืนยันหลังจากสร้างสลีปปลอม
    print("\n🎉 สลีปปลอมถูกสร้างและบันทึกเรียบร้อยแล้ว! 🖼️")
    print("📂 ภาพถูกบันทึกในโฟลเดอร์ 'textnew'")

    # เริ่มจากสร้างชื่อไฟล์ใหม่ตามที่ต้องการ
    image_filename = f"{name_user_id}_{name_me_id}_{money_id}_{phone_me_id}.png"
    image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "textnew", image_filename))

    # เรียกใช้ฟังก์ชันเพื่อส่งไปยัง Discord
    # send_to_discord(image_path, f"สลีปปลอมของ {name_user_id} ถูกสร้างเรียบร้อยแล้ว!")

    # สร้างข้อความพร้อมรายละเอียดเพิ่มเติม
    message = (
        f"🎉 สลีปปลอมถูกสร้างเรียบร้อย! \n"
        f"📄 รายละเอียด: \n"
        f"👤 ผู้โอน: {name_user_id}\n"
        f"👥 ผู้รับ: {name_me_id}\n"
        f"📞 เบอร์ผู้รับ: {phone_me_id}\n"
        f"💵 จำนวนเงิน: {money_id}.00 บาท"
    )

    # เรียกใช้ฟังก์ชันเพื่อส่งไปยัง Discord
    send_to_discord(image_path, message)

else:
    print("ไม่สามารถเข้าสู่ระบบได้ ❌")