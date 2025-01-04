# main.py
from function import create_fake_receipt

# รับข้อมูลจากผู้ใช้
name_user_id = input("ชื่อผู้โอนจ่าย: ")
name_me_id = input("ชื่อผู้รับเงิน: ")
phone_me_id = input("เบอร์โทรศัพท์ผู้รับ: ")
money_id = input("จำนวนเงิน: ")

# เรียกใช้ฟังก์ชันในการสร้างสลีปปลอม
create_fake_receipt(name_user_id, name_me_id, phone_me_id, money_id)
