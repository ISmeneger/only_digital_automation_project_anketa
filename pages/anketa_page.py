from pages.base_page import BasePage
from components.components import WebElement

class AnketaPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://only.digital/projects#brief'
        super().__init__(driver, self.base_url)

        self.name_field = WebElement(driver, 'form > div:nth-child(1) > div > div:nth-child(1) > div > input')

        self.e_mail_field = WebElement(driver, 'form > div:nth-child(1) > div > div:nth-child(2) > div > input')
        self.phone_field = WebElement(driver, 'form > div:nth-child(1) > div > div:nth-child(3) > div > div.iti.iti--allow-dropdown.iti--separate-dial-code.iti--show-flags > input')
        self.company_field = WebElement(driver, 'form > div:nth-child(1) > div > div:nth-child(4) > div > input')
        self.sait_radio_button = WebElement(driver, 'form > div:nth-child(2) > div.sc-60972c5f-6.iVzsq > label:nth-child(2) > span')
        self.textarea_field = WebElement(driver, 'form > div:nth-child(2) > div.sc-30c137f2-0.ktozux > textarea')
        self.upload_file_field = WebElement(driver, "//input[@type='file']", 'xpath')
        self.bolee_20_mln_radio_button = WebElement(driver, 'form > div:nth-child(3) > div > label:nth-child(6) > span')
        self.socseti_radio_button = WebElement(driver, 'form > div:nth-child(4) > div > label:nth-child(3) > span')
        self.button_send = WebElement((driver, "form > div.sc-22c64804-0.lgfktX > button > span"))



