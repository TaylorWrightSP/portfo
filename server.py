from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def main_route():
    return render_template('index.html')

@app.route('/<string:page_name>')
def dynamic_route(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('database2.csv', newline="", mode="a") as databasecsv:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(databasecsv, delimiter=",", quotechar=" ", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thanks.html')
        except:
            return "Unable to save values to database."
    else:
        return 'Something went wrong.'