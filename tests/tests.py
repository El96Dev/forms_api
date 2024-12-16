import requests


def test_nonexistent_form():
    body = {
        "country": "USA", 
        "city": "Chicago", 
        "date": "10.11.2020", 
        "email": "example@gmail.com",
        "phone": "+7 909 900 20 20"
    }
    response = requests.post("http://0.0.0.0:8000/get_form", json=body)
    assert response.status_code == 200
    assert response.json() == {
        "country": "text", 
        "city": "text", 
        "date": "date", 
        "email": "email",
        "phone": "phone"
    }

# Test order form

def test_order_form():
    body = {
        "name": "Some name", 
        "user_email": "example@gmail.com", 
        "user_phone": "+7 202 200 30 30", 
        "order_date": "01.01.2024", 
        "notes": "Some notes"
    }
    response = requests.post("http://0.0.0.0:8000/get_form", json=body)
    assert response.status_code == 200
    assert response.json() == "Order form"

def test_order_form_incorrect_phone():
    body = {
        "name": "Some name", 
        "user_email": "example@gmail.com", 
        "user_phone": "+8 202 200 3030", 
        "order_date": "01.01.2024", 
        "notes": "Some notes"
    }
    response = requests.post("http://0.0.0.0:8000/get_form", json=body)
    assert response.status_code == 200
    assert response.json() == {
        "name": "text", 
        "user_email": "email", 
        "user_phone": "text", 
        "order_date": "date", 
        "notes": "text"
    }

def test_order_form_incorrect_email():
    body = {
        "name": "Some name", 
        "user_email": "examplegmail.com", 
        "user_phone": "+7 202 200 30 30", 
        "order_date": "01.01.2024", 
        "notes": "Some notes"
    }
    response = requests.post("http://0.0.0.0:8000/get_form", json=body)
    assert response.status_code == 200
    assert response.json() == {
        "name": "text", 
        "user_email": "text", 
        "user_phone": "phone", 
        "order_date": "date", 
        "notes": "text"
    }

def test_order_form_incorrect_date():
    body = {
        "name": "Some name", 
        "user_email": "example@gmail.com", 
        "user_phone": "+7 202 200 30 30", 
        "order_date": "15 15 2024", 
        "notes": "Some notes"
    }
    response = requests.post("http://0.0.0.0:8000/get_form", json=body)
    assert response.status_code == 200
    assert response.json() == {
        "name": "text", 
        "user_email": "email", 
        "user_phone": "phone", 
        "order_date": "text", 
        "notes": "text"
    }

def test_order_form_incorrect_fieldnames():
    body = {
        "name": "Some name", 
        "email": "example@gmail.com", 
        "phone": "+7 202 200 30 30", 
        "orderdate": "11.12.2024", 
        "notes": "Some notes"
    }
    response = requests.post("http://0.0.0.0:8000/get_form", json=body)
    assert response.status_code == 200
    assert response.json() == {
        "name": "text", 
        "email": "email", 
        "phone": "phone", 
        "orderdate": "date", 
        "notes": "text"
    }

def test_order_form_missing_fields():
    body = {
        "name": "Some name", 
        "user_email": "example@gmail.com", 
        "order_date": "01.01.2024", 
        "notes": "Some notes"
    }
    response = requests.post("http://0.0.0.0:8000/get_form", json=body)
    assert response.status_code == 200
    assert response.json() == {
        "name": "text", 
        "user_email": "email", 
        "order_date": "date", 
        "notes": "text"
    }

# Test employee form

def test_employee_form():
    body = {
        "name": "Some name",
        "firstname": "text",
        "lastname": "text",
        "employee_email": "example@gmail.com",
        "employee_phone": "+7 909 100 20 30"
    }
    response = requests.post("http://0.0.0.0:8000/get_form", json=body)
    assert response.status_code == 200
    assert response.json() == "Employee form"

def test_employee_form_incorrect_phone():
    body = {
        "name": "Some name",
        "firstname": "text",
        "lastname": "text",
        "employee_email": "example@gmail.com",
        "employee_phone": "7 909 100 20 30"
    }
    response = requests.post("http://0.0.0.0:8000/get_form", json=body)
    assert response.status_code == 200
    assert response.json() == {
        "name": "text",
        "firstname": "text",
        "lastname": "text",
        "employee_email": "email",
        "employee_phone": "text"
    }

def test_employee_form_incorrect_email():
    body = {
        "name": "Some name",
        "firstname": "text",
        "lastname": "text",
        "employee_email": "examplegmail.com",
        "employee_phone": "+7 909 100 20 30"
    }
    response = requests.post("http://0.0.0.0:8000/get_form", json=body)
    assert response.status_code == 200
    assert response.json() == {
        "name": "text",
        "firstname": "text",
        "lastname": "text",
        "employee_email": "text",
        "employee_phone": "phone"
    }

def test_employee_form_incorrect_fieldnames():
    body = {
        "name": "Some name",
        "first_name": "text",
        "last_name": "text",
        "email": "example@gmail.com",
        "employee_phone": "+7 909 100 20 30"
    }
    response = requests.post("http://0.0.0.0:8000/get_form", json=body)
    assert response.status_code == 200
    assert response.json() == {
        "name": "text",
        "first_name": "text",
        "last_name": "text",
        "email": "email",
        "employee_phone": "phone"
    }

def test_employee_form_missing_fields():
    body = {
        "name": "Some name",
        "lastname": "text",
        "employee_email": "example@gmail.com",
    }
    response = requests.post("http://0.0.0.0:8000/get_form", json=body)
    assert response.status_code == 200
    assert response.json() == {
        "name": "text",
        "lastname": "text",
        "employee_email": "email",
    }

# Test store form

def test_store_form():
    body = {
        "name": "Store name",
        "address": "Example st., 29",
        "store_phone": "+7 100 300 40 50",
        "store_email": "example@gmail.com"
    }
    response = requests.post("http://0.0.0.0:8000/get_form", json=body)
    assert response.status_code == 200
    assert response.json() == "Store form"

def test_store_form_incorrect_phone():
    body = {
        "name": "Store name",
        "address": "Example st., 29",
        "store_phone": "+7100 30040 50",
        "store_email": "example@gmail.com"
    }
    response = requests.post("http://0.0.0.0:8000/get_form", json=body)
    assert response.status_code == 200
    assert response.json() == {
        "name": "text",
        "address": "text",
        "store_phone": "text",
        "store_email": "email"
    }

def test_store_form_incorrect_email():
    body = {
        "name": "Store name",
        "address": "Example st., 29",
        "store_phone": "+7 100 300 40 50",
        "store_email": "examplegmail.com"
    }
    response = requests.post("http://0.0.0.0:8000/get_form", json=body)
    assert response.status_code == 200
    assert response.json() == {
        "name": "text",
        "address": "text",
        "store_phone": "phone",
        "store_email": "text"
    }

def test_store_form_missing_fields():
    body = {
        "store_phone": "+7 100 300 40 50",
    }
    response = requests.post("http://0.0.0.0:8000/get_form", json=body)
    assert response.status_code == 200
    assert response.json() == {
        "store_phone": "phone",
    }

def test_store_form_incorrect_fieldnames():
    body = {
        "name": "Store name",
        "address": "Example st., 29",
        "phone": "+7 100 300 40 50",
        "email": "example@gmail.com"
    }
    response = requests.post("http://0.0.0.0:8000/get_form", json=body)
    assert response.status_code == 200
    assert response.json() == {
        "name": "text",
        "address": "text",
        "phone": "phone",
        "email": "email"
    }