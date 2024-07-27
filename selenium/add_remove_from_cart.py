import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import login  # Import the login module

# Configure logging
logging.basicConfig(
    filename='selenium.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger()

def add_remove_from_cart(driver):
    #######################################################################################
    # Check clicking on the 'Add to cart' button for Sauce Labs Backpack
    #######################################################################################
    try:
        addcarts = driver.find_elements(By.CSS_SELECTOR, ".btn.btn_primary.btn_small.btn_inventory")
        if addcarts:
            print(f"Number of 'Add to cart' buttons found: {len(addcarts)}")
            logger.info(f"Number of 'Add to cart' buttons found: {len(addcarts)}")
            for addcart in addcarts:
                print(f"Button found with text: {addcart.text}")
                logger.info(f"Button found with text: {addcart.text}")
                addcart.click()
                print('Click on the button with class Add cart successful')
                logger.info('Click on the button with class Add cart successful')

                # Wait for the button to transform into "Remove"
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".btn_secondary.btn_small.btn_inventory"))
                )
                print('The button has transformed into Remove')
                logger.info('The button has transformed into Remove')
        else:
            print("No 'Add to cart' buttons found on the page.")
            logger.info("No 'Add to cart' buttons found on the page.")
    except Exception as e:
        print(f"An error occurred: {e}")
        logger.info(f"An error occurred: {e}")

# If this file is executed directly, perform the login and add/remove from cart actions
if __name__ == "__main__":
    driver = login.login('standard_user', 'secret_sauce')
    add_remove_from_cart(driver)
    #input("Press Enter to close the browser...")
    driver.quit()
