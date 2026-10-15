import json
import time

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def start_hub():
    config = load_config()
    print(f"[*] Starting {config['device_name']}...")
    print(f"[*] LEDs: {config['led_count']} on GPIO {config['led_pin']}")
    print(f"[*] Brightness: {config['brightness']}/255")
    print("[+] LED Hub is ACTIVE. Press Ctrl+C to exit.")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[-] Shutting down LED Hub cleanly...")

if __name__ == "__main__":
    start_hub()
