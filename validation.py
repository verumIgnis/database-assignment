import re

def exhibition(formData):
    try:
        if int(formData["input1"]) > 10 or int(formData["input1"]) < 3:
            return "An exhibition must be between 3 and 10 days long."
    except Exception as e:
        return e

def artist(formData):
    try:
        if not re.match("^[A-Z]{1}$", formData["input2"]):
            return "Artist initial must be a single uppercase character."
    except Exception as e:
        return e