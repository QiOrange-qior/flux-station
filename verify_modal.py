import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1920, "height": 1080})
        await page.goto('file:///app/index.html')

        # Screenshot before clicking
        await page.screenshot(path='/tmp/before_click.png')

        # Click the button to open config
        await page.click('#open-config-btn')
        await page.wait_for_timeout(500) # wait for transition

        # Screenshot after clicking
        await page.screenshot(path='/tmp/after_click.png')

        await browser.close()

asyncio.run(main())
