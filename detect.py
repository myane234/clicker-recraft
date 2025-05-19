import pyautogui
import time

print("🕹️ Arahkan kursor ke posisi yang lo mau... (5 detik)")
time.sleep(5)

posisi = pyautogui.position()
print(f"📍 Posisi kursor: {posisi}")