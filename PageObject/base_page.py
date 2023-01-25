class BasePage():
    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.browser.current_url)