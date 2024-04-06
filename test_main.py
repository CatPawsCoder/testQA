import re
from playwright.sync_api import Page, expect

def test_visual1 (page: Page):

    page.goto('https://www.avito.ru/avito-care/eco-impact')
   
    # создание счетчика воды
    water = page.locator(".desktop-video-value-hsJQq:has-text('млн м³ воды')")
    # page.locator(".desktop-video-value-hsJQq").nth(0)
    expect(water).to_be_visible()  # Проверяем, что счетчик виден
    water.screenshot(path="output/water_screen.png")

    # создание счетчика co2

    co2 = page.locator(".desktop-video-value-hsJQq:has-text('млн тонн CO₂')")
    # page.locator(".desktop-video-value-hsJQq").nth(1)
    expect(co2).to_be_visible()  # Проверяем, что счетчик виден
    co2.screenshot(path="output/co2_screen.png")

    # создаем счетчик электричества
    electro = page.locator(".desktop-video-value-hsJQq:has-text('млрд кВт·ч энергии')")
    # page.locator(".desktop-video-value-hsJQq").nth(2)
    expect(electro).to_be_visible()  # Проверяем, что счетчик виден
    electro.screenshot(path="output/electro_screen.png")

    # Создание скриншота всей страницы
    page.screenshot(path="output/full_page.png",full_page=True)

    # # проверка expect
    # expect(page).to_have_title('Google')
    # # mail_link = page.get_by_role ('link',  name = 'Mail')
    # # mail_link = page.locator('text="Почта"')
    # # mail_link = page.locator('a.gb_H[aria-label="Почта (откроется новая вкладка)"]')
    # mail_link = page.locator('a[href*="mail.google.com/mail/"]')
    # # print(mail_link.get_attribute('href'))
    # expect(mail_link).to_have_attribute("href", "https://mail.google.com/mail/&ogbl")
    # # print(page.title())
    # input_field = page.locator ('[name="q"]')
    # print(input_field.get_attribute('aria-label'))
    # page.screenshot(path="screenshot.png")
    # # input_field.fill('cat')
    # search_button = page.locator('[name="btnK"]').nth(2)
    # search_button.wait_for(state='visible')
    # search_button.click()
    # expect(page).to_have_title(re.compile('cat'))
     # expect(page).to_have_title (re.compile('планете'))


