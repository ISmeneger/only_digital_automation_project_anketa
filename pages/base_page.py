import logging


class BasePage:
    def __init__(self, driver, base_url):
        self.last_name_field = None
        self.driver = driver
        self.base_url = base_url

    def visit(self):
        return self.driver.get(self.base_url)

    # перейти по урлу
    def get_url(self):
        return self.driver.current_url

    # .current_url - получить текущий URL
    def equal_url(self) -> object:
        if self.get_url() == self.base_url:
            return True
        return False








