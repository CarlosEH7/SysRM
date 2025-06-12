import psutil
import time
import os

def clear_screen():
    # Clear command for Windows or macOS/Linux
    os.system('cls' if os.name == 'nt' else 'clear')

def monitor():
    try:
        while True:
            clear_screen()

            cpu_percent = psutil.cpu_percent(interval=1)
            memory_percent = psutil.virtual_memory().percent

            print("System Resource Monitor\n")
            print(f"CPU Usage:    {cpu_percent}%")
            print(f"Memory Usage: {memory_percent}%")
            print("-" * 30)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nMonitor stopped.")

if __name__ == "__main__":
    monitor()
