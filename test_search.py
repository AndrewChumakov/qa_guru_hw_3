from selene import be, have


def test_search_success(browser_driver):
    browser_driver.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser_driver.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_search_without_result(browser_driver):
    browser_driver.element('[name="q"]').should(be.blank).type('wqer23resfew@#WF$@#TRDFE@#$%@#W$RWER').press_enter()
    browser_driver.element('.card-section').should(be.present).should(
        have.text('Your search - wqer23resfew@#WF$@#TRDFE@#$%@#W$RWER - did not match any documents.'))
