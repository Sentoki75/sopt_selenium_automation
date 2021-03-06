from selenium.webdriver.chrome.options import Options
from selenium import webdriver

def set_chrome_options() -> None:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options

if __name__ == "__main__":
    print("Starting Selenium...")
    chrome_options = set_chrome_options()
    
    driver = webdriver.Chrome(options=chrome_options)
    print(driver.current_url)

    driver.close()

    print("Selenium closed.")
