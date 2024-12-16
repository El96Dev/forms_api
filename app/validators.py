import re


def is_valid_date(text: str) -> bool:
    pattern = r'^(?:(?:0[1-9]|[12][0-9]|3[01])\.(?:0[1-9]|1[0-2])\.\d{4}|' \
              r'\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01]))$'
    return re.match(pattern, text)

def is_valid_phone(text: str) -> bool:
    pattern = r'^\+7 \d{3} \d{3} \d{2} \d{2}$'
    return re.match(pattern, text)
        
def is_valid_email(text: str) -> bool:
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, text)