import pyautogui
import time

prompt_x = 124
prompt_y = 334
enter_x = 139
enter_y = 643


fixed_offset_x = 65 

def load_keywords(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

keywords = load_keywords("input.txt")

def setup_canvas_fixed():
    print("\n=== SETUP KOLOM GAMBAR (OFFSET FIXED) ===")
    
    ("🖱️ Arahkan ke KOLOM GAMBAR PERTAMA (canvas pertama), tunggu 5 detik...")
    time.sleep(5)
    canvas_x, canvas_y = pyautogui.position()
    print(f"📍 Posisi canvas pertama: ({canvas_x}, {canvas_y})")
    time.sleep(7.0)
    
    return canvas_x, canvas_y


print("=== AUTO INPUT RECRAAFT (OFFSET FIXED) ===")
input("Pastikan Recraaft sudah terbuka penuh, lalu tekan Enter untuk mulai setup...")


canvas_x, canvas_y = setup_canvas_fixed()


print("\nMulai input otomatis dalam 5 detik...")
time.sleep(5)

for keyword in keywords:
    print(f"\n🟢 Mengisi keyword: {keyword}")
    
    # Klik canvas
    pyautogui.click(canvas_x, canvas_y)
    print("👉 Klik canvas")
    time.sleep(1.0)
    
    # Klik kolom prompt dan isi keyword
    pyautogui.click(prompt_x, prompt_y)
    print("📝 Klik prompt")
    time.sleep(1.0)
    pyautogui.write(keyword)
    print(f"⌨️ Menulis: {keyword}")
    time.sleep(1.0)
    

    # Tunggu proses generate
    print("⏳ Menunggu generate (4 detik)...")
    time.sleep(4.0)
    
    # Geser hanya posisi canvas ke kanan (pakai offset tetap)
    canvas_x += fixed_offset_x

print("\n🎉 Semua keyword selesai diisi.")
