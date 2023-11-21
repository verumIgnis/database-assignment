import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('pages/index.html')

@app.route('/testform1', methods=['GET', 'POST'])
def testform():
    if request.method == 'POST':
        input1 = request.form['input1']
        input2 = request.form['input2']

        concatenated = f"{input1} {input2}"

        return concatenated

    return render_template('testform1.html')

if __name__ == '__main__':
    app.run(debug=True)



#conn = sqlite3.connect('database.db')
#cursor = conn.cursor()
#cursor.execute('CREATE TABLE IF NOT EXISTS salesTable (saleID INTEGER PRIMARY KEY, saleDate TEXT, saleAmount REAL)')
#conn.commit()
#conn.close()