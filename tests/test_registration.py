import pytest
from selenium import webdriver

url = "localhost:8000"

@pytest.fixture
def browser(request):
    browser = webdriver.Firefox()
    request.addfinalizer(lambda: browser.quit())
    return browser

def test_can_see_homepage(browser):
    browser.get(url)
    assert 'Mailgenic' in browser.title

