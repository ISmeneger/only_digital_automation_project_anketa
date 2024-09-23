import time
import os
from pages.anketa_page import AnketaPage


def test_anketa_page(browser):
    anketa_page = AnketaPage(browser)

    anketa_page.visit()
    name = 'Ivan'
    e_mail_field = 'test@yandex.ru'
    phone_field = '9111111111'
    company_field = 'EnergoTech Company'
    textarea_field = 'EnergoTech Company - мы занимаемся продажей высокотехнологичного энергетического оборудования'


    anketa_page.name_field.send_keys(name)
    time.sleep(2)

    anketa_page.e_mail_field.send_keys(e_mail_field)
    time.sleep(2)

    anketa_page.phone_field.click()
    anketa_page.phone_field.send_keys(phone_field)
    time.sleep(2)
    anketa_page.company_field.send_keys(company_field)
    time.sleep(2)

    anketa_page.complex_of_works_radio_button.click()
    time.sleep(2)

    anketa_page.sait_radio_button.click()
    time.sleep(2)

    anketa_page.service_radio_button.click()
    time.sleep(2)

    anketa_page.design_radio_button.click()
    time.sleep(2)

    anketa_page.ux_audit_radio_button.click()
    time.sleep(2)

    anketa_page.branding_radio_button.click()
    time.sleep(2)

    anketa_page.textarea_field.send_keys(textarea_field)
    time.sleep(2)

    anketa_page.upload_file_field.send_keys(f'{os.getcwd()}\\downloads\\STE In Banner.jpg')
    time.sleep(4)

    anketa_page.menee_2_mln_radio_button.click()
    time.sleep(2)

    anketa_page.two_3_mln_radio_button.click()
    time.sleep(2)

    anketa_page.three_5_mln_radio_button.click()
    time.sleep(2)

    anketa_page.five_10_mln_radio_button.click()
    time.sleep(2)

    anketa_page.ten_20_mln_radio_button.click()
    time.sleep(2)

    anketa_page.bolee_20_mln_radio_button.click()
    time.sleep(2)

    anketa_page.ratings_radio_button.click()
    time.sleep(2)

    anketa_page.copyright_on_the_website_radio_button.click()
    time.sleep(2)

    anketa_page.socseti_radio_button.click()
    time.sleep(2)

    anketa_page.recommendations_radio_button.click()
    time.sleep(2)

    anketa_page.known_for_a_long_time.click()
    time.sleep(2)


    # Рекапчу на тестовых стендах всегда отключают, поэтому ее автоматизировать не нужно.

#     Если поставить рекапчу в ручную, то можно нажать на кнопку "Отправить"

    # anketa_page.button_send.click()
    # time.sleep(2)


