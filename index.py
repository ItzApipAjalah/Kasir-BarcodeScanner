import cv2
from pyzbar import pyzbar
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import threading

def login(driver):
    driver.get("http://127.0.0.1:8000/login")

    # Mengisi form login
    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, "button.login-button")

    email_input.send_keys("staff@amwp.website")
    password_input.send_keys("63935845")
    login_button.click()

    # Tunggu hingga login selesai dan halaman dashboard terbuka
    time.sleep(5)

def process_barcode(driver, barcode_data):
    # Mengisi form secara otomatis di halaman web
    input_element = driver.find_element(By.ID, "input-produk-id")
    input_element.clear()
    input_element.send_keys(barcode_data)
    add_button = driver.find_element(By.ID, "add-by-id-button")
    add_button.click()
    
    # Memberikan delay 3 detik untuk menghindari spam
    time.sleep(3)

def scan_barcode():
    # Setup Selenium WebDriver
    driver = webdriver.Chrome()  # Pastikan ChromeDriver ada di PATH Anda

    # Login ke halaman web
    login(driver)

    # Mengakses halaman dashboard setelah login
    driver.get("http://127.0.0.1:8000/petugas/dashboard")

    # Menggunakan kamera
    cap = cv2.VideoCapture(0)

    last_processed_time = 0
    delay = 3  # delay in seconds

    while True:
        # Membaca frame dari kamera
        ret, frame = cap.read()
        
        if not ret:
            print("Gagal mengambil gambar dari kamera.")
            break

        # Memindai barcode dari frame
        barcodes = pyzbar.decode(frame)
        
        for barcode in barcodes:
            # Menampilkan hasil pemindaian pada frame
            (x, y, w, h) = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            barcode_data = barcode.data.decode("utf-8")
            barcode_type = barcode.type

            text = f"{barcode_type}: {barcode_data}"
            cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Proses barcode jika delay telah terlewati
            current_time = time.time()
            if current_time - last_processed_time >= delay:
                last_processed_time = current_time
                threading.Thread(target=process_barcode, args=(driver, barcode_data)).start()

        # Menampilkan frame dengan hasil pemindaian
        cv2.imshow('Barcode Scanner', frame)

        # Keluar dari loop jika tombol 'q' ditekan
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Membersihkan resource
    cap.release()
    cv2.destroyAllWindows()
    driver.quit()

if __name__ == "__main__":
    scan_barcode()
