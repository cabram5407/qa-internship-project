from pages.base_page import Page
from pages.login_page import LoginPage
from pages.profile_setting_page import SettingPage
from pages.profile_edits_page import  ProfileChange
from pages.profile_update_page import ProfileUpdatePage



#Reference for page objects. It acts as a library that leads to the other pages. It acts as an umbrella



class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.login_page = LoginPage(driver)
        self.profile_setting_page = SettingPage(driver)
        self.profile_edits_page = ProfileChange(driver)
        self.profile_update_page = ProfileUpdatePage(driver)









