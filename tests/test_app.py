from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time  # Importa time para pausas

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8081")  # Ajusta el puerto según npm start
    yield driver
    driver.quit()

def test_page_loads(driver):
    assert "Todo" in driver.title or "todo" in driver.title.lower()
@pytest.mark.skip(reason="Omitida temporalmente")
def test_add_todo(driver):
    #time.sleep(10)
    input_field = driver.find_element(By.CLASS_NAME, "new-todo")
    #breakpoint()  
    input_field.send_keys("Estudiar Jenkins")
    input_field.submit()
    todo_list = driver.find_element(By.CLASS_NAME, "todo-list")
    assert "Estudiar Jenkins" in todo_list.text
@pytest.mark.skip(reason="Omitida temporalmente")
def test_complete_todo(driver):
    input_field = driver.find_element(By.CLASS_NAME, "new-todo")
    input_field.send_keys("Hacer ejercicio")
    input_field.submit()
    checkbox = driver.find_element(By.CSS_SELECTOR, ".todo-list .toggle")
    checkbox.click()
    completed_todo = driver.find_element(By.CSS_SELECTOR, ".todo-list .completed")
    assert completed_todo is not None