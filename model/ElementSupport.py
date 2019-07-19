class GetCurrentUrl(object):
    def __call__(self, driver):
        return driver.current_url