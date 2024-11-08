from pages.base_page import Page
from pages.help_page import HelpPage
from pages.search_results_page import SearchResultsPage


#Reference for page objects. It acts as a library that leads to the other pages. It acts as an umbrella
class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.help_page = HelpPage(driver)
        self.search_results_page = SearchResultsPage(driver)



