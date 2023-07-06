import pyrebase

config = {
    "apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": "",
    "appId": "",
    "measurementId": ""
} 

firebase = pyrebase.initialize_app(config)

db = firebase.database()

from flask import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def basic():
    if request.method == 'POST':
        if request.form['submit'] == 'add':
            email = request.form['email']
            password = request.form['password']
            
            data = {
                'email': email,
                'password': password
            }
            
            db.child("users").push(data)
            
            return render_template('index_test.html')
        
    return render_template('index_test.html')

if __name__ == '__main__':
    app.run(debug = True)

