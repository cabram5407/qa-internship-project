from selenium.webdriver.common.by import By
from pages.base_page import Page

from selenium.webdriver.common.action_chains import ActionChains

#Class pages use "camel case" naming convention, no underscore '_'
class SearchResultsPage(Page):
    SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
    HEART_ICON = (By.CSS_SELECTOR, "[data-test='FavoritesButton']")
    FAV_TOOLTIP = (By.XPATH, "//*[contains(text(), 'Click to sign in and save')]")

    def hover_favorites(self):
        heart_icon = self.find_element(*self.HEART_ICON)

        actions = ActionChains(self.driver)
        actions.move_to_element(heart_icon)
        actions.perform()

    def verify_favorites(self):
        self.wait_for_element_to_appear(*self.FAV_TOOLTIP)


    def verify_results(self, item)
        self.verify_partial_text(item, *self.SEARCH_RESULTS_HEADER)

    def verify_results_url(self, item):
        self.verify_partial_url(item)

    def sign_in_form(self):
        self.verify_sign_in_page(*self.SIGN_IN_FORM_OPEN)

   def empty_cart(self):
        expected_result = 'Your cart is empty'
        actual_result = self.driver.find_element(*self.EMPTY_CART_HEADER).text
        assert expected_result == actual_result, f'Expected {expected_result}, got {actual_result}'


