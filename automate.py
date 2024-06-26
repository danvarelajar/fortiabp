import click
import time
import random
from selenium import webdriver
#  from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#
@click.command()
@click.option("--url_login", "urllogin", type=str, required=True)
@click.option("--username_id", "username_id", type=str, required=True)
@click.option("--error_class", "errorfield", type=str, required=True)
def automate(urllogin, username_id, errorfield):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--password-store=basic')
    options.add_experimental_option("prefs",
                                    {
                                        "credentials_enable_service": False,
                                        "profile.password.manager_enabled": False
                                    })
    driver = webdriver.Chrome(options=options)
    #  action = ActionChains(driver)
    driver.get(urllogin)
    username = "johndoe@fortinet.demo"
    password = "password1"
    driver.implicitly_wait(0.5)
    time.sleep(3)
    driver.find_element(By.ID, username_id).click()
    active_element = driver.switch_to.active_element
    for letter in username:
        active_element.send_keys(letter)
        time.sleep(random.uniform(0, 0.5))

    time.sleep(1)
    active_element.send_keys(Keys.TAB)
    active_element = driver.switch_to.active_element
    for letter in password:
        active_element.send_keys(letter)
        time.sleep(random.uniform(0, 0.5))

    active_element.send_keys(Keys.ENTER)
    #  Check content after send credentials
    time.sleep(2)
    if driver.find_elements(By.CLASS_NAME, errorfield):
        print("Login Failed")

    time.sleep(7)
    driver.quit()


if __name__ == "__main__":
    automate()
