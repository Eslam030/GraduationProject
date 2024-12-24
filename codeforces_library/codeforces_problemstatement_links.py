import requests
class ProblemStatementLinks:
    def __init__(self):
        pass

    def get_all_problem_links(self):
        # categorize by tag
        response = requests.get("https://codeforces.com/api/problemset.problems/")
        data = response.json()
        data = data['result']['problems']
        links = []
        for problem in data:
            link = 'https://codeforces.com/problemset/problem/' + str(problem['contestId']) + '/' + problem[
                    'index'] + '/'
            link += " " + str(problem.get('tags'))
            links.append(link)
        return links

    def upload_problem_links(self):
        self.get_all_problem_links()
        links = self.get_all_problem_links()
        with open ("problem_links.txt", 'w') as f:
            for link in links:
                f.write(link + '\n')