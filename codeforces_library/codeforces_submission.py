import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from codeforces_scraper.db_setup import upload_submission


class Submissions :
    def __init__ (self , driver) :
        self.driver = driver

    def log_submission_data (self , problem_link , submission_link , author) :
        with open("submission_logging.txt" , "a") as f :
            f.write(f"{problem_link} {submission_link} {author}\n")
            # if the program crashed we will start from this problem link
            # and get its authors but we will not start scrapping until we get this author
            f.close()

    def get_submission_code (self , problem_link , submission_link , author):
        self.driver.get(submission_link)

        time.sleep(3)
        ol_element = self.driver.find_element(By.CLASS_NAME, 'linenums')

        # Extract all <li> elements within the <ol> tag
        li_elements = ol_element.find_elements(By.TAG_NAME, 'li')

        # Concatenate the text content of each <li> element
        result_text = '\n'.join([li.text for li in li_elements])

        # Print or use the concatenated string
        # print(result_text)
        submission_object = {
            "submission_link" : submission_link ,
            "problem_link" : problem_link ,
            "submission" : result_text ,
            "author" : author
        }

        upload_submission(submission_object)

        self.log_submission_data(problem_link , submission_link , author)








