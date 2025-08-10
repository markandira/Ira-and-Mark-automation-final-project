from playwright.sync_api import sync_playwright
import time

def perform_test(playwright, test_number):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    def wait_for_element(selector, max_attempts=10, timeout=5000):
        attempts = 0
        while attempts < max_attempts:
            try:
                page.wait_for_selector(selector, state="visible", timeout=timeout)
                return True
            except Exception:
                attempts += 1
                print(f"Attempt {attempts} failed to find {selector}, retrying...")
                time.sleep(1)
        return False

    try:
        page.goto("https://www.nike.com/il")

        if not wait_for_element("text=MEN"):
            print(f"Test number {test_number}: 'MEN' category not found.")
            return
        page.click("text=MEN")

        shoes_selector = '[data-analytics-action-id="c098f50f-3b4e-4455-9b11-bed5349057c2"]'
        if not wait_for_element(shoes_selector):
            print(f"Test number {test_number}: 'Shoes' category inside 'MEN' not found using the data-analytics-action-id.")
            return
        page.click(shoes_selector)

        xpath_selector = '//*[@id="left-nav"]/nav/div[1]/div/div/a[2]'
        if not wait_for_element(xpath_selector):
            print(f"Test number {test_number}: Element with XPath {xpath_selector} not found.")
            return
        page.click(xpath_selector)

        if not wait_for_element('button[aria-label="Sort By"]'):
            print(f"Test number {test_number}: 'Sort By' filter button not found.")
            return
        page.click('button[aria-label="Sort By"]')

        if not wait_for_element('//*[@id="sort-options"]/button[4]'):
            print(f"Test number {test_number}: 'Price Low-High' option not found.")
            return
        page.click('//*[@id="sort-options"]/button[4]')

        time.sleep(4)

        first_item_image_selector = 'img.product-card__hero-image'
        if not wait_for_element(first_item_image_selector):
            print(f"Test number {test_number}: First product image not found.")
            return

        page.click(first_item_image_selector)

        time.sleep(5)


        price_selector = '[data-testid="currentPrice-container"]'
        if not wait_for_element(price_selector):
            print(f"Test number {test_number}: Price element not found.")
            return

        price = page.query_selector(price_selector).inner_text()
        print(f"Test number {test_number}: Price of the product is {price}")

        page.close()

    except Exception as e:
        print(f"Error during test number {test_number}: {str(e)}")
    finally:
        browser.close()


def main():
    with sync_playwright() as playwright:
        for i in range(1, 6):
            perform_test(playwright, i)
            print(f"Test number {i} completed")
            time.sleep(1)  # Optional delay between repetitions

        print("Total test end")


if __name__ == "__main__":
    main()