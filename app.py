from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users/Lenovo/Downloads/chromedriver_win32/chromedriver.exe")  
driver.maximize_window()  

driver.get("https://app.cloudqa.io/home/AutomationPracticeForm") 

first_name_xpath = "/html/body/div[1]/form/div[1]/div[2]/input"
last_name_xpath = "/html/body/div[1]/form/div[1]/div[3]/input"
gender_xpath = "/html/body/div[1]/form/div[1]/div[4]/div/"

# gender options 
male = "input[1]"
female = "input[2]"
trans = "input[3]"


# form 
first_name = "Aayush"
last_name = "Harwani"
gender = male 


driver.find_element_by_xpath(first_name_xpath).send_keys(first_name)
driver.find_element_by_xpath(last_name_xpath).send_keys(last_name)
driver.find_element_by_xpath(gender_xpath+gender).click()
