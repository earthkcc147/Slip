import time
import sys
from colorama import Fore

def hacker_download_animation(duration=5):
    # ฟังก์ชันสำหรับแสดงการดาวน์โหลดแบบ hacker
    print(Fore.GREEN + "เริ่มการดาวน์โหลด...")

    # สร้างหน้าต่างดาวน์โหลดแบบ hacker
    for _ in range(duration):
        sys.stdout.write(Fore.RED + "\r[███████████████████----] " + str(duration) + "s Remaining...")
        sys.stdout.flush()
        time.sleep(1)
        duration -= 1

    sys.stdout.write(Fore.GREEN + "\r[███████████████████████] " + "ดาวน์โหลดเสร็จสิ้น!\n")
    sys.stdout.flush()


# hacker_download_animation(5)  # แสดงหน้าต่างดาวน์โหลด