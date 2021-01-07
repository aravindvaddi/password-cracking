# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
from flask import jsonify
from hashlib import sha256

salt = '000000000000000000000000000078d2'.encode('utf-8')

hashed_password = '18821d89de11ab18488fdc0a01f1ddf4d290e198b0f80cd4974fc031dc2615a3'

def get_hash(salt, password):
    hasher = sha256()
    hasher.update(salt)
    hasher.update(password.encode('utf-8'))
    return hasher.hexdigest()

# create the application object
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        password = get_hash(salt, request.form['password'])
        if request.form['username'] != 'admin' or password != hashed_password:
            authorised = 'Denied'
        else:
            authorised = 'Granted'
        return jsonify(authorised)
    else:
        return render_template('index.html')

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run()
