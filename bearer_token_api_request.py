import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth
from request_methods import make_request
import configure_logging
import logging


base_url = 'http://127.0.0.1:8000' 
load_dotenv()
logging.info("setting up base URL")


BEARER_TOKEN = os.getenv("token")
headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}
def get_base_endpoint():
    endpoint = '/'
    logging.info(f"using Base URL")
    code, text = make_request('GET', endpoint, base_url, headers=headers)
    logging.info(f"Response [{code}], {text}")

def get_hello_endpoint():
    endpoint = '/hello'
    logging.info(f"Calling /hello endpoint")
    code, text = make_request('GET', endpoint, base_url, headers=headers)
    logging.info(f"Response [{code}], {text}")

def get_goodbye_endpoint():
    endpoint = '/goodbye'
    logging.info(f"Calling /goodbye endpoit")
    code, text = make_request('GET', endpoint, base_url, headers=headers)
    logging.info(f"Respone [{code}],{text}")

def get_all_students():
    endpoint = '/students/'
    logging.info(f"Calling /students/ details endpoint")
    code, text = make_request('GET', endpoint, base_url, headers=headers)
    logging.into(f"Response [{code}], {text}")

def get_student_by_id():
    student_id = int(input("Enter student ID: "))
    endpoint = f'/students/{student_id}'
    logging.info(f"Calling student details with student ID: {student_id}")
    code, text = make_request('GET', endpoint, base_url, headers=headers)
    logging.info(f"Response [{code}], {text}")

def create_student():
    firstname = input("Enter your first name: ")
    lastname = input("Enter your last name: ")
    age = int(input("Enter your age: "))
    email = input("Enter your _@gmail.com Email: ")
    bio = input("Enter your Bio: ")

    payload = {
        'firstname': firstname,
        'lastname': lastname,
        'age': age,
        'email': email,
        'bio': bio
    }

    endpoint = '/create'
    logging.info(f"Creating New Student ID and details")
    code, text = make_request('POST', endpoint, base_url, headers=headers, payload=payload)
    logging.info(f"Response [{code}], {text}")

def edit_student():
    student_id = int(input("Enter the ID of the student to edit: "))
    firstname = input("Enter your first name: ")
    lastname = input("Enter your last name: ")
    age = int(input("Enter your age: "))
    email = input("Enter your _@gmail.com Email: ")
    bio = input("Enter your Bio: ")

    payload = {
        'firstname': firstname,
        'lastname': lastname,
        'age': age,
        'email': email,
        'bio': bio
    }

    endpoint = f'/{student_id}/edit'
    logging.info(f"Editing Student deatails from student ID: {student_id}")
    code, text = make_request('POST', endpoint, base_url, headers=headers, payload=payload)
    logging.info(f"Response [{code}], {text}")

def delete_student():
    student_id = int(input("Enter the ID of the student to delete: "))
    endpoint = f'/{student_id}/delete'
    logging.info(f"Deleting student from student ID: {student_id}")
    code, text = make_request('DELETE', endpoint, base_url, headers=headers)
    logging.info(f"Response [{code}], {text}")
    
if __name__ == "__main__":
    get_base_endpoint()
    get_hello_endpoint()
    get_goodbye_endpoint()
    get_all_students()
    get_student_by_id()
    create_student()
    edit_student()
    delete_student()