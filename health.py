import psutil
import datetime
import csv

FILENAME = "health-log.csv"

def get_cpu():
    return psutil.cpu_percent(interval=1)


def get_memory():
    mem = psutil.virtual_memory()
    return mem.percent

def get_disk():
    disk_use = psutil.disk_usage('/')
    return disk_use.percent

def get_battery():
    bat = psutil.sensors_battery()
    if bat is None:
        return "N/A"
    return bat.percent

def save_report():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = {
        "timestamp": now,"cpu": get_cpu(),
        "memory": get_memory(),
        "disk": get_disk(),
        "battery": get_battery()
        }
    with open(FILENAME, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp", "cpu", "memory", "disk", "battery"])
        writer.writerow(row)

def print_report():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("=" * 30)
    print("🖥️  DEVICE HEALTH REPORT")
    print("=" * 30)
    print(f"🕐 Time: {now}")
    print(f"💻 CPU: {get_cpu()} %")
    print(f"🧠 RAM: {get_memory()} %")
    print(f"💾 Disk: {get_disk()} %")
    print(f"🔋 Battery: {get_battery()} %")
    print("=" * 30)

print_report()
save_report()