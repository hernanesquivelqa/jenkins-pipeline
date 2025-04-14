from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class TodoAppPage:
    def __init__(self, driver: WebDriver):
        self.web = driver
        self.input_locator = (By.CLASS_NAME, "new-todo")
        self.todo_list_locator = (By.CLASS_NAME, "todo-list")
        self.checkbox_locator = (By.CSS_SELECTOR, ".todo-list .toggle")
        self.completed_locator = (By.CSS_SELECTOR, ".todo-list .completed")
        self.checkbox = (By.CSS_SELECTOR, ".todo-list .toggle")
        self.completed_todo = (By.CSS_SELECTOR, ".todo-list .completed")


    def get_input_field(self):
        return self.web.find_element(*self.input_locator) 

    def get_todo_list(self):
        todo_list = self.web.find_element(*self.todo_list_locator)
        return todo_list.text
    def add_to_do(self,text):
        input_field = self.get_input_field()
        input_field.send_keys(text)
        input_field.send_keys(Keys.RETURN)
        
    def checkbox_click(self):
        checkbox = self.web.find_element(*self.checkbox)
        checkbox.click()
    
    def get_completed_todo_by_id(self, todo_id: int):
        locator = (By.CSS_SELECTOR, f'li[data-id="{todo_id}"] .toggle')
        return self.web.find_element(*locator)
