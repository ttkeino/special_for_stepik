import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Поиск элемента и проверка его наличия на странице
def test_guest_should_see_button_add(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    try:
        btn_add_to_bascket = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn-add-to-basket"))
        )
        assert len(btn_add_to_bascket.text) > 0, "Кнопка не найдена"
    finally:
        time.sleep(5)
        browser.quit()
