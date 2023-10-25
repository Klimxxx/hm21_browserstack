from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_search():
    with step("Find Wikipedia search"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
    with step("Type Browserstack"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("BrowserStack")
    with step("Find resuls"):
        results = browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView"))
    with step("Check resuls"):
        results.should(have.size_greater_than(0))

def test_main_page_contains_1topic_in_the_news():
    with step("Check main page contains 1st topic 'in the news'"):
        browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/view_card_header_title")).first.should(have.text("In the news"))


def test_search_result_with_mistake():
    with step("Find Wikipedia search"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
    with step("Type www"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("www")
    with step("Click 1st suggested"):
        browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/search_container")).first.click()
    with step("Check button GO_BACK"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/view_wiki_error_button")).should(have.text("GO BACK"))


