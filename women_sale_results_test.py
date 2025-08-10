from playwright.sync_api import sync_playwright
import time

def run_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.nike.com/il")

        page.click('a[href="https://www.nike.com/il/women"]')

        time.sleep(3)

        page.click('a[href="https://www.nike.com/il/w/womens-sale-3yaepz5e1x6"]')

        time.sleep(3)

        try:
            result = page.locator('xpath=//*[@id="Women\'s-Sale"]/span').inner_text()
            print(f"Results in Sale category for women: {result}")
        except Exception as e:
            print("Could not locate results element:", e)
        browser.close()

for i in range(3):
    print(f"\n--- Running iteration {i+1} ---")
    run_test()

print("\nTest end")
