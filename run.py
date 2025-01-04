# main.py
from function import create_fake_receipt

# รับข้อมูลจากผู้ใช้
name_user_id = input("ชื่อผู้โอนจ่าย: ")
name_me_id = input("ชื่อผู้รับเงิน: ")
phone_me_id = input("เบอร์โทรศัพท์ผู้รับ: ")
money_id = input("จำนวนเงิน: ")

# แสดงข้อมูลที่ผู้ใช้กรอก
print("\nรายละเอียดที่กรอก:")
print(f"ชื่อผู้โอนจ่าย: {name_user_id}")
print(f"ชื่อผู้รับเงิน: {name_me_id}")
print(f"เบอร์โทรศัพท์ผู้รับ: {phone_me_id}")
print(f"จำนวนเงิน: {money_id} บาท")

# เรียกใช้ฟังก์ชันในการสร้างสลีปปลอม
create_fake_receipt(name_user_id, name_me_id, phone_me_id, money_id)

print("\nสลีปปลอมถูกสร้างและบันทึกเรียบร้อยแล้ว!")