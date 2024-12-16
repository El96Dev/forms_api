from database import collection


async def get_matching_form_name(form: dict) -> str | None:
    cursor = collection.find({})
    async for document in cursor:
        fits_form = True
        for key, value in document.items():
            if key == "_id" or key == "name":
                continue
            elif (key in form and form[key] != value) or (key not in form):
                fits_form = False
                break
        if fits_form:     
            return document["name"]

async def add_forms():
    order_form = {
        "name": "Order form", 
        "user_email": "email", 
        "user_phone": "phone", 
        "order_date": "date", 
        "notes": "text"
    }
    employee_form = {
        "name": "Employee form",
        "firstname": "text",
        "lastname": "text",
        "employee_email": "email",
        "employee_phone": "phone"
    }
    store_form = {
        "name": "Store form",
        "address": "text",
        "store_phone": "phone",
        "store_email": "email"
    }
    await collection.insert_many([order_form, employee_form, store_form])