from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

class WebElement:

    def __init__(self, driver, locator='', locator_type='css'):
        self.driver = driver
        self.locator = locator
        self.locator_type = locator_type

    # Метод для поиска элемента
    def find_element(self):
        return self.driver.find_element(self.get_by_type(), self.locator)

    # Метод, позволяющий кликнуть на элемент
    def click(self):
        self.find_element().click()

    # Метод для ввода текста
    def send_keys(self, text: str):
        self.find_element().send_keys(text)

     # Метод, который возвращает значение атрибутов с заданным именем
    def get_dom_attribute(self, name: str):
        value = self.find_element().get_dom_attribute(name)

        if value is None:
            return False
        if len(value) > 0:
            return value
        return True

    # Метод для работы с любым типом локатора
    def get_by_type(self):
        if self.locator_type == 'id':
            return By.ID
        elif self.locator_type == 'name':
            return By.NAME
        elif self.locator_type == 'xpath':
            return By.XPATH
        elif self.locator_type == 'css':
            return By.CSS_SELECTOR
        elif self.locator_type == 'class':
            return By.CLASS_NAME
        elif self.locator_type == 'link':
            return By.LINK_TEXT
        else:
            print('Locator type ' + self.locator_type + ' not correct')
        return False
