import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# inisialisasi Web Driver 
driver = webdriver.Edge()

# Membuka halaman web google
driver.get('https://google.com')

# Mencari elemen input pada pendarian google
search_input = driver.find_element(By.NAME, "q")

# masukan kata kunci pencarian
search_input.send_keys("Kampus digital masa gitu")
time.sleep(2)

# manekan tombol enter untuk melakukan pencarian
search_input.send_keys(Keys.ENTER)

# Misalnya, dapatkan judul halaman saat Ini 
page_title = driver.title
print("Judul Halaman:", page_title)

# penundaaan waktu loading agar tidak langsung close atau quit
time.sleep(2)

# menutup driver 
driver.quit()