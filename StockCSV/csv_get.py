from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import datetime
import json
import os

all_stock = json.load(open(os.path.join(os.path.dirname(__file__), "stock.json")))

while True:
  stock_name = input('Enter stock ticker (ex. AAPL): ')
  if stock_name  not in all_stock:
    print('Invalid Ticker!\n')
  else:
    break

start_date = input('Enter start date (YYYY-MM-DD): ')
start_date = datetime.strptime(start_date, '%Y-%m-%d')
unix_1 = int(start_date.timestamp())

end_date = input('Enter end date (YYYY-MM-DD): ')
end_date = datetime.strptime(end_date, '%Y-%m-%d')
unix_2 = int(end_date.timestamp())

download_dir = os.path.join(os.getcwd(), os.path.dirname(__file__))
os.makedirs(download_dir, exist_ok=True)

url = f'https://finance.yahoo.com/quote/{stock_name}/history?period1={unix_1}&period2={unix_2}'

chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
  "download.default_directory": download_dir,
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

driver = Chrome(options=chrome_options)

driver.get(url), sleep(2)

download_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.subtle-link.fin-size-medium.svelte-wdkn18'))
)

download_link.click(), sleep(3)

