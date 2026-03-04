from playwright.sync_api import sync_playwright
import time

def test_frontend():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("file:///app/index.html")

        # Give animations time
        time.sleep(1)
        # Screenshot default (Generation View)
        page.screenshot(path="frontend_verification_gen.png", full_page=True)

        # Click Model Plaza
        page.click("#nav-plaza")
        time.sleep(1)
        page.screenshot(path="frontend_verification_plaza.png", full_page=True)

        # Click API
        page.click("#nav-api")
        time.sleep(1)
        page.screenshot(path="frontend_verification_api.png", full_page=True)

        browser.close()

if __name__ == "__main__":
    test_frontend()
