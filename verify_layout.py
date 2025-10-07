import os
from pathlib import Path
from playwright.sync_api import sync_playwright, Page, expect

def test_report_layout(page: Page):
    """
    This test verifies that the main sections of the report are rendered.
    """
    # 1. Arrange: Go to the local index.html file.
    # The path needs to be absolute for the browser to open it.
    file_path = f"file://{Path('index.html').resolve()}"
    page.goto(file_path)

    # 2. Assert: Check for the presence of key sections.
    # We expect the hero section title to be visible.
    hero_title = page.get_by_role("heading", name="Отчёт о результатах внешней оценки Совета директоров компании {{название компании}}")
    expect(hero_title).to_be_visible()

    # We expect the table of contents to be visible.
    toc_title = page.get_by_role("heading", name="Содержание")
    expect(toc_title).to_be_visible()
    
    # We expect the footer to be visible.
    footer_copy = page.get_by_text("© Board AI")
    expect(footer_copy).to_be_visible()

    # 3. Screenshot: Capture the full page for visual verification.
    page.screenshot(path="jules-scratch/verification/verification.png", full_page=True)

# This is a wrapper to run the test function with Playwright.
# This setup is a bit more standard for Playwright tests.
def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            test_report_layout(page)
            print("Verification script ran successfully.")
        except Exception as e:
            print(f"An error occurred during verification: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    main()