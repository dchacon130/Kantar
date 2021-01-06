import unittest
import time
import HtmlTestRunner

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 


class use_unittest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"G:\tmp\chromedriver")

	def test_download_csv(self):
		driver = self.driver
		driver.get("https://amrs-dev.engkantar.com")
		time.sleep(3)

		with open('datos.txt') as file:
			for i, line in enumerate(file):
				usuario = (line)
				sep = ","
				separate = usuario.split(sep)
				try:
					gotdata = separate[1]
					user = separate[0]
					pas = separate[1]
				except IndexError:
					gotdata = 'null'

				print(user)
				print(pas)

				driver.find_element_by_name("user").send_keys(user)
				driver.find_element_by_name("password").send_keys(pas)
				driver.find_element_by_xpath("//*[@id='login-form']/footer/button").click()
				time.sleep(3)
		file.close()

		driver.get("https://amrs-dev.engkantar.com/#/location/countries")
		time.sleep(3)
		driver.find_element_by_id("ToolTables_countryTable_0").click()
		time.sleep(10)
	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='ResultTests'))