from pages.placeholder_text import PlaceholderText


def test_placeholder(browser):
    """Проверка значения атрибута элемента"""

    placeholder_text = PlaceholderText(browser)

    placeholder_text.visit()

    assert browser.title == 'Портфолио Only digital. Разработали 60+ проектов'
    assert placeholder_text.name.get_dom_attribute('placeholder') == 'Имя*'
    assert placeholder_text.email.get_dom_attribute('placeholder') == 'E-mail*'
    assert placeholder_text.phone.get_dom_attribute('placeholder') == 'Телефон'
    assert placeholder_text.company.get_dom_attribute('placeholder') == 'Компания'
    assert placeholder_text.description.get_dom_attribute('placeholder') == 'Расскажите о вашем проекте'