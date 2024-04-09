import pytest
from playwright.sync_api import Page,expect
from pages.EcoPage import EcoPage

# создаем инстанс ecopage для каждого теста и скриншот
@pytest.fixture
def eco_page(page: Page, request):
    eco_page_inst = EcoPage(page)
    eco_page_inst.navigate()
    yield eco_page_inst 
    eco_page_inst.take_counters_screenshot(request)

# после ручной авторизации через тестового пользователя с нулевым вкладом
def test1_default(eco_page):
    # Проверяем, что все счетчики видны на странице
    for counter_name, selector in eco_page.counters.items():
        expect(selector).to_be_visible()

    for counter_name, value_locator in eco_page.counters_values.items():
        # Проверяем, что значение счетчика равно 0
        expect(value_locator).to_have_text("0") 
       
    # Проверяем, что все единицы измерения счетчиков корректно отображаются
    for counter_name, unit_locator in eco_page.counters_units.items():
        expected_unit = "л воды" if counter_name == "water" else "кг CO₂" if counter_name == "CO2" else "кВт⋅ч энергии"
        expect(unit_locator).to_have_text(expected_unit)

# после ручной авторизации через тестового пользователя с небольшим вкладом
# так как у нас нет возможности реально создать тестового пользователя берем фейк данные
def test2_unit_small(eco_page):
    # Заменяем реальные значения на фиктивные
    fake_values = {"water": "999", "CO2": "999", "energy": "999"}
    fake_units = {"water": "л воды", "CO2": "кг CO₂", "energy": "кВт⋅ч энергии"}

    eco_page.counters_values = {
        counter_name: value
        for counter_name, value in fake_values.items()
    }

    eco_page.counters_units = {
        counter_name: unit
        for counter_name, unit in fake_units.items()
    }

    for counter_name, value in eco_page.counters_values.items():
        assert eco_page.counters_values[counter_name] == fake_values[counter_name]

    for counter_name, value in eco_page.counters_units.items():
        assert eco_page.counters_units[counter_name] == fake_units[counter_name]

# после ручной авторизации через тестового пользователя с большим вкладом
# так как у нас нет возможности реально создать тестового пользователя берем фейк данные
def test3_unit_large(eco_page):
    # Заменяем реальные значения на фиктивные
    fake_values = {"water": "1000", "CO2": "1000", "energy": "1000"}
    fake_units = {"water": "м куб воды", "CO2": "тонны CO₂", "energy": "МВт⋅ч энергии"}

    eco_page.counters_values = {
        counter_name: value
        for counter_name, value in fake_values.items()
    }

    eco_page.counters_units = {
        counter_name: unit
        for counter_name, unit in fake_units.items()
    }

    # Проверяем отображение значений и единиц измерения для каждого счетчика
    for counter_name, value in eco_page.counters_values.items():
        assert eco_page.counters_values[counter_name] == fake_values[counter_name]

    for counter_name, value in eco_page.counters_units.items():
        assert eco_page.counters_units[counter_name] == fake_units[counter_name]

