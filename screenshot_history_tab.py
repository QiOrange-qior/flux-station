import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        page.set_viewport_size({"width": 1280, "height": 720})
        await page.goto("http://localhost:8000")

        # Click on Assets / Vault in sidebar
        await page.evaluate("""() => {
            const tabs = document.querySelectorAll('aside nav button');
            for (let t of tabs) {
                if (t.innerText.includes('资产') || t.innerText.includes('Vault')) {
                    t.click();
                    break;
                }
            }
        }""")
        await page.wait_for_timeout(1000)

        # Click on History tab in Vault
        await page.evaluate("switchVaultTab('history')")
        await page.wait_for_timeout(1000)

        await page.screenshot(path="vault_history_content.png")
        await browser.close()

asyncio.run(main())
