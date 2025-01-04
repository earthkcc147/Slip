import os
from function import login
from function import create_fake_receipt
from function.send.discord_id import send_to_discord_user  # เปลี่ยนเป็นฟังก์ชันใหม่

# เรียกใช้ฟังก์ชัน login ก่อนการสร้างสลีปปลอม
if login():
    # รับข้อมูลจากผู้ใช้
    name_user_id = input("ชื่อผู้โอนจ่าย: ")
    name_me_id = input("ชื่อผู้รับเงิน: ")
    phone_me_id = input("เบอร์โทรศัพท์ผู้รับ: ")
    money_id = input("จำนวนเงิน: ")

    # แสดงข้อมูลที่ผู้ใช้กรอก
    print("\n📝 รายละเอียดที่กรอก:")
    print(f"👤 ชื่อผู้โอนจ่าย: {name_user_id}")
    print(f"💵 จำนวนเงิน: {money_id} บาท")
    print(f"👨‍💻 ชื่อผู้รับเงิน: {name_me_id}")
    print(f"📞 เบอร์โทรศัพท์ผู้รับ: {phone_me_id}")

    # เรียกใช้ฟังก์ชันในการสร้างสลีปปลอม
    print("\n🔨 กำลังสร้างสลีปปลอม... ⏳")
    image_path = create_fake_receipt(name_user_id, name_me_id, phone_me_id, money_id)

    # แสดงข้อความยืนยันหลังจากสร้างสลีปปลอม
    print("\n🎉 สลีปปลอมถูกสร้างและบันทึกเรียบร้อยแล้ว! 🖼️")
    print("📂 ภาพถูกบันทึกในโฟลเดอร์ 'textnew'")

    # สร้างข้อความพร้อมรายละเอียดเพิ่มเติม
    message = (
        f"🎉 สลีปปลอมถูกสร้างเรียบร้อย! \n"
        f"📄 รายละเอียด: \n"
        f"👤 ผู้โอน: {name_user_id}\n"
        f"👥 ผู้รับ: {name_me_id}\n"
        f"📞 เบอร์ผู้รับ: {phone_me_id}\n"
        f"💵 จำนวนเงิน: {money_id}.00 บาท"
    )

    # ถามผู้ใช้ว่าต้องการส่งหรือไม่
    send_choice = input("คุณต้องการส่งไปที่ ID ของผู้ใช้ Discord หรือไม่? (y/n): ").lower()

    if send_choice == "y":
        # รับ ID ผู้ใช้ Discord
        user_id = input("กรุณาใส่ ID ของผู้ใช้ Discord: ").strip()
        send_to_discord_user(user_id, image_path, message)
    else:
        print("ยกเลิกการส่งข้อมูล ✅")
else:
    print("ไม่สามารถเข้าสู่ระบบได้ ❌")