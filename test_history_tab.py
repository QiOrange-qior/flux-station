import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1280, "height": 720})
        await page.goto("http://localhost:8000")

        # Call switchView directly with the correct argument
        await page.evaluate("switchView('vault')")
        await page.wait_for_timeout(1000)

        # Click the History tab
        await page.evaluate("switchVaultTab('history')")
        await page.wait_for_timeout(1000)

        await page.screenshot(path="assets_history_view7.png")
        await browser.close()

asyncio.run(main())
