from pages.base_page import BasePage
from components.components import WebElement

class AnketaPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://only.digital/projects#brief'
        super().__init__(driver, self.base_url)

        self.name_field = WebElement(driver, 'div:nth-child(1) > div > div:nth-child(1) > div > input')

        self.e_mail_field = WebElement(driver, 'div:nth-child(2) > div > input')
        self.phone_field = WebElement(driver, 'div.iti.iti--allow-dropdown.iti--separate-dial-code.iti--show-flags > input')
        self.company_field = WebElement(driver, 'div:nth-child(4) > div > input')
        self.complex_of_works_checkbox_button = WebElement(driver, 'div:nth-child(2) > div.sc-60972c5f-6.iVzsq > label:nth-child(1)')
        self.sait_checkbox_button = WebElement(driver, 'div:nth-child(2) > div.sc-60972c5f-6.iVzsq > label:nth-child(2)')
        self.service_checkbox_button = WebElement(driver, 'div:nth-child(2) > div.sc-60972c5f-6.iVzsq > label:nth-child(3)')
        self.design_checkbox_button = WebElement(driver, 'div:nth-child(2) > div.sc-60972c5f-6.iVzsq > label:nth-child(4)')
        self.ux_audit_checkbox_button = WebElement(driver, 'div:nth-child(2) > div.sc-60972c5f-6.iVzsq > label:nth-child(5)')
        self.branding_checkbox_button = WebElement(driver, 'div:nth-child(2) > div.sc-60972c5f-6.iVzsq > label:nth-child(6)')
        self.textarea_field = WebElement(driver, 'div.sc-30c137f2-0.ktozux > textarea')
        self.upload_file_field = WebElement(driver, "//input[@type='file']", 'xpath')
        self.menee_2_mln_radio_button = WebElement(driver, 'div:nth-child(3) > div > label:nth-child(1)')
        self.two_3_mln_radio_button = WebElement(driver, 'div:nth-child(3) > div > label:nth-child(2)')
        self.three_5_mln_radio_button = WebElement(driver, 'div:nth-child(3) > div > label:nth-child(3)')
        self.five_10_mln_radio_button = WebElement(driver, 'div:nth-child(3) > div > label:nth-child(4)')
        self.ten_20_mln_radio_button = WebElement(driver, 'div:nth-child(3) > div > label:nth-child(5)')
        self.bolee_20_mln_radio_button = WebElement(driver, 'div:nth-child(3) > div > label:nth-child(6)')
        self.ratings_radio_button = WebElement(driver, 'div:nth-child(4) > div > label:nth-child(1)')
        self.copyright_on_the_website_radio_button = WebElement(driver, 'div:nth-child(4) > div > label:nth-child(2)')
        self.socseti_radio_button = WebElement(driver, 'div:nth-child(4) > div > label:nth-child(3)')
        self.recommendations_radio_button = WebElement(driver, 'div:nth-child(4) > div > label:nth-child(4)')
        self.known_for_a_long_time = WebElement(driver, 'div:nth-child(4) > div > label:nth-child(5)')
        self.button_send = WebElement((driver, 'div.sc-22c64804-0.lgfktX > button > span'))



