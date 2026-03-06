import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        # open local index.html
        await page.goto('file:///app/index.html')

        # Click on Assets (Vault) tab
        await page.evaluate("""() => {
            const vaultBtn = Array.from(document.querySelectorAll('a')).find(el => el.textContent.includes('资产'));
            if (vaultBtn) vaultBtn.click();
        }""")

        # Wait a bit for transition
        await page.wait_for_timeout(1000)

        # Take screenshot
        await page.screenshot(path='vault_history.png')
        await browser.close()

asyncio.run(main())
