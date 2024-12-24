from bson import ObjectId
from django.db.models.expressions import result
from pymongo import MongoClient

# MongoDB connection setup
client = MongoClient("mongodb://localhost:27017/")
db = client["codeforces_db"]  # Database name

# Collections
problems_collection = db["problems"]
solutions_collection = db["solutions"]


def insert_problem (problem_object) :
    problem_id = problems_collection.insert_one(problem_object).inserted_id
    return problem_id

def update_problem (problem_id , problem_object):
    problem_id = ObjectId(problem_id)
    res = problems_collection.find_one({"_id": problem_id})
    result = problems_collection.update_one({"_id" : problem_id},{"$set":problem_object})

def get_problem_by_link (problem_link):
    res = problems_collection.find_one({"link": problem_link})
    return res


def delete_problem (problem_id):
    problem_id = ObjectId(problem_id)
    problems_collection.delete_one({"_id": problem_id})


def insert_problem_with_solutions(problem_name, problem_statement, tags, solutions):
    """
    Inserts a problem and its solutions into MongoDB.

    Parameters:
        problem_name (str): Name of the problem.
        problem_statement (str): Problem description.
        tags (list of str): Tags associated with the problem.
        solutions (list of dict): List of solutions with 'language' and 'code'.
    """
    # Insert Problem
    problem_document = {
        "problem_name": problem_name,
        "problem_statement": problem_statement,
        "tags": tags
    }
    problem_id = problems_collection.insert_one(problem_document).inserted_id

    # Insert Solutions
    solution_documents = [
        {
            "problem_id": problem_id,
            "language": solution["language"],
            "code": solution["code"]
        }
        for solution in solutions
    ]
    solutions_collection.insert_many(solution_documents)
    print(f"Problem '{problem_name}' and its solutions inserted successfully!")
