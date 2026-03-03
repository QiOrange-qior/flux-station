from playwright.sync_api import sync_playwright

def test_frontend():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("file:///app/index.html")
        page.wait_for_selector(".masonry-item-models")
        page.screenshot(path="frontend_verification.png", full_page=True)
        browser.close()

if __name__ == "__main__":
    test_frontend()
