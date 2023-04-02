from selenium.webdriver.common.by import By
import time


def test_petfriends(selenium):
    # Открывается главная страница сайта:
    selenium.get("https://petfriends.skillfactory.ru/")

    time.sleep(5)

    # клик по кнопке новый пользователь
    btn_newuser = selenium.find_element(By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]")

    btn_newuser.click()

    # клик по кнопке у меня уже есть аккаунт
    btn_exist_acc = selenium.find_element(By.LINK_TEXT, "У меня уже есть аккаунт")
    btn_exist_acc.click()

    # поиск поля email и ввод валидного значения
    field_email = selenium.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys("123bda@mail.ru")

    # поиск поля пароль и ввод валидного значения
    field_pass = selenium.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys("xiouojtb")

    # клик по кнопке подтвердить
    btn_submit = selenium.find_element(By.XPATH, "//button[@type='submit']")
    btn_submit.click()

    time.sleep(10)
    if selenium.current_url == 'https://petfriends.skillfactory.ru/all_pets':
        # Делаем скриншот
        selenium.save_screenshot('result_petfriends.png')
    else:
        raise Exception("login error")
