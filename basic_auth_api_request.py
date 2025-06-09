import os
import logging
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth
from request_methods import make_request


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

base_url = 'http://127.0.0.1:8000' 
load_dotenv()
VALID_USERNAME = os.getenv("username")
VALID_PASSWORD = os.getenv("password1")

def get_base_endpoint():
    endpoint = '/'
    logging.info("Calling base endpoint")
    code, text = make_request('GET', endpoint=endpoint, base_url=base_url, auth=HTTPBasicAuth(VALID_USERNAME, VALID_PASSWORD))
    logging.info(f"Response [{code}]: {text}")

def get_hello_endpoint():
    endpoint = '/hello'
    logging.info("Calling /hello endpoint")
    code, text = make_request('GET', endpoint=endpoint, base_url=base_url, auth=HTTPBasicAuth(VALID_USERNAME, VALID_PASSWORD))
    logging.info(f"Response [{code}]: {text}")

def get_goodbye_endpoint():
    endpoint = '/goodbye'
    logging.info("Calling /goodbye endpoint")
    code, text = make_request('GET', endpoint=endpoint, base_url=base_url, auth=HTTPBasicAuth(VALID_USERNAME, VALID_PASSWORD))
    logging.info(f"Response [{code}]: {text}")

def get_all_students():
    endpoint = '/students/'
    logging.info("Fetching all students")
    code, text = make_request('GET', endpoint=endpoint, base_url=base_url, auth=HTTPBasicAuth(VALID_USERNAME, VALID_PASSWORD))
    logging.info(f"Response [{code}]: {text}")

def get_student_by_id():
    student_id = int(input("Enter student ID: "))
    endpoint = f'/{student_id}'
    logging.info(f"Fetching student with ID: {student_id}")
    code, text = make_request('GET', endpoint=endpoint, base_url=base_url, auth=HTTPBasicAuth(VALID_USERNAME, VALID_PASSWORD))
    logging.info(f"Response [{code}]: {text}")

def create_student():
    firstname = input("Enter your first name: ")
    lastname = input("Enter your last name: ")
    age = int(input("Enter your age: "))
    email = input("Enter your _@gmail.com Email: ")
    bio = input("Enter your Bio: ")

    payload = {
        'firstname': firstname,
        'lastname': lastname,
        'age': str(age),
        'email': email,
        'bio': bio
    }

    logging.info(f"Creating student with email: {email}")
    endpoint = '/create'
    code, text = make_request('POST', endpoint=endpoint, base_url=base_url, auth=(VALID_USERNAME, VALID_PASSWORD), payload=payload)
    logging.info(f"Response [{code}]: {text}")

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
        'age': str(age),
        'email': email,
        'bio': bio
    }

    logging.info(f"Editing student ID: {student_id}")
    endpoint = f'/{student_id}/edit'
    code, text = make_request('POST', endpoint=endpoint, base_url=base_url, auth=(VALID_USERNAME, VALID_PASSWORD), payload=payload)
    logging.info(f"Response [{code}]: {text}")

def delete_student():
    student_id = int(input("Enter the ID of the student to delete: "))
    logging.info(f"Deleting student ID: {student_id}")
    endpoint = f'/{student_id}/delete'
    code, text = make_request('DELETE', endpoint=endpoint, base_url=base_url, auth=(VALID_USERNAME, VALID_PASSWORD))
    logging.info(f"Response [{code}]: {text}")

if __name__ == "__main__":
    get_base_endpoint()
    get_hello_endpoint()
    get_goodbye_endpoint()
    get_all_students()
    get_student_by_id()
    create_student()
    edit_student()
    delete_student()
