# tests/test_navigation.py
from playwright.sync_api import Page, expect
from pages.home_page import HomePage


# Test 1: Proverava naslov stranice
def test_page_title_is_correct(page: Page):
    home_page = HomePage(page)
    home_page.navigate()

    # ISPRAVNA ASERCIJA: Očekivana vrednost koja je tačna
    expected_title = "Fast and reliable end-to-end testing for modern web apps | Playwright Python"
    expect(page).to_have_title(expected_title)


# Test 2: Testira navigaciju na docs stranicu
def test_navigate_to_docs_and_verify_heading(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.click_get_started()

    # ASERCIJA: Provera da li je naslov 'Installation' vidljiv
    expect(home_page.docs_heading).to_be_visible()