import re

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

def is_valid(email):
    return EMAIL_REGEX.match(email)