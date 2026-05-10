"""Playwright tests that verify every local image loads correctly.
The suite iterates over all <img> tags whose src starts with "assets/" and checks:
  1. The network request returns HTTP 200 and an image MIME type.
  2. The browser decoded the image (naturalWidth > 0).
  3. The element is visible on the page (helps catch hidden placeholders).
"""

import re
from pathlib import Path
import pytest
from playwright.sync_api import expect

# The HomePage object gives us easy navigation.
from ..pages.home_page import HomePage

BASE_URL = "https://tapas100.github.io/arogyarasa-website/"

@pytest.fixture(scope="function")
def home(page):
    hp = HomePage(page)
    hp.navigate()
    # Ensure we are on the right page before proceeding.
    expect(page).to_have_url(re.compile(r"^" + re.escape(BASE_URL)))
    return hp

def test_all_local_images_load(page, home):
    # Grab all <img> elements that point to the assets folder.
    img_elements = page.query_selector_all('img[src^="assets/"]')
    assert img_elements, "No local images found on the page"

    for img in img_elements:
        src = img.get_attribute('src')
        # 1️⃣ Verify network response (status 200, image MIME)
        with page.expect_response(lambda resp: resp.url().endswith(src)) as resp_info:
            # Force the browser to request the image if it hasn't yet (lazy‑load cases).
            page.evaluate('el => el.scrollIntoView()', img)
        response = resp_info.value
        assert response.status == 200, f"{src} returned {response.status}"
        ct = response.headers.get('content-type', '')
        assert ct.startswith('image/'), f"{src} MIME type is not image (got {ct})"

        # 2️⃣ Verify the image decoded (naturalWidth > 0)
        natural_width = page.evaluate('el => el.naturalWidth', img)
        assert natural_width > 0, f"{src} failed to decode (naturalWidth=0)"

        # 3️⃣ Verify visibility – catches hidden placeholders.
        expect(img).to_be_visible()
