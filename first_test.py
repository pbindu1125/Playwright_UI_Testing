from playwright.sync_api import sync_playwright

def run():
    """
    Launches a Chromium browser using Playwright, navigates to Google's homepage, prints the page title, and closes the browser.

    This function uses the synchronous Playwright API to automate browser actions for demonstration or testing purposes.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.google.com")
        print("Page Title: ", page.title())
        browser.close()

if __name__ == "__main__":
    run()