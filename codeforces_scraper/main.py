from db_setup import insert_problem_with_solutions

# Mock Data - Replace with your scraping script
problem_name = "MEX Destruction"
problem_statement = "Problem description here..."
tags = ["dfs", "graph"]
solutions = [
    {"language": "Python", "code": "def solve(): pass"},
    {"language": "C++", "code": "#include<iostream>\nint main() { return 0; }"}
]

# Insert the scraped data into MongoDB
insert_problem_with_solutions(problem_name, problem_statement, tags, solutions)
