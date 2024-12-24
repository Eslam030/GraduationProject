# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# import re
# import requests
# # import pandas as pd
#
# def scrap_problem_data_from_link(link):
#     driver_path = 'D:\\moviies\\testcases\\New\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'  # Change this to the path of your ChromeDriver
#     service = ChromeService(executable_path=driver_path)
#     driver = webdriver.Chrome(service=service)
#     # time.sleep(2)
#     driver.get(link)
#     # time.sleep(2)
#     time_limit = driver.find_elements(By.CSS_SELECTOR, '.problem-statement > :nth-child(1) > :nth-child(2)')[0].text
#     memory_limit = driver.find_elements(By.CSS_SELECTOR, '.problem-statement > :nth-child(1) > :nth-child(3)')[0].text
#     problem_statement = driver.find_elements(By.CSS_SELECTOR, '.problem-statement > :nth-child(2)')[0].text
#     input_constraint = driver.find_elements(By.CSS_SELECTOR, '.problem-statement > :nth-child(3)')[0].text
#     output_constraint = driver.find_elements(By.CSS_SELECTOR, '.problem-statement > :nth-child(4)')[0].text
#     sample_input = driver.find_elements(By.CSS_SELECTOR,
#                                         '.problem-statement > :nth-child(5) > :nth-child(2) > :nth-child(1) :nth-child(2)')[
#         0].text
#     sample_output = driver.find_elements(By.CSS_SELECTOR,
#                                          '.problem-statement > :nth-child(5) > :nth-child(2) > :nth-child(2) :nth-child(2)')[
#         0].text
#
#     problem_statement = problem_statement.replace('\n', ' ')
#     input_constraint = input_constraint.replace('\n', ' ')
#     output_constraint = output_constraint.replace('\n', ' ')
#
#     return {
#         'time_limit': time_limit,
#         'memory_limit': memory_limit,
#         'problem_statement': problem_statement,
#         'input_constraint': input_constraint,
#         'output_constraint': output_constraint,
#         'sample_input': sample_input,
#         'sample_output': sample_output
#     }
#
# def get_all_problem_links():
#     problems_with_tags = {}
#
#     response = requests.get("https://codeforces.com/api/problemset.problems/")
#     data = response.json()
#     data = data['result']['problems']
#     for problem in data:
#         for tag in problem.get('tags', []):
#             if tag not in problems_with_tags:
#                 problems_with_tags[tag] = []
#             link = 'https://codeforces.com/problemset/problem/' + str(problem['contestId']) + '/' + problem['index'] + '/'
#             problems_with_tags[tag].append(link)
#     return problems_with_tags
#
# #
#
#
# tags_with_link = get_all_problem_links()
# count = 1
# limit = 2
# for tag in tags_with_link :
#     # apply scraping for each problem link
#     for link in tags_with_link[tag] :
#         print(scrap_problem_data_from_link(link))
#         if count == limit :
#             exit()
#
#         count += 1
#
#
# # scrap_problem_statement_from_link('https://codeforces.com/problemset/problem/2033/B')
#
#
#
#
#
# # scrap_problem_statement_from_link('https://codeforces.com/problemset/problem/2036/G/')














# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# import time
#
# # Set up Chrome options
# chrome_options = Options()
# chrome_options.add_argument("--start-maximized")
#
# # Provide the path to the ChromeDriver
# service = Service("D:\\moviies\\testcases\\New\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")  # Update the path to your ChromeDriver
# driver = webdriver.Chrome(service=service, options=chrome_options)
#
# try:
#     # Open the Codeforces login page
#     driver.get("https://codeforces.com/enter")
#
#     # Wait for the page to load
#     time.sleep(2)  # Consider using WebDriverWait for better handling
#
#     # Find the username and password input fields
#     username_input = driver.find_element(By.NAME, "handleOrEmail")
#     password_input = driver.find_element(By.NAME, "password")
#
#     # Input your credentials
#     username_input.send_keys("Eslam7215")  # Replace with your username
#     password_input.send_keys("01157228162e2")  # Replace with your password
#
#     # Submit the form
#     password_input.send_keys(Keys.RETURN)
#
#     # Wait for human verification (CAPTCHA)
#     print("Please complete the CAPTCHA manually.")
#
#     # You can wait here until the CAPTCHA is solved
#     time.sleep(60)  # Adjust the time as needed
#
#     # After solving the CAPTCHA, you can proceed with further actions
#     # e.g., navigate to a specific page, scrape data, etc.
#
# finally:
#     # Close the driver
#     driver.quit()



# from selenium import webdriver
# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By
# import requests
# import time
#
# # Set up WebDriver
# driver = webdriver.Chrome()  # Ensure path to ChromeDriver is correct
#
# # Open Codeforces login page
# driver.get("https://codeforces.com/enter")
#
# # Enter your credentials
# driver.find_element(By.NAME, "handleOrEmail").send_keys("Eslam7215")
# driver.find_element(By.NAME, "password").send_keys("01157228162e2")
#
# # Submit the form
# driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
#
# # Capture CAPTCHA token
# site_key = "your-site-key"  # You can find the CAPTCHA site key in the page source
# api_key = "your-2captcha-api-key"  # Replace with your 2Captcha API key
#
# # Request CAPTCHA solution
# captcha_url = f"http://2captcha.com/in.php?key={api_key}&method=userrecaptcha&googlekey={site_key}&pageurl=https://codeforces.com/enter"
# response = requests.get(captcha_url)
#
# if response.text.startswith("OK|"):
#     captcha_id = response.text.split("|")[1]
#     # Poll for CAPTCHA result
#     while True:
#         result_url = f"http://2captcha.com/res.php?key={api_key}&action=get&id={captcha_id}"
#         result = requests.get(result_url).text
#         if result.startswith("OK|"):
#             captcha_solution = result.split("|")[1]
#             break
#         time.sleep(30)  # Check every 5 seconds for the solution
#
#     # Submit CAPTCHA solution (this part will depend on the form's structure)
#     driver.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML = '{captcha_solution}';")
#     # Submit the form again if needed


# import undetected_chromedriver as uc
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import requests
# import time
#
#
# def login_codeforces_with_captcha():
#     # Set up undetected-chromedriver to bypass detection
#     driver = uc.Chrome()
#     driver.get("https://codeforces.com/enter")
#
#     # Enter your credentials
#     driver.find_element(By.NAME, "handleOrEmail").send_keys("your_username")  # Replace with your Codeforces username
#     driver.find_element(By.NAME, "password").send_keys("your_password")  # Replace with your Codeforces password
#
#     # CAPTCHA site key and 2Captcha API key
#     site_key = "6LfZKw8UAAAAAJc3vlM_GE7B3umCrpO2fFZ1YOVc"  # Replace this with the actual site key found in the HTML
#     api_key = "your_2captcha_api_key"  # Replace with your 2Captcha API key
#
#     # Request CAPTCHA solution
#     captcha_url = f"http://2captcha.com/in.php?key={api_key}&method=userrecaptcha&googlekey={site_key}&pageurl=https://codeforces.com/enter"
#     response = requests.get(captcha_url)
#
#     if response.text.startswith("OK|"):
#         captcha_id = response.text.split("|")[1]
#
#         # Poll for CAPTCHA result
#         while True:
#             result_url = f"http://2captcha.com/res.php?key={api_key}&action=get&id={captcha_id}"
#             result = requests.get(result_url).text
#             if result.startswith("OK|"):
#                 captcha_solution = result.split("|")[1]
#                 break
#             elif result == "CAPCHA_NOT_READY":
#                 time.sleep(5)  # Wait a bit and retry
#             else:
#                 print("Error solving CAPTCHA:", result)
#                 driver.quit()
#                 return
#
#         # Inject CAPTCHA solution using JavaScript
#         driver.execute_script("document.getElementById('g-recaptcha-response').innerHTML = arguments[0];",
#                               captcha_solution)
#
#         # Submit the form after solving CAPTCHA
#         driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
#
#         # Optional: Wait and check if login was successful
#         time.sleep(3)  # Adjust as needed
#         if "logout" in driver.page_source:
#             print("Login successful!")
#         else:
#             print("Login failed or CAPTCHA verification failed.")
#
#     else:
#         print("Error submitting CAPTCHA request:", response.text)
#
#     # Clean up and close the driver
#     driver.quit()
#
#
# # Call the function to perform login
# login_codeforces_with_captcha()


import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# # Your Codeforces credentials
# USERNAME = "Test12347088@gmail.com"  # Replace with your actual username
# PASSWORD = "01157228162e2"  # Replace with your actual password
#
# # URL of the login page
# URL = "https://codeforces.com/enter"
#
# from undetected_chromedriver import Chrome, ChromeOptions
# def login_codeforces_speed ():
#     # options = ChromeOptions()
#     # options.add_argument("--headless")  # Use headless if UI isn’t needed
#     # options.add_argument("--disable-extensions")
#     # options.add_argument("--disable-images")  # Disable images for faster load
#     # options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
#     # options.page_load_strategy = "eager"
#
#     driver = Chrome()
#
#     driver.get(URL)
#     driver.find_element(By.NAME, "handleOrEmail").send_keys(USERNAME)
#     driver.find_element(By.NAME, "password").send_keys(PASSWORD)
#     driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
#
#     # Pause and wait for manual CAPTCHA solving
#     print("If a CAPTCHA is presented, please solve it manually within the browser.")
#     time.sleep(10)  # Adjust the time as needed for CAPTCHA-solving
#
#     # Optional: Verify login success
#     if "logout" in driver.page_source:
#         print("Login successful!")
#     else:
#         print("Login failed or CAPTCHA verification failed.")
#
#
#     urls = ["https://codeforces.com/contest/2028/submission/290916694", "https://codeforces.com/contest/2028/submission/290922683"]
#
#     for submission in urls :
#         driver.get(submission)
#         time.sleep(10)
#
#
# login_codeforces_speed()





# from codeforces_scraper import db_setup
#
#
#
# # id = db_setup.insert_problem({
# #     "problem_name" : "test" ,
# #     "problem_description": "test2" ,
# # })
#
#
# db_setup.update_problem("67691fa3382d7635a0774be6" , {
#     "problem_name": "testdd",
#     "problem_description": "test2",
#
# })



# if __file__ == "__main__":
#     open("failed_to_fetch.txt").close()
#     open("problem_links.txt").close()


"""
Getting Problemstatment links and upload it in problem_links.txt
"""
# from codeforces_library.codeforces_problemstatement_links import ProblemStatementLinks
# ProblemStatementLinks().upload_problem_links()
"""
Scrapping the problemstatment from each link
"""
# from codeforces_library.codeforces_problemstatement import ProblemStatement
# ProblemStatement().run()

# from codeforces_scraper.db_setup import get_problem_by_link
# problem = get_problem_by_link("https://codeforces.com/problemset/problem/2052/T/")
# print(problem.get('_id'))


from codeforces_library.codeforces_submission_links import SubmissionLinks
from codeforces_scraper.db_setup import problems_collection
objects = problems_collection.find()
for object in objects:
    SubmissionLinks().upload_submission_links(object)
    # print(object)
    break
# SubmissionLinks().upload_submission_links(problem.get('_id'))
