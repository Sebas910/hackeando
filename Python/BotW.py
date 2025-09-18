from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Ruta al ChromeDriver
driver_path = "C:/Users/joseq/Desktop/Programacion/Python/Programas/Chromedriver/chromedriver.exe"

# Configuración recomendada para Selenium 4+
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=driver_path, options=options)

driver.get("https://web.whatsapp.com/")
input("Escanea el código QR y presiona Enter aquí...")

contacto = "Nombre de tu amigo"
mensaje = "¡Hola! Mensaje automático :)"

search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
search_box.click()
search_box.send_keys(contacto)
search_box.send_keys(Keys.ENTER)
time.sleep(2)

for i in range(5):
    box_mensaje = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
    box_mensaje.send_keys(f"{mensaje} #{i+1}")
    box_mensaje.send_keys(Keys.ENTER)
    time.sleep(1)

# driver.quit()