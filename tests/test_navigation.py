# tests/test_navigation.py
from playwright.sync_api import Page, expect
from pages.home_page import HomePage


# Test 1: PROLAZI (Provera naslova)
def test_page_title_is_correct(page: Page):
    home_page = HomePage(page)
    home_page.navigate()

    # Assert (Provera)
    expect(page).to_have_title("Playwright: Fast and reliable end-to-end testing for modern web apps")


# Test 2: PADA (Da bi se generisao screenshot u izveštaju)
def test_non_existent_element_fails(page: Page):
    home_page = HomePage(page)
    home_page.navigate()

    # NAMERNO PADA: Provera nepostojećeg elementa
    # Kada ovaj test padne, Playwright će automatski snimiti screenshot
    expect(home_page.non_existent_locator).to_be_visible(timeout=5000)