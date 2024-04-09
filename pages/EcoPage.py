from playwright.sync_api import Page
import os
import pytest

class EcoPage:
    def __init__(self, page: Page):
        self.page = page      

        # Словарь с локаторами счетчиков для скриншотов
        self.counters = {
            "water": page.locator(".desktop-impact-items-F7T6E > div:nth-child(4)") ,
            "CO2": page.locator(".desktop-impact-items-F7T6E > div:nth-child(2)") ,
            "energy": page.locator(".desktop-impact-items-F7T6E > div:nth-child(6)"),
        }

        #Cловарь с локаторами значений счетчиков 
        self.counters_values = {
            "water": page.locator(".desktop-impact-items-F7T6E > div:nth-child(4) .desktop-value-Nd1tR") ,
            "CO2":  page.locator(".desktop-impact-items-F7T6E > div:nth-child(2) .desktop-value-Nd1tR"),
            "energy": page.locator(".desktop-impact-items-F7T6E > div:nth-child(6) .desktop-value-Nd1tR"),
        }

        #Cловарь с локаторами единиц измерения счетчиков 
        self.counters_units = {
            "water": page.locator(".desktop-impact-items-F7T6E > div:nth-child(4) .desktop-unit-puWVS") ,
            "CO2":  page.locator(".desktop-impact-items-F7T6E > div:nth-child(2) .desktop-unit-puWVS")  ,
            "energy": page.locator(".desktop-impact-items-F7T6E > div:nth-child(6) .desktop-unit-puWVS") ,
        }

    def navigate(self):
        self.page.goto('https://www.avito.ru/avito-care/eco-impact')
        # Даем тестовому пользователю время на авторизацию (например, 40 секунд)
        self.page.wait_for_timeout(40000)


    def take_counters_screenshot(self,request, output_dir="output" ):
       
        # Создание скриншотов каждого счетчика
        for counter_name, selector in self.counters.items():
            screenshot_path = os.path.join(output_dir, f"{request.node.name}_{counter_name}.png")
            selector.screenshot(path=screenshot_path)
            print(f"Скриншот {counter_name} сохранен в {screenshot_path}")

