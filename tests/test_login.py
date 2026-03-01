import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

# def test_login_ui_elements(page: Page):
#     login_pg = LoginPage(page)
#     login_pg.navigate()

#     # UI Integrity Checks
#     expect(page).to_have_title("Login | My App")
#     expect(login_pg._username).to_be_visible()
#     expect(login_pg._password).to_be_visible()
#     expect(login_pg._login_btn).to_be_enabled()

def test_successful_login(page: Page):
    login_pg = LoginPage(page)
    login_pg.navigate()

    # Functional Flow
    login_pg.login("student", "Password123")
    
    # Assert redirection to dashboard
    expect(page).to_have_url("https://practicetestautomation.com/logged-in-successfully/")
    expect(page.get_by_role("heading", name="Logged In Successfully")).to_be_visible()

# def test_failed_login_shows_error(page: Page):
#     login_pg = LoginPage(page)
#     login_pg.navigate()

#     login_pg.login("wrong_user", "wrong_pass")
    
#     # Assert error message appears
#     expect(login_pg._error_message).to_be_visible()
#     expect(login_pg._error_message).to_contain_text("Invalid credentials")