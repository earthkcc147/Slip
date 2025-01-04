import time
import random
import sys
from colorama import init, Fore

# เริ่มต้นการใช้งาน colorama
init(autoreset=True)

def hacker_loading_screen(duration=5):
    # กำหนดข้อความลำดับขั้นตอน
    steps = [
        "[SYSTEM] Initializing environment variables...",
        "[SYSTEM] Connecting to secure server...",
        "[SECURITY] Verifying access token...",
        "[NETWORK] Establishing encrypted channel...",
        "[FILE] Scanning directories for required assets...",
        "[DATA] Downloading essential libraries...",
        "[COMPILER] Compiling core components...",
        "[SYSTEM] Finalizing configurations...",
        "[SUCCESS] Process completed successfully!"
    ]

    # กำหนดเวลาเริ่มต้น
    start_time = time.time()
    step_index = 0  # ติดตามขั้นตอนปัจจุบัน

    # แสดงการดาวน์โหลดพร้อมกับการแสดงข้อความขั้นตอน
    while time.time() - start_time < duration:
        if step_index < len(steps):  # ถ้ายังมีข้อความในลำดับ
            sys.stdout.write(Fore.GREEN + f"{steps[step_index]}")
            sys.stdout.flush()
            step_index += 1
        else:  # แสดงข้อความสุ่มเมื่อหมดลำดับ
            sys.stdout.write(Fore.YELLOW + f"[INFO] {random.randint(0, 9999):04x}: Task in progress...")
            sys.stdout.flush()

        # สร้างแอนิเมชันหลอดโหลด
        sys.stdout.write("\r[")
        for i in range(20):  # จำนวนบล็อคในหลอด
            if i < (time.time() - start_time) / duration * 20:  # คำนวณความคืบหน้า
                sys.stdout.write("█")
            else:
                sys.stdout.write("-")
        sys.stdout.write(f"] {int((time.time() - start_time) / duration * 100)}%")
        sys.stdout.flush()

        time.sleep(0.3)

    # แสดงข้อความสำเร็จเมื่อครบเวลา
    sys.stdout.write("\n[COMPLETE] All tasks have been executed successfully!\n")
    sys.stdout.flush()

def hacker_download_animation(duration=5):
    # ฟังก์ชันสำหรับแสดงการดาวน์โหลดแบบ hacker
    print(Fore.GREEN + "\nเริ่มการดาวน์โหลด...")

    # เริ่มการดาวน์โหลดพร้อมกับการแสดงการโหลด
    for _ in range(duration):
        sys.stdout.write(Fore.RED + "\r[███████████████████----] " + str(duration) + "s Remaining...")
        sys.stdout.flush()
        time.sleep(1)
        duration -= 1

    sys.stdout.write(Fore.GREEN + "\r[███████████████████████] " + "ดาวน์โหลดเสร็จสิ้น!\n")
    sys.stdout.flush()

# เรียกใช้ฟังก์ชันที่รวมการดาวน์โหลดและแอนิเมชัน
def run_hacker_simulation():
    print(Fore.GREEN + "เริ่มการดาวน์โหลด...")
    # เรียกใช้การโหลดที่มีแอนิเมชันพร้อมกับข้อความ
    hacker_loading_screen(5)  # แสดงแอนิเมชันขั้นตอนการโหลด
    hacker_download_animation(5)  # แสดงหน้าต่างดาวน์โหลด

# เรียกใช้ฟังก์ชันทั้งหมด
# run_hacker_simulation()