import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure logging
logging.basicConfig(
    filename='selenium.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger()

def login(user, password):
    print('Starting the browser...')
    logger.info('Starting the browser...')
    
    options = ChromeOptions()
    options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)
    
    # Start the browser and navigate to the website
    driver.get('https://www.saucedemo.com/')

    # Enter username
    username_input = driver.find_element(By.CSS_SELECTOR, "input#user-name")
    username_input.send_keys(user)

    # Enter password
    password_input = driver.find_element(By.CSS_SELECTOR, "input#password")
    password_input.send_keys(password)

    # Find and click the login button
    login_button = driver.find_element(By.CSS_SELECTOR, "input#login-button")
    login_button.click()

    # Wait for the next page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".inventory_item"))
    )

    # Check for presence of products on the next page
    try:
        products = driver.find_elements(By.CSS_SELECTOR, ".inventory_item")
        if products:
            print(f"Number of products found: {len(products)}")
            logger.info(f"Number of products found: {len(products)}")
            for product in products:
                print(product.text)
                logger.info(product.text)
        else:
            print("No products found on the page.")
            logger.info("No products found on the page.")
    except Exception as e:
        print(f"An error occurred: {e}")
        logger.info(f"An error occurred: {e}")

    return driver

# If this file is executed directly, perform a login
if __name__ == "__main__":
    driver = login('standard_user', 'secret_sauce')
    #input("Press Enter to close the browser...")
    driver.quit()
