# pages/home_page.py
from playwright.sync_api import Page, Locator


class HomePage:
    # 1. Definicija URL-a
    URL = "https://playwright.dev/python"

    # 2. Inicijalizacija i lokatori
    def __init__(self, page: Page):
        self.page = page
        self.get_started_link: Locator = page.get_by_role("link", name="Get started")
        self.docs_heading: Locator = page.get_by_role("heading", name="Installation")
        self.non_existent_locator: Locator = page.locator("#neki-nepostojeci-element")  # Za testiranje fail-a

    # 3. Akcione metode
    def navigate(self):
        """Navigira do Playwright Python početne stranice."""
        self.page.goto(self.URL)

    def click_get_started(self):
        """Klikne na dugme 'Get started'."""
        self.get_started_link.click()