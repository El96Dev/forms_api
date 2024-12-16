from fastapi import APIRouter, Body

from validators import is_valid_date, is_valid_email, is_valid_phone
from crud import get_matching_form_name


router = APIRouter()

@router.post("/get_form")
async def get_form(json_data: dict[str, str]=Body(...)):
    typed_data = dict()
    for key, value in json_data.items():
        if is_valid_date(value):
            typed_data[key] = "date"
        elif is_valid_phone(value):
            typed_data[key] = "phone"
        elif is_valid_email(value):
            typed_data[key] = "email"
        else:
            typed_data[key] = "text"
    form_name = await get_matching_form_name(typed_data)
    if form_name is not None:
        return form_name
    else:
        return typed_data
    
