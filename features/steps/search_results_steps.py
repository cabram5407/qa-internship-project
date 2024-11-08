 from selenium.webdriver.common.by import By
 from selenium.webdriver.support import expected_conditions as EC
 from behave import given, when, then
 from time import sleep

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id='addToCartButton']")
ADD_TO_CART_BTN_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "['data-test=content-wrapper'] h4")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWarpper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')
COLOR_OPTIONS = (By.CSS_SELECTOR, "div[aria-label='Carosel'] li img")
SELECTED_COLOR = (By.CSS_SELECTOR, "data-test='@web/VariationComponent'] div")

@when('Click on Add to Cart Button')
def click_add_to_cart_button(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    context.driver.wait.until(
        EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),
        message= 'Side navigation product name is not visible'
    )

@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_TITLE).text
    print(f'Product stored: {context.product_name}')

#Target product in cart test case
 @when('Confirm Add to Cart - Side Navigation')
 def side_nav_click_add_to_cart(context):
     context.driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()
     context.driver.wait.until(EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME))
     sleep(5)


@when('Hover favorites icon')
def hover_favorites(context):
    context.app.search_results_page.hover_favorites()


@then('Favorites tooltip is shown')
def verify_favorites(context):
    context.app.search_results_page.verify_favorites()


 @then('Verify search results show {item}')
 def verify_results(context, item):
     # actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
     # assert item == actual_result, f'Expected {item}, got actual {actual_result}'
     context.app.search_results_page.verify_results(item)

@then('Verify product {item} in URL')
def verify_results_url(context, item):
    context.app.search_results_page.verify_results_url(item)


 @then('Verify sign-in form shown')
     def verify_sign_in_form(context):
         actual_result = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
         expected_result = 'Sign into your Target account'
         assert expected_result == actual_result, f'Expected {expected_result}, got actual {actual_result}'


#Target circle test case
@then('Verify 10 benefit links')
     def verify_benefit_links(context, amount):
         links = context.driver.find_element(By.CSS_SELECTOR.driver.find_elements(By.CSS_SELECTOR,"[data-component='Cells Component Container'] [class*='cell-item-content']").text
         expected_result = int(links)
         assert len(expected_result) == expected_result, f'Expected {expected_result}, got actual {len(expected_result)}'


@ then('Verify header has {amount} links')
         def verify_header_links(context, amount):
             expected_amount = int(amount)
             links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
             assert len(links) == int(amount), f'Expected {amount} links, got {len(links)}'


@then('Verify header is shown')
         def verify_header(context):
             context.driver.find_element(By.CSS_SELECTOR, "[class*='styles_utilityHeaderContainer']")


#Verify Help UI elements present
 @then('Verify UI elements present')
 def verify_help_links(context, amount):
    links = context.driver.get.find.elements(By.CSS_SELECTOR, "[class='col-lg-12']").click()
     assert len(links) == int(amount), f'Expected {amount} links, got {len(links)}')


 @then('Verify product has name and image')
 def product_name_and_image(context, product, title):
     context.driver.execute_script("window.scrollBy"(0,2000)", "")
     sleep(4)
     context.driver.execute_script("window.scrollBy"(0,2000)", "")

     all_products = context.driver.find_elements(*LISTINGS)

      for product in all_products:
         title = product.find_element(*PRODUCT_TITLE).text
         assert title, 'Product title not shown'
         product.find_element(*PRODUCT_IMG)


 @then('Verify user can click through colors')
 def click_and_verif_colors(context):
     expected_colors= ['Blue Tint', 'Denim Blue', 'Marine', 'Raven']
     actual_colors =[]

     colors = context.driver.find_elements(*COLOR_OPTIONS)
     for color in colors:
         color.click()

         selected_color = context.driver.find_element(*SELECTED_COLOR).text

         selected_color = selected_color.split('\n')[1]
         actual_colors.append(selected_color)

     assert expected_colors == actual_colors, f'Expected {expected_colors} did match {actual_colors}'
