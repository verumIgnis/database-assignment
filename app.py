import sqlite3
import validation
from flask import Flask, render_template, request, send_from_directory
from datetime import datetime, timedelta
import json

app = Flask(__name__)

with open("queries/exhibitions.sql", "r") as file:
    exhibitionsQuery = file.read()

with open("queries/revenue.sql", "r") as file:
    revenueQuery = file.read()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rptexh', methods=['GET'])
def rptexh():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(exhibitionsQuery)
    rowsTuple = cursor.fetchall()
    rows = [list(row) for row in rowsTuple]
    conn.close()
    for row in rows:
        parsedDate = datetime.strptime(row[3], "%Y-%m-%d")
        row[4] = parsedDate + timedelta(days=row[2])
        row[4] = str(str(row[4])[:-9])
    return render_template('rptexh.html', exhibitions=rows)

@app.route('/rptrev', methods=['GET', 'POST'])
def rptrev():
    if request.method == "POST":
        try:
            formData = request.form
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute(revenueQuery, formData)
            rowsTuple = cursor.fetchall()
            rows = [list(row) for row in rowsTuple]
            conn.close()
            for row in rows:
                row[3] = "{:.2f}".format(row[3])
            return render_template('rsprev.html', rows=rows)
        except Exception as e:
            return f"Error: {e}"
    return render_template('rptrev.html')

@app.route('/viewexh', methods=['GET', 'POST'])
def viewexh():
    if request.method == "POST":
        try:
            formData = request.form
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute('DELETE FROM exhibitionTable WHERE exhibitionID = :input1', formData)
            conn.commit()
            conn.close()
            return "Success."
        except Exception as e:
            return f"Error: {e}"
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM exhibitionTable')
    rows = cursor.fetchall()
    conn.close()
    return render_template('viewexh.html', exhibitions=rows)

@app.route('/viewart', methods=['GET', 'POST'])
def viewart():
    if request.method == "POST":
        try:
            formData = request.form
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute('DELETE FROM artistTable WHERE artistID = :input1', formData)
            conn.commit()
            conn.close()
            return "Success."
        except Exception as e:
            return f"Error: {e}"
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM artistTable')
    rows = cursor.fetchall()
    conn.close()
    return render_template('viewart.html', artists=rows)

@app.route('/viewgal', methods=['GET', 'POST'])
def viewgal():
    if request.method == "POST":
        try:
            formData = request.form
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute('DELETE FROM galleryTable WHERE galleryID = :input1', formData)
            conn.commit()
            conn.close()
            return "Success."
        except Exception as e:
            return f"Error: {e}"
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM galleryTable')
    rows = cursor.fetchall()
    conn.close()
    return render_template('viewgal.html', galleries=rows)

@app.route('/viewtyp', methods=['GET', 'POST'])
def viewtyp():
    if request.method == "POST":
        try:
            formData = request.form
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute('DELETE FROM galleryTypeTable WHERE galleryTypeID = :input1', formData)
            conn.commit()
            conn.close()
            return "Success."
        except Exception as e:
            return f"Error: {e}"
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM galleryTypeTable')
    rows = cursor.fetchall()
    conn.close()
    return render_template('viewtyp.html', galleryTypes=rows)



@app.route('/editexh', methods=['GET', 'POST'])
def editexh():
    if request.method == "POST":
        try:
            formData = request.form
            if formData["input1"] == "" or formData["input2"] == "" or formData["input3"] == "" or formData[
                "input4"] == "" or formData["input5"] == "":
                return "All fields must be completed."
            if int(formData["input1"]) > 10 or int(formData["input1"]) < 3:
                return "An exhibition must be between 3 and 10 days long."
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute('SELECT artistID FROM artistTable')
            rows = cursor.fetchall()
            conn.close()
            valid = False
            for row in rows:
                if str(formData["input2"]) == str(row[0]):
                    valid = True
            if not valid:
                return "Invalid Artist"
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO exhibitionTable (numDays, artistID, galleryID, startDate, predictedSales) VALUES (:input1, :input2, :input3, :input4, :input5)', formData)
            conn.commit()
            conn.close()
            return "Success."
        except Exception as e:
            return f"Error: {e}"
    return render_template('editexh.html')

@app.route('/editart', methods=['GET', 'POST'])
def editart():
    if request.method == "POST":
        try:
            formData = request.form
            if formData["input1"] == "" or formData["input2"] == "":
                return "All fields must be completed."
            if not re.match("^[A-Z]{1}$", formData["input2"]):
                return "Artist initial must be a single uppercase character."
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO artistTable (artistSurname, artistInitial) VALUES (:input1, :input2)', formData)
            conn.commit()
            conn.close()
            return "Success."
        except Exception as e:
            return f"Error: {e}"
    return render_template('editart.html')

@app.route('/editgal', methods=['GET', 'POST'])
def editgal():
    if request.method == "POST":
        try:
            formData = request.form
            if formData["input1"] == "" or formData["input2"] == "":
                return "All fields must be completed."
            valid = False
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute('SELECT galleryTypeID FROM galleryTypeTable')
            rows = cursor.fetchall()
            conn.close()
            for row in rows:
                if str(formData["input2"]) == str(row[0]):
                    valid = True
            if not valid:
                return "Invalid Gallery Type"
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO galleryTable (galleryName, galleryTypeID) VALUES (:input1, :input2)', formData)
            conn.commit()
            conn.close()
            return "Success."
        except Exception as e:
            return f"Error: {e}"
    return render_template('editgal.html')

@app.route('/edittyp', methods=['GET', 'POST'])
def edittyp():
    if request.method == "POST":
        try:
            formData = request.form
            if formData["input1"] == "":
                return "All fields must be completed."
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO galleryTypeTable (galleryType) VALUES (:input1)', formData)
            conn.commit()
            conn.close()
            return "Success."
        except Exception as e:
            return f"Error: {e}"
    return render_template('edittyp.html')


@app.route('/<path:filename>')
def webroot(filename):
    return send_from_directory("webroot", filename)

if __name__ == '__main__':
    app.run(debug=True)
