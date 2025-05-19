import pyautogui
import time


prompt_x = 124
prompt_y = 334
enter_x = 139
enter_y = 643



def load_keywords(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

keywords = load_keywords("input.txt")
def setup_canvas():
    print("\n=== SETUP KOLOM GAMBAR ===")
    
    print("🖱️ Arahkan ke KOLOM GAMBAR PERTAMA (canvas pertama), tunggu 5 detik...")
    time.sleep(5)
    canvas_x, canvas_y = pyautogui.position()
    print(f"📍 Posisi canvas pertama: ({canvas_x}, {canvas_y})")
    
    input("\n🖱️ Arahkan ke KOLOM GAMBAR KEDUA (canvas kedua), lalu tekan Enter jika sudah siap...")
    time.sleep(5)
    canvas2_x, _ = pyautogui.position()
    offset_x = canvas2_x - canvas_x
    print(f"📏 Offset horizontal antar canvas: {offset_x} pixel")
    
    return canvas_x, canvas_y, offset_x


print("=== AUTO INPUT RECRAAFT (SKEMA BARU) ===")
input("Pastikan Recraaft sudah terbuka penuh, lalu tekan Enter untuk mulai setup...")

# === Setup posisi canvas ===
canvas_x, canvas_y, offset_x = setup_canvas()


print("\nMulai input otomatis dalam 5 detik...")
time.sleep(5)

for keyword in keywords:
    print(f"\n🟢 Mengisi keyword: {keyword}")
    
    # 1. Klik canvas
    pyautogui.click(canvas_x, canvas_y)
    print("👉 Klik canvas")
    time.sleep(1.0)
    
    # 2. Klik kolom prompt dan isi keyword
    pyautogui.click(prompt_x, prompt_y)
    print("📝 Klik prompt")
    time.sleep(1.0)
    pyautogui.write(keyword)
    print(f"⌨️ Menulis: {keyword}")
    time.sleep(1.0)
    
    # 3. Klik tombol Enter
    
    
    # 4. Tunggu proses generate
    print("⏳ Menunggu generate (4 detik)...")
    time.sleep(4.0)
    
    
    canvas_x += offset_x

print("\n🎉 Semua keyword selesai diisi.")
