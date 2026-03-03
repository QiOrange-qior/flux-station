import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1920, "height": 1080})
        await page.goto('file:///app/index.html')
        await page.screenshot(path='/tmp/verify_modal.png')
        await browser.close()

asyncio.run(main())
