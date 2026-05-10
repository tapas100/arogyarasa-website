import os
from pathlib import Path

BASE_URL = os.getenv('BASE_URL', 'https://tapas100.github.io/arogyarasa-website/')

# Playwright test configuration (Python style)
# This file is loaded by the pytest‑playwright plugin.
# It defines a shared ``page`` fixture and global settings.

# The pytest‑playwright plugin automatically reads ``playwright.config.py``
# if present in the project root (or any sub‑folder).  The settings below are
# kept minimal – we let each test decide whether to run headless or headed.

def pytest_configure(config):
    config.base_url = BASE_URL


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", default=True,
                     help="Run browsers in headless mode (default: true)")


def pytest_fixture_setup(fixturedef, request):
    if fixturedef.argname == "page":
        headless = request.config.getoption("--headless")
        from playwright.sync_api import sync_playwright
        playwright = sync_playwright().start()
        browser = playwright.chromium.launch(headless=headless)
        context = browser.new_context(viewport={"width": 1280, "height": 800})
        page = context.new_page()
        request.node._playwright = playwright
        request.node._browser = browser
        request.node._context = context
        return page

def pytest_fixture_post_finalizer(fixturedef, request):
    if fixturedef.argname == "page":
        request.node._context.close()
        request.node._browser.close()
        request.node._playwright.stop()
