import requests
import json
from codeforces_scraper.db_setup import delete_problem
from .codeforces_submission import Submissions
class SubmissionLinks :
    def __init__(self , driver):
        self.sub = Submissions(driver)

    def get_from_handle_submission (self , handle , project_object) :
        pass

    def upload_submission_links (self , problem_object) :
        problem_link = problem_object.get('link').split('/')
        contest_id = problem_link[-3]
        problem_index = problem_link[-2]
        print(contest_id , problem_index)

        standing_link = f"https://codeforces.com/api/contest.standings?contestId={contest_id}&from=1&showUnofficial=true"
        # may be optimized in the future
        response = requests.get(standing_link)
        response = json.loads(response.content)
        current_index = 0
        wanted_index = 0
        for problem in response['result']['problems']:
            if problem['index'] == problem_index :
                wanted_index = current_index
                break
            current_index += 1
        standing = response['result']['rows'][:20]
        for stand in standing :
            handle = None

            if len(stand['party']['members']) > 0 :
                handle = stand['party']['members'][0]['handle']

            problem_results = stand['problemResults'][wanted_index]

            if handle and 'bestSubmissionTimeSeconds' in problem_results:
                # get the submissions for this handle
                print(handle)
                submissions_link = f"https://codeforces.com/api/user.status?handle={handle}&from=1"
                response = requests.get(submissions_link)
                response = json.loads(response.content)

                for submission in response['result']:
                    if submission.get('contestId') == int(contest_id) and submission.get('verdict') == "OK" and submission.get('problem').get('index') == problem_index :
                        submission_link = f"https://codeforces.com/contest/{contest_id}/submission/{submission['id']}"
                        print(submission_link)
                        self.sub.get_submission_code(submission_link)

