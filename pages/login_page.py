from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.uname = page.get_by_role("textbox", name="Username")
        self.passwd = page.get_by_role("textbox", name="Password")
        self.button = page.get_by_role("button", name="Submit")
        

    def navigate(self):
        self.page.goto("https://practicetestautomation.com/practice-test-login/")

    def login(self, user, pwd):
        self.uname.fill(user)
        self.passwd.fill(pwd)
        self.button.click()