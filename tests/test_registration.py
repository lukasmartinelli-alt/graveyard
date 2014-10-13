import pytest
from selenium import webdriver

url = "localhost:8000"

@pytest.fixture
def browser(request):
    browser = webdriver.Firefox()
    request.addfinalizer(lambda: browser.quit())
    return browser

def test_can_register(browser):
    browser.get(url)
    login_link = browser.find_element_by_link_text("Login")
    assert login_link
    login_link.click()
    assert "Registration" in browser.title
    #Now we should see the login and see that we have to reister

