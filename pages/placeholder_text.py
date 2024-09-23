from pages.base_page import BasePage
from components.components import WebElement

class PlaceholderText(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://only.digital/projects#brief'
        super().__init__(driver, self.base_url)

        self.name = WebElement(driver, 'div:nth-child(1) > div > div:nth-child(1) > div > input')
        self.email = WebElement(driver, 'div:nth-child(2) > div > input')
        self.phone = WebElement(driver, 'div.iti.iti--allow-dropdown.iti--separate-dial-code.iti--show-flags > input')
        self.company = WebElement(driver, 'div:nth-child(4) > div > input')
        self.description = WebElement(driver, 'div.sc-30c137f2-0.ktozux > textarea')

