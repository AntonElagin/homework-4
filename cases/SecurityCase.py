import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from pages.AuthPage import AuthPage
from pages.SecurityPage import SecurityPage


class GetTest(unittest.TestCase):
    def runTest(self):
        self.test_click_password_more_link()
        self.test_click_keys_more_link()
        self.test_click_twofact_more_link()

        self.test_click_history_link()
        self.test_click_oauth_link()
        self.test_click_devices_link()
        self.test_click_services_link()
        self.test_click_setPassword_link()
        self.test_click_keys_link()
        

    def setUp(self):
        browser = 'CHROME'
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        LOGIN = os.environ['LOGIN']
        PASSWORD = os.environ['PASSWORD']

        auth_page = AuthPage(self.driver)
        auth_page.auth(LOGIN, PASSWORD)
        security_page = SecurityPage(self.driver)
        security_page.open()
        self.security_page = SecurityPage(self.driver)

    def go_to_main(self):
        self.security_page.open(self.security_page.BASE_URL)
        

    def tearDown(self):
        self.driver.quit()

    def test_click_devices_link(self):
        isOkey = self.security_page.click_devices_link()
        self.assertTrue(isOkey)
        self.go_to_main()

    def test_click_services_link(self):
        isOkey = self.security_page.click_services_link()
        self.assertTrue(isOkey)
        self.go_to_main()

    def test_click_setPassword_link(self):
        isOkey = self.security_page.click_setPassword_link()
        self.assertTrue(isOkey)
        self.go_to_main()

    def test_click_history_link(self):
        isOkey = self.security_page.click_history_link()
        self.assertTrue(isOkey)
        self.go_to_main()

    def test_click_oauth_link(self):
        isOkey = self.security_page.click_oauth_link()
        self.assertTrue(isOkey)
        self.go_to_main()

    def test_click_keys_link(self):
        isOkey = self.security_page.click_keys_link()
        self.assertTrue(isOkey)
        self.go_to_main()

    def test_click_password_more_link(self):
        isOkey = self.security_page.click_password_more_link()
        self.assertTrue(isOkey)
        self.go_to_main()

    def test_click_twofact_more_link(self):
        isOkey = self.security_page.click_twofact_more_link()
        self.assertTrue(isOkey)
        self.go_to_main()
    
    def test_click_keys_more_link(self):
        isOkey = self.security_page.click_keys_more_link()
        self.assertTrue(isOkey)
        self.go_to_main()
        
    