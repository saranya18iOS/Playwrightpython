import pytest
from playwright.sync_api import sync_playwright

from utils.config import CONFIG


@pytest.fixture(scope="session")
def app():
    from utils.api_client import APIClient

    with sync_playwright() as p:

        # Launch browser
        browser = p.chromium.launch(headless=CONFIG["headless"])

        # API context
        api_context = p.request.new_context(
            base_url=CONFIG["api_url"],
            extra_http_headers={"Content-Type": "application/json"}
        )

        yield {
            "browser": browser,
            "api_context": api_context,
            "APIClient": APIClient
        }

        # Cleanup
        browser.close()
        api_context.dispose()


@pytest.fixture(scope="session")
def api_client(app):
    return app["APIClient"](app["api_context"])


@pytest.fixture
def page(app):
    context = app["browser"].new_context()
    page = context.new_page()

    yield page

    context.close()