from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
import pytest
from selenium.webdriver.common.keys import Keys
from tests.pages.todo_app_page import TodoAppPage

@pytest.fixture
def driver():
    # Uso webdriver-manager para instalar y configurar ChromeDriver automáticamente
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("http://localhost:8081")
    yield driver
    driver.quit()
    
@pytest.fixture
def todo_page(driver):
    return TodoAppPage(driver)
    
def test_page_loads(driver):
    assert "Todo" in driver.title or "todo" in driver.title.lower()
    
def test_add_todo(todo_page):
    todo_page.add_to_do("Estudiar Jenkins")  
    text_todo_list = todo_page.get_todo_list()
    assert "Estudiar Jenkins" in text_todo_list
    
def test_complete_todo(todo_page):
    todo_page.add_to_do("Hacer ejercicios")  
    todo_page.checkbox_click()
    completed_todo_id = todo_page.get_completed_todo_by_id(1)
    assert completed_todo_id is not None

