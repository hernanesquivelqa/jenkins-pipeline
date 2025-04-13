from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
import pytest
import time
from selenium.webdriver.common.keys import Keys
@pytest.fixture
def driver():
    # Uso webdriver-manager para instalar y configurar ChromeDriver automáticamente
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("http://localhost:8081")
    yield driver
    driver.quit()
    
def test_page_loads(driver):
    assert "Todo" in driver.title or "todo" in driver.title.lower()
def test_add_todo(driver):
    #time.sleep(3)
    input_field = driver.find_element(By.CLASS_NAME, "new-todo")
    #breakpoint()  
    input_field.send_keys("Estudiar Jenkins")
    input_field.send_keys(Keys.RETURN)
    todo_list = driver.find_element(By.CLASS_NAME, "todo-list")
    assert "Estudiar Jenkins" in todo_list.text

def test_complete_todo(driver):
    input_field = driver.find_element(By.CLASS_NAME, "new-todo")
    input_field.send_keys("Hacer ejercicio")
    input_field.send_keys(Keys.RETURN)
    checkbox = driver.find_element(By.CSS_SELECTOR, ".todo-list .toggle")
    checkbox.click()
    completed_todo = driver.find_element(By.CSS_SELECTOR, ".todo-list .completed")
    assert completed_todo is not None