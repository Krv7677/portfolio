from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/<string:page_name>")
def htmlpage(page_name):
    return render_template(page_name)

# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#       name = data["name"]
#       email = data["email"]
#       contact = data["contact"]
#       message = data["message"]
#       file=database.write(f'\n{name},{email},{contact},{message}')


def write_to_file(data):
    with open('database.csv', mode='a') as database2:
      name = data["name"]
      email = data["email"]
      contact = data["contact"]
      message = data["message"]
      csv_writer = csv.writer(database2, delimiter=',',
                                quotechar ='"', quoting=csv.QUOTE_MINIMAL)
      csv_writer.writerow([name,email,contact,message])


@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():

      if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('/thankyou.html')
      else:
        return 'something went wrong'


