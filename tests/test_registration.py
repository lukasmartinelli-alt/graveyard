import os
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

@pytest.fixture
def browser(request):
    if "DISPLAY" in os.environ and "PHANTOM" not in os.environ:
        browser = webdriver.Firefox()
    else:
        browser = webdriver.PhantomJS()
    request.addfinalizer(lambda: browser.quit())
    return browser

@pytest.mark.slow
def test_can_choose_domain(browser, live_server):
    browser.get(live_server.url)
    domain_input = browser.find_element_by_name("domain")
    assert domain_input

    tld_select = Select(browser.find_element_by_name("tld"))
    tld_options = [o.text for o in tld_select.options]
    assert ".me" in tld_options
    assert ".ch" in tld_options
    assert ".com" in tld_options
    tld_select.select_by_visible_text(".me")
    create_button = browser.find_element_by_name("submit")
    create_button.click()
#    assert "Registration" in browser.title

