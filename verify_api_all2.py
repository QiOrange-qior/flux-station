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

        # Test Volcengine save to ensure it works
        page.click("#api-display-volcengine button:has-text('添加密钥')")
        time.sleep(0.5)

        page.fill("#api-input-volcengine", "sk-volc-mock-key")
        page.click("#api-edit-volcengine button:has-text('保存')")
        time.sleep(0.5)

        # Screenshot saved state
        page.screenshot(path="frontend_verification_api_all.png", full_page=True)

        browser.close()

if __name__ == "__main__":
    test_frontend()
