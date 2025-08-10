

import time
from playwright.sync_api import sync_playwright

def run_test():
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir="/tmp/playwright",
            headless = False,
            permissions = ["geolocation"],
            geolocation = {"longitude": 34.9896, "latitude": 32.7940},
            locale = "en-US")

        page = context.new_page()

        for i in range(4):
            print(f"\nStarting iteration {i + 1}...")

            page.goto("https://www.nike.com/il", timeout=60000)
            page.wait_for_load_state("load")
            time.sleep(3)

            try:
                find_store_xpath = '//*[@id="gen-nav-commerce-header-v2"]/nav/div[1]/div/div[2]/nav/ul/li[1]/a/p'
                page.locator(find_store_xpath).click()
                time.sleep(3)
            except Exception as e:
                print(f"Error clicking 'Find a Store': {e}")
                continue

            try:
                location_input_xpath = '//*[@id="ta-Location_input"]'
                page.wait_for_selector(location_input_xpath, timeout=10000)
                page.locator(location_input_xpath).fill("Haifa, Israel")
                time.sleep(3)
            except Exception as e:
                print(f"Error entering location: {e}")
                continue

            time.sleep(5)

            time.sleep(5)

            try:
                result_text_xpath = '//*[@id="store-locator"]/article/div/section[1]/div[2]/p'
                page.wait_for_selector(result_text_xpath, timeout=10000)
                result_text = page.locator(result_text_xpath).inner_text()
                print(f"Iteration {i + 1}: {result_text}")
                time.sleep(3)
            except Exception as e:
                print(f"Error reading store count: {e}")
                continue

            page.goto("https://www.nike.com/il", timeout=60000)
            time.sleep(3)

        context.close()
        print("\nTest end")

if __name__ == "__main__":
    run_test()
