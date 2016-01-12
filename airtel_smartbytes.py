from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# https://pypi.python.org/pypi/PyVirtualDisplay
from pyvirtualdisplay import Display

SMART_BYTES_URL = 'http://www.airtel.in/forme/home/smartbytes'


def access_smartbytes_page(browser, display):
    """
    Visit Airtel smart bytes
    """
    browser.get(SMART_BYTES_URL)
    try:
        print 'Finding the element...'
        browser.find_element_by_class_name('icon-3g').click()
        print 'Got element...'
        browser.switch_to_window(browser.window_handles[-1])
    except Exception as error:
        print error
        destroy(browser, display)
        exit(0)

    print browser.title, dir(browser)
    print browser.current_url


def init_driver():
    # Used to hide browser
    display = Display(visible=0, size=(1080, 1200))
    display.start()
    # Initialize browser
    browser = webdriver.Firefox()
    return browser, display


def destroy(browser, display):
    """
    Stop browser and display which is running in the backgroud
    """
    browser.quit()
    display.stop()


if __name__ == '__main__':
    # initialize browser and display
    browser, display = init_driver()
    try:
        access_smartbytes_page(browser, display)
    except Exception as error:
        print error
        destroy(browser, display)
        exit(0)

    # stop display and browser
    destroy(browser, display)
