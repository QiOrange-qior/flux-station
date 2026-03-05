from playwright.sync_api import sync_playwright
import time

def test_frontend():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("file:///app/index.html")

        # Give animations time
        time.sleep(1)

        # Click API Settings
        page.click("#nav-api")
        time.sleep(1)

        # Click add key on Google
        page.click("button:has-text('添加密钥')")
        time.sleep(0.5)

        # Screenshot edit state
        page.screenshot(path="frontend_verification_api_edit.png", full_page=True)

        # Fill input and save
        page.fill("#api-input-google", "sk-google-mock-key-xyz123")
        page.click("button:has-text('保存')")
        time.sleep(0.5)

        # Screenshot saved state
        page.screenshot(path="frontend_verification_api_saved.png", full_page=True)

        browser.close()

if __name__ == "__main__":
    test_frontend()
