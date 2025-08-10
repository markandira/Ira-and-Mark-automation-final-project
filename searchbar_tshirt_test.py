import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, channel="chrome")
        context = await browser.new_context()
        page = await context.new_page()

        for i in range(4):
            print(f"\n--- Test interation {i + 1} ---")

            await page.goto("https://www.nike.com/il/")

            await page.wait_for_timeout(5000)

            await page.wait_for_selector('input#gn-search-input')

            await page.click('input#gn-search-input')

            await page.fill('input#gn-search-input', 't shirts for men')

            await page.keyboard.press('Enter')

            await page.wait_for_selector('.wall-header__item_count', timeout=10000)

            result_count = await page.inner_text('.wall-header__item_count')

            print("Page loaded as expected")
            print(f"Number of results: {result_count}")

            await page.wait_for_timeout(3000)

        await browser.close()

asyncio.run(run())
