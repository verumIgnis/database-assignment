import sqlite3
import validation
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

with open("queries/exhibitions.sql", "r") as file:
    exhibitionsQuery = file.read()

with open("queries/revenue.sql", "r") as file:
    revenueQuery = file.read()

@app.route('/')
def index():
    return render_template('index.html')

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
            cursor.execute('DELETE FROM artustTable WHERE artistID = :input1', formData)
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
            validated = validation.exhibition(formData)
            if validated is None:
                conn = sqlite3.connect('database.db')
                cursor = conn.cursor()
                cursor.execute('INSERT INTO exhibitionTable (numDays, artistID, galleryID, startDate, predictedSales) VALUES (:input1, :input2, :input3, :input4, :input5)', formData)
                conn.commit()
                conn.close()
                return "Success."
            else:
                return validated
        except Exception as e:
            return f"Error: {e}"
    return render_template('editexh.html')

@app.route('/editart', methods=['GET', 'POST'])
def editart():
    if request.method == "POST":
        try:
            formData = request.form
            validated = validation.artist(formData)
            if validated is None:
                conn = sqlite3.connect('database.db')
                cursor = conn.cursor()
                cursor.execute('INSERT INTO artistTable (artistSurname, artistInitial) VALUES (:input1, :input2)', formData)
                conn.commit()
                conn.close()
                return "Success."
            else:
                return validated
        except Exception as e:
            return f"Error: {e}"
    return render_template('editart.html')

@app.route('/editgal', methods=['GET', 'POST'])
def editgal():
    if request.method == "POST":
        try:
            formData = request.form
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
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO galleryTypeTable (galleryType) VALUES (:input1)', formData)
            conn.commit()
            conn.close()
            return "Success."
        except Exception as e:
            return f"Error: {e}"
    return render_template('edittyp.html')

@app.route('/testform1', methods=['GET', 'POST'])
def testform():
    if request.method == 'POST':
        input1 = request.form['input1']
        input2 = request.form['input2']

        concatenated = f"{input1} {input2}"

        return concatenated

    return render_template('testform1.html')

@app.route('/<path:filename>')
def webroot(filename):
    return send_from_directory("webroot", filename)

if __name__ == '__main__':
    app.run(debug=True)
