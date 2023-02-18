import os
import tempfile
import json
from bson import json_util
from functools import reduce

from pymongo import MongoClient

client = MongoClient("mongodb://mongo:27017")
mydb = client["mydatabase"]
student_col = mydb["students"]

def add(student=None):
    # queries = []
    # query = Query()
    # queries.append(query.first_name == student.first_name)
    # queries.append(query.last_name == student.last_name)
    # query = reduce(lambda a, b: a & b, queries)
    # res = student_db.search(query)
    # if res:
    #     return 'already exists', 409

    # doc_id = student_db.insert(student.to_dict())
    # student.student_id = doc_id
    # return student.student_id

    query = {"student_id": student.student_id}
    query_find = student_col.find_one(query)

    if (query_find):
        return 'already exists', 409

    student_col.insert_one(student.to_dict())

    return student.student_id


def get_by_id(student_id=None, subject=None):
    # student = student_db.get(doc_id=int(student_id))
    # if not student:
    #     return 'not found', 404
    # student['student_id'] = student_id
    # print(student)
    # return student

    query = {"student_id": student_id}
    query_find = student_col.find_one(query)

    if (not query_find):
        return 'not found', 404
    
    return json.loads(json_util.dumps(query_find))

def delete(student_id=None):
    # student = student_db.get(doc_id=int(student_id))
    # if not student:
    #     return 'not found', 404
    # student_db.remove(doc_ids=[int(student_id)])
    # return student_id

    query = {"student_id": student_id}
    query_find = student_col.find_one(query)

    if (not query_find):
        return 'not found', 404
    
    student_col.delete_one(query)
    return student_id