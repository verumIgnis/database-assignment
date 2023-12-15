import re
import sqlite3

def exhibition(formData):
    try:
        if formData["input1"] == "" or formData["input2"] == "" or formData["input3"] == "" or formData["input4"] == "" or formData["input5"] == "":
            return "All fields must be completed."
        if int(formData["input1"]) > 10 or int(formData["input1"]) < 3:
            return "An exhibition must be between 3 and 10 days long."
    except Exception as e:
        return e

def artist(formData):
    try:
        if formData["input1"] == "" or formData["input2"] == "":
            return "All fields must be completed."
        if not re.match("^[A-Z]{1}$", formData["input2"]):
            return "Artist initial must be a single uppercase character."
    except Exception as e:
        return e

def gallery(formData):
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT galleryTypeID FROM galleryTypeTable')
        rows = cursor.fetchall()
        conn.close()
        print(rows)
        if formData["input1"] == "" or formData["input2"] == "":
            return "All fields must be completed."
        if formData["input1"] not in rows:
            return "Invalid Gallery Type"
    except Exception as e:
        return e

def galleryType(formData):
    try:
        if formData["input1"] == "":
            return "All fields must be completed."
    except Exception as e:
        return e