# Selenium Task:
# Step-1: Go to URL(https://katalon-test.s3.amazonaws.com/aut/html/form.html)
# Step-2: Enter the first name
# Step-3: Enter the last name
# Step-4: Select the Gender (radio button)
# Step-5: Select the date of birth (calendar)
# Step-6: Enter your address
# Step-7: Enter your email
# Step-8: Enter the password
# Step-9: Enter your company name
# Step-10: Select your role in the company from dropdown
# Step-11: Select the job expectation from selectbox
# Step-12: Select the ways of development from checkbox (multiple can be checked)
# Step-13: Enter the comment
# Step-14: Click on the Submit button
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time
browser = "chrome"  # chrome, firefox, edge
driver = ''
if browser == "chrome":
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
elif browser == "firefox":
    driver = webdriver.Firefox()
elif browser == "edge":
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Edge(options=options)
else:
    driver = webdriver.Chrome()
driver.get("https://katalon-test.s3.amazonaws.com/aut/html/form.html")
driver.maximize_window()
#Enter informatios
driver.find_element(By.ID,"first-name").send_keys("Maria")
driver.find_element(By.ID,"last-name").send_keys("Jones")
time.sleep(5)
driver.find_element(By.XPATH,"//label[normalize-space()='Female']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='dob']").send_keys("03/12/1990")
driver.find_element(By.NAME,"address").send_keys("23/A, New York City")
time.sleep(5)
driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
driver.find_element(By.NAME,"email").send_keys("maria@example.com")
driver.find_element(By.ID,"password").send_keys("password")
driver.find_element(By.ID,"company").send_keys("Corporate")
driver.find_element(By.XPATH,"(//select[@id='role'])[1]").click()
time.sleep(5)
driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
driver.find_element(By.XPATH,"//option[@value='Good teamwork']").click()
driver.find_element(By.XPATH,"//label[normalize-space()='Read books']").click()
driver.find_element(By.XPATH,"//label[normalize-space()='Take online courses']").click()
driver.find_element(By.XPATH,"//label[normalize-space()='Contribute to opensource projects']").click()
driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
driver.find_element(By.ID,"comment").send_keys("Open To Work")
time.sleep(10)
driver.find_element(By.XPATH,"//button[@id='submit']").click()
time.sleep(5)
act_id=driver.id="submit-msg"
exp_id="submit-msg"
if act_id==exp_id:
    print("Successfully Submitted!")
else:
    print("BUG")
