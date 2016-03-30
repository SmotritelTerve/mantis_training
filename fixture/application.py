# from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper


class Application:

    def __init__(self, browser, base_url):
        # self.wd = WebDriver()
        if browser == "firefox":
            profile = webdriver.FirefoxProfile()
            profile.set_preference('browser.startup.homepage', '')
            profile.set_preference('startup.homepage_welcome_url', '')
            profile.set_preference('startup.homepage_welcome_url.additional', '')
            self.wd = webdriver.Firefox(profile)
        elif browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
            options.add_argument('--disable-extensions')
            self.wd = webdriver.Chrome(chrome_options=options)
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)

        # self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()