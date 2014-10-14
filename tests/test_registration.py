import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

url = "localhost:8000"

@pytest.fixture
def browser(request):
    browser = webdriver.Firefox()
    request.addfinalizer(lambda: browser.quit())
    return browser

def test_can_choose_domain(browser):
    browser.get(url)
    domain_input = browser.find_element_by_name("domain")
    assert domain_input

    tld_select = Select(browser.find_element_by_name("tld"))
    tld_options = [o.text for o in tld_select.options]
    assert ".me" in tld_options
    assert ".ch" in tld_options
    assert ".com" in tld_options

