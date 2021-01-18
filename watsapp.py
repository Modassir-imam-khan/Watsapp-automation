from selenium import webdriver
import time


timeout_secs=200
username = 'Person Name'
message = 'Message to send'


browser = start_chrome('https://web.whatsapp.com/')
wait_until(Text('Keep your phone').exists,timeout_secs=timeout_secs )
search_box = browser.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
search_box.clear()
search_box.send_keys(username)
time.sleep(1)
user = browser.find_element_by_xpath(f'//span[@title="{username}"]')
user.click()
#enter no of messages you want to send in range section

for i in range(1,50):    
    message_box = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    message_box.send_keys(message)
    browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
print('Sucess!')