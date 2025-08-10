import asyncio
from playwright.async_api import async_playwright
import time

URL_EXPECTED = "https://www.eshopworld.com/shoppers/help/retailer/nike/terms-and-conditions-of-sale-en/"

async def run_test():
    for i in range(4):
        async with async_playwright() as p:
            browser = await p.chromium.launch(channel="chrome", headless=False)
            context = await browser.new_context()
            page = await context.new_page()

            await page.goto("https://www.nike.com/il")
            print(f"[{i+1}] Opened Nike IL site")
            time.sleep(5)

            try:
                await page.click('//*[@id="gen-nav-commerce-header-v2"]/nav/div[1]/div/div[2]/nav/ul/li[2]/a/p')
                print(f"[{i+1}] Clicked on dropdown menu")
                time.sleep(5)

                await page.click('//*[@id="gen-nav-commerce-header-v2"]/nav/div[1]/div/div[2]/nav/ul/li[2]/details/div/div/ul/li[6]/a')
                print(f"[{i+1}] Clicked on Terms of Sale")
                time.sleep(5)

                current_url = page.url
                if current_url == URL_EXPECTED:
                    print(f"[{i+1}] Terms of sale page loaded successfully")
                else:
                    print(f"[{i+1}] Terms of sale page loading error (Got: {current_url})")
                time.sleep(5)
            except Exception as e:
                print(f"[{i+1}] Error occurred: {e}")
            finally:
                await browser.close()

    print("Test end")

asyncio.run(run_test())
