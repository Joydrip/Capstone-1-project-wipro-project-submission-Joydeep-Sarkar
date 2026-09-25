from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://tutorialsninja.com/demo/")
    print("Page title:", driver.title)

    driver.save_screenshot("screenshots/simple_test.png")
    print("Screenshot saved")

finally:
    driver.quit()