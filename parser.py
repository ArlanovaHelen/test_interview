import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import sqlite_db
import schedule
import asyncio





async def static_task_pars():
	service=Service(executable_path=ChromeDriverManager().install())

	driver = webdriver.Chrome(service=service)

	driver.get("https://robota.ua/")
	url = driver.current_url

	assert url=="https://robota.ua/", "Error page"

	ocupation_field = driver.find_element(By.XPATH, "//input[@type='text']")
	ocupation_field.send_keys("junior")

	time.sleep(3)
	assert ocupation_field.get_attribute("value")=="junior", "Error value" # Перевіряємо чи правильно введене значення в поле

	a = driver.find_elements(By.TAG_NAME, "santa-button")[1].click()

	time.sleep(2)

	count_field = driver.find_elements(By.CSS_SELECTOR, "div.santa-typo-h2")[0].text

	#count_field = driver.find_elements(By.TAG_NAME, "div")[31].text
	#print(count_field)

	count=""
	for i in count_field:
	    if i.isdigit():
	        count += i
	quantity = int(count)
	print(quantity)
	sqlite_db.db_connect()


	try:
		last_count = sqlite_db.select_last()
		different = quantity - int(last_count[0])
	except:
		different=0

	sqlite_db.create_report(quantity, different)


async def main():
    task1 = asyncio.create_task(static_task_pars())


if __name__ == '__main__':
	while True:
		asyncio.run(main())
		time.sleep(3600)


	# schedule.every().day.at("00:00").do(static_task_pars)
