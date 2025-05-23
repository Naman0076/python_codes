import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth
from request_methods import make_request


base_url = 'http://127.0.0.1:8000' 
load_dotenv()
VALID_USERNAME = os.getenv("username")
VALID_PASSWORD = os.getenv("password1")
def get_base_endpoint():
    endpoint = '/'
    code, text = make_request('GET',endpoint=endpoint, base_url=base_url, auth=HTTPBasicAuth(VALID_USERNAME, VALID_PASSWORD))

def get_hello_endpoint():
    endpoint = '/hello'
    code, text = make_request('GET',endpoint=endpoint, base_url=base_url, auth=HTTPBasicAuth(VALID_USERNAME, VALID_PASSWORD))

def get_goodbye_endpoint():
    endpoint = '/goodbye'
    code, text = make_request('GET',endpoint=endpoint, base_url=base_url, auth=HTTPBasicAuth(VALID_USERNAME, VALID_PASSWORD))

def get_all_students():
    endpoint = '/students/'
    code, text = make_request('GET',endpoint=endpoint, base_url=base_url, auth=HTTPBasicAuth(VALID_USERNAME, VALID_PASSWORD))

def get_student_by_id():
    student_id = int(input("Enter student ID: "))
    endpoint = f'/{student_id}'
    code, text = make_request('GET',endpoint=endpoint, base_url=base_url, auth=HTTPBasicAuth(VALID_USERNAME, VALID_PASSWORD))

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

    endpoint = '/create'
    code, text = make_request('POST',endpoint=endpoint, base_url=base_url, auth=(VALID_USERNAME, VALID_PASSWORD), payload=payload)

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

    endpoint = f'/{student_id}/edit'
    code, text = make_request('POST',endpoint=endpoint, base_url=base_url, auth=(VALID_USERNAME, VALID_PASSWORD), payload=payload)

def delete_student():
    student_id = int(input("Enter the ID of the student to delete: "))
    endpoint = f'/{student_id}/delete'
    code, text = make_request('DELETE',endpoint=endpoint, base_url=base_url, auth=(VALID_USERNAME, VALID_PASSWORD))

if __name__ == "__main__":
    get_base_endpoint()
    get_hello_endpoint()
    get_goodbye_endpoint()
    get_all_students()
    get_student_by_id()
    create_student()
    edit_student()
    delete_student()