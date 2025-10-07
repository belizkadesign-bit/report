import os
from pathlib import Path
from playwright.sync_api import sync_playwright, Page, expect

def test_final_report_layout(page: Page):
    """
    This test verifies that the entire report page, including all detailed
    sections and interactive elements, renders correctly.
    """
    # 1. Arrange: Go to the local index.html file.
    file_path = f"file://{Path('index.html').resolve()}"
    page.goto(file_path)

    # 2. Assert: Check for the presence of key section titles.
    expect(page.get_by_role("heading", name="Миссия и приоритеты Совета директоров")).to_be_visible()
    expect(page.get_by_role("heading", name="Состав и компетенции Совета директоров")).to_be_visible()
    expect(page.get_by_role("heading", name="Процесс и динамика работы Совета директоров")).to_be_visible()
    expect(page.get_by_role("heading", name="Комитеты Совета директоров")).to_be_visible()
    expect(page.get_by_role("heading", name="Председатель и Корпоративный секретарь")).to_be_visible()
    expect(page.get_by_role("heading", name="Приложение 2. Бенчмаркинг состава и компетенций Совета директоров")).to_be_visible()

    # Scroll to the bottom to ensure all animations are triggered and the layout is stable.
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    # Wait for animations to complete.
    page.wait_for_timeout(1000)

    # 3. Screenshot: Capture the full page for final visual verification.
    page.screenshot(path="jules-scratch/verification/final_verification.png", full_page=True)

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            test_final_report_layout(page)
            print("Final verification script ran successfully.")
        except Exception as e:
            print(f"An error occurred during final verification: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    main()