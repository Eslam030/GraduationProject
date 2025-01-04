import requests
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
import ast
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
from codeforces_scraper import db_setup

import undetected_chromedriver as uc

import time

from codeforces_scraper.db_setup import problems_collection


class ProblemStatement :
    def __init__(self ,):
        # driver_path = 'D:\\moviies\\testcases\\New\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'  # Change this to the path of your ChromeDriver
        # service = ChromeService(executable_path=driver_path)
        # # self.driver = webdriver.Chrome(service=service)
        self.driver = uc.Chrome()
    problem_statement = ""
    def scrap_the_tag (self , node) :
        children = node.find_elements(By.XPATH, "./*")

        for child in children :
            self.scrap_the_tag(child)



    def get_problem_statement(self , link ):
        time.sleep(2)
        self.driver.get(link)
        time.sleep(2)
        try :
            time_limit = self.driver.find_elements(By.CSS_SELECTOR, '.problem-statement > :nth-child(1) > :nth-child(2)')[
                0].text
            memory_limit = self.driver.find_elements(By.CSS_SELECTOR, '.problem-statement > :nth-child(1) > :nth-child(3)')[
                0].text
            problem_statement = self.driver.find_elements(By.CSS_SELECTOR, '.problem-statement > :nth-child(2)')[0].text

            # print(self.driver.find_elements(By.CSS_SELECTOR, '.problem-statement > :nth-child(2)')[0])
            print(problem_statement)


            # return

            input_constraint = self.driver.find_elements(By.CSS_SELECTOR, '.problem-statement > :nth-child(3)')[0].text
            output_constraint = self.driver.find_elements(By.CSS_SELECTOR, '.problem-statement > :nth-child(4)')[0].text
            sample_input = self.driver.find_elements(By.CSS_SELECTOR,
                                                '.problem-statement > :nth-child(5) > :nth-child(2) > :nth-child(1) :nth-child(2)')[
                0].text
            sample_output = self.driver.find_elements(By.CSS_SELECTOR,
                                                 '.problem-statement > :nth-child(5) > :nth-child(2) > :nth-child(2) :nth-child(2)')[
                0].text

            problem_statement = problem_statement.replace('\n', ' ')

            input_constraint = input_constraint.replace('\n', ' ')
            output_constraint = output_constraint.replace('\n', ' ')

            # clean the memory and time limit fields
            memory_limit = memory_limit.replace("memory limit per test", "").replace(" megabytes", "")
            time_limit = time_limit.replace("time limit per test", "").replace(" seconds", "")
            return {
                'time_limit': time_limit,
                'memory_limit': memory_limit,
                'problem_statement': problem_statement,
                'input_constraint': input_constraint,
                'output_constraint': output_constraint,
                'sample_input': sample_input,
                'sample_output': sample_output
            }
        except Exception as ex :
            with open ("failed_to_fetch.txt" , "a") as f:
                f.write(f"link {link} error {str(ex)}\n")




    def upload_problem_statement_object (self , problem_statement):
        print(problem_statement.get('link'))
        if not problems_collection.find_one({"link" : problem_statement.get('link')}) :
            db_setup.insert_problem(problem_statement)


    def run (self) :
        with open ("problem_links.txt", "r") as f:
            links = f.read().splitlines()
            for link in links:
                link_without_tags = ""
                tags_with_rating = ""
                is_link = True
                for char in link:
                    if not is_link:
                        tags_with_rating += char
                    if char != " " and is_link:
                        link_without_tags += char
                    else :
                        is_link = False
                rate = ""
                tags = ""
                is_rate = True
                for i in range (len(tags_with_rating) - 1 , -1 , -1) :
                    if tags_with_rating[i] == " " :
                        is_rate = False
                        continue
                    if is_rate :
                        rate += tags_with_rating[i]
                    else :
                        tags += tags_with_rating[i]
                rate = rate[::-1]
                tags = tags[::-1]
                if rate == "None" or int(rate) >= 1600:
                    continue
                problem = self.get_problem_statement(link_without_tags)
                if problem :
                    problem['tags'] = ast.literal_eval(tags)
                    problem['link'] = link_without_tags
                    problem['rate'] = rate
                    self.upload_problem_statement_object(problem)


        self.driver.quit()