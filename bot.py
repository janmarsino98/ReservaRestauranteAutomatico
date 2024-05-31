# IMPORTS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import re


class Bot():
    
    def __init__(self):
        options = Options()
        options.add_argument("--incognito")
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
    
    def scrap_site(self):
        self.driver.get("https://www.sevenrooms.com/reservations/asadoretxebarri")
        self.select_month("septiembre", "2024", "12")
        self.select_comensals("8")
        self.select_hora("18:45")
        self.buscar()
        self.fill_data(
            name="Pepe",
            last_name="Fernandez",
            email="pepefernandez@gmail.com",
            phone="657481525"
        )

    def select_month(self, month, year, day):
        current_date = ""
        pattern = "opacity: 0.5"
        
        next_date_btn = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[@aria-label='increment month']"))
            )
        while current_date != month + " " + year:
            next_date_btn.click()
            current_date = self.driver.find_element(By.XPATH, "//button[@aria-label='increment month']/preceding-sibling::div[1]/span").text
            time.sleep(0.2)
            
        time.sleep(2)
        day_cell = self.driver.find_element(By.XPATH, f"//td[text()={day}]")
        
        print(re.match(pattern, day_cell.get_attribute("style")))
        
        if re.match(pattern, day_cell.get_attribute("style")):
            day_cell.click()
            
        else:
            print("El dia no está disponible")
            exit()
        
    def select_comensals(self, comensals):
        curr_hour = self.driver.find_element(By.XPATH, "//span[@aria-label='Comensales']")
        self.driver.execute_script("arguments[0].click()", curr_hour)
        desired_hour_option = self.driver.find_element(By.XPATH, f"//button[text()='{comensals}']")
        desired_hour_option.click()
        
        
    def select_hora(self, hour):
        curr_hour = self.driver.find_element(By.XPATH, "//span[@aria-label='Hora']")
        self.driver.execute_script("arguments[0].click()", curr_hour)
        desired_hour_option = self.driver.find_element(By.XPATH, f"//button[text()='{hour}']")
        desired_hour_option.click()
        
    def buscar(self):
        btn_buscar = self.driver.find_element(By.XPATH, "//button[text()='Buscar']")
        btn_buscar.click()
        
    def fill_data(self, name, last_name, email, phone):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='Envíe una solicitud']"))
        ) 
        
        presentar_solicitud_btn = self.driver.find_element(By.XPATH, "//button[text()='Presentar una solicitud']")
        presentar_solicitud_btn.click()
        
        name_field = self.driver.find_element(By.XPATH, "//input[@id='sr-nombre-*']")
        for chr in name:
            name_field.send_keys(chr)
            time.sleep(random.random()*0.15)
            
        last_name_field = self.driver.find_element(By.XPATH, "//input[@id='sr-apellido-*']")
        for chr in last_name:
            last_name_field.send_keys(chr)
            time.sleep(random.random()*0.15)
            
        email_field = self.driver.find_element(By.XPATH, "//input[@id='sr-dirección-de correo electrónico *']")
        for chr in email:
            email_field.send_keys(chr)
            time.sleep(random.random()*0.15)
            
        phone_field = self.driver.find_element(By.XPATH, "//input[@aria-label='Phone Number']")
        for chr in phone:
            phone_field.send_keys(chr)
            time.sleep(random.random()*0.15)
        
        time.sleep(5)
        presentar_solicitud_btn = self.driver.find_element(By.XPATH, "//button[text()='Presentar una solicitud']")
        presentar_solicitud_btn.click()
        
        
bot = Bot()

bot.scrap_site()