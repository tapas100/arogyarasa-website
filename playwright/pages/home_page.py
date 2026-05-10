"""Page‑object model for the Arogyarasa home page.

All selectors are deliberately generic so they survive minor HTML tweaks.
If you add new sections, simply extend this class with new properties.
"""

from playwright.sync_api import Page, Locator

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "/"

    # ---------------------------------------------------------------------
    # Core sections
    # ---------------------------------------------------------------------
    @property
    def hero_section(self) -> Locator:
        return self.page.locator('header[style*="background-image"]')

    @property
    def shop_now_button(self) -> Locator:
        return self.page.locator("a:has-text('Shop Now')")

    @property
    def product_cards(self) -> Locator:
        return self.page.locator("section#products article")

    def product_card_by_title(self, title: str) -> Locator:
        """Return the card that contains a given product title."""
        return self.page.locator(f"section#products article >> h3:has-text('{title}')").first

    @property
    def learn_more_buttons(self) -> Locator:
        return self.page.locator("section#products article a:has-text('Learn More')")

    # ---------------------------------------------------------------------
    # Process‑flow icons (farm, sun, grind, seal)
    # ---------------------------------------------------------------------
    @property
    def process_icons(self) -> Locator:
        return self.page.locator("section#process img")

    # ---------------------------------------------------------------------
    # Utilities
    # ---------------------------------------------------------------------
    def navigate(self):
        """Open the home page using the base URL from the pytest config."""
        base = getattr(self.page.context, "base_url", None) or "https://tapas100.github.io/arogyarasa-website/"
        self.page.goto(base)
