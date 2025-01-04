import time
import random
import sys

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

    while time.time() - start_time < duration:
        if step_index < len(steps):  # ถ้ายังมีข้อความในลำดับ
            print(steps[step_index])
            step_index += 1
        else:  # แสดงข้อความสุ่มเมื่อหมดลำดับ
            print(f"[INFO] {random.randint(0, 9999):04x}: Task in progress...")
        
        # เพิ่มแอนิเมชันจุดที่เคลื่อนไหว
        for _ in range(3):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(0.3)
        print()  # สร้างบรรทัดใหม่
    
    # แสดงข้อความสำเร็จเมื่อครบเวลา
    print("[COMPLETE] All tasks have been executed successfully!\n")

# hacker_loading_screen(duration=5)  # รอ 5 วินาที พร้อมแสดงผล