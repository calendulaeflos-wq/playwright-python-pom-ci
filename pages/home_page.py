# pages/home_page.py
from playwright.sync_api import Page, Locator


class HomePage:
    URL = "https://playwright.dev/python"
    url="u"

    def __init__(self, page: Page):
        self.page = page

        # Lokatori
        self.get_started_link: Locator = page.get_by_role("link", name="Get started")
        self.docs_heading: Locator = page.get_by_role("heading", name="Installation")

    # Akcione metode
    def navigate(self):
        """Navigira do Playwright Python početne stranice."""
        self.page.goto(self.URL)

    def click_get_started(self):
        """Klikne na link 'Get started'."""
        self.get_started_link.click()
        print("all done!")