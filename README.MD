# Kasir Barcode Scanner

Proyek ini adalah sistem pemindaian barcode yang menggunakan kamera untuk membaca barcode dan secara otomatis mengisi data ke dalam form di halaman web. Proyek ini menggunakan OpenCV untuk menangkap gambar dari kamera, pyzbar untuk mendekode barcode, dan Selenium untuk mengotomatisasi pengisian form di halaman web.

## Fitur

- Memindai barcode menggunakan kamera.
- Menampilkan hasil pemindaian barcode di jendela video.
- Mengisi form secara otomatis di halaman web setelah barcode dipindai.
- Mencegah spam dengan menambahkan jeda waktu 3 detik antara pemindaian barcode.

## Dependensi

Pastikan Anda menginstal dependensi berikut sebelum menjalankan proyek:

- OpenCV
- pyzbar
- pyautogui
- Selenium
- ChromeDriver (untuk Selenium)
