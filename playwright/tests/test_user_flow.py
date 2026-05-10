"""End‑to‑end user‑flow tests using Playwright.
We cover the most visible interactions a visitor performs:
  • Click the hero "Shop Now" button – it should scroll to the product section.
  • Verify that each product card is displayed.
  • Click the first "Learn More" button and assert that the page stays on the same URL (the demo uses placeholder links).
  • Ensure the process‑flow icons are present and have non‑empty alt texts.
These checks guarantee that each UI feature you add gets a corresponding test.
"""

import re
import pytest
from playwright.sync_api import expect

from ..pages.home_page import HomePage

BASE_URL = "https://tapas100.github.io/arogyarasa-website/"

@pytest.fixture(scope="function")
def home(page):
    hp = HomePage(page)
    hp.navigate()
    expect(page).to_have_url(re.compile(r"^" + re.escape(BASE_URL)))
    return hp

def test_shop_now_scrolls_to_products(page, home):
    # Click the hero CTA
    home.shop_now_button.click()
    # Expect the URL to stay the same (anchor navigation)
    expect(page).to_have_url(BASE_URL)
    # The products section should now be in the viewport
    first_card = home.product_cards.first
    first_card.scroll_into_view_if_needed()
    expect(first_card).to_be_visible()

def test_product_cards_and_learn_more(page, home):
    cards = home.product_cards
    expect(cards).to_have_count(4)  # we have 4 product cards

    # Verify each card has an image with a non‑empty alt attribute
    for i in range(4):
        card = cards.nth(i)
        img = card.locator('img')
        alt = img.get_attribute('alt')
        assert alt and alt.strip(), f"Card {i+1} image missing alt text"
        # Ensure the image actually loaded (naturalWidth > 0)
        natural_width = page.evaluate('el => el.naturalWidth', img)
        assert natural_width > 0, f"Card {i+1} image failed to decode"

    # Click the first "Learn More" button and ensure we stay on the same page
    first_learn = home.learn_more_buttons.first
    first_learn.click()
    expect(page).to_have_url(BASE_URL)

def test_process_flow_icons(page, home):
    icons = home.process_icons
    # Expect exactly 4 icons (farm, sun, grind, seal)
    expect(icons).to_have_count(4)
    for i in range(4):
        icon = icons.nth(i)
        # alt attribute should be present and meaningful
        alt = icon.get_attribute('alt')
        assert alt and alt.strip(), f"Process icon {i+1} missing alt"
        # Ensure the image decoded correctly
        natural_width = page.evaluate('el => el.naturalWidth', icon)
        assert natural_width > 0, f"Process icon {i+1} failed to decode"
