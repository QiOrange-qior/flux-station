from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_viewport_size({"width": 1280, "height": 720})
        page.goto('file://' + __import__('os').path.abspath('index.html'))

        # Switch to Vault view
        page.evaluate("switchView('vault')")
        page.wait_for_timeout(500)

        # Switch to History tab
        page.evaluate("switchVaultTab('history')")
        page.wait_for_timeout(500)

        page.screenshot(path='assets_history_view8.png')
        print("Saved screenshot to assets_history_view8.png")
        browser.close()

run()
