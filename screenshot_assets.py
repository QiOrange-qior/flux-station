import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1280, "height": 720})
        await page.goto("http://localhost:8000")

        # Click the "资产" (Assets) menu item
        await page.evaluate("switchView('vault-view', document.querySelectorAll('aside nav a')[4])")
        await page.wait_for_timeout(500)

        await page.screenshot(path="assets_history_view2.png")
        await browser.close()

asyncio.run(main())
