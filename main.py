import urllib.request

response = urllib.request.urlopen('https://httpbin.org/uuid')
data = response.read()
output = data.decode('utf-8')
print(output)

# url = "https://httpbin.org/uuid"
# response = requests.get(url)
# output = response.text()
# print(output)


# from datetime import datetime
# # from selenium import webdriver
# 
# today = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
# print(today)
# output = today

# options = webdriver.ChromeOptions()
# options.add_argument("headless=new")
# options.add_argument("--no-sandbox")
# 
# driver = webdriver.Remote(command_executor="http://188.245.144.110:4444/wd/hub", options=options)
# # driver.set_window_size(1280, 1024)
# 
# driver.get('https://amazon.fr')
# 
# print(driver.title)
# 
# output=driver.page_source
# 
# driver.quit()