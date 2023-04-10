from flask import Flask, render_template, request, redirect, send_file, url_for, abort
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import pymysql
import re
import datetime
# (Note)
# JWT is not implemented correctly. I'm just leaving this in here for now. 
# Feel free to remove any of the unnecessary JWT items
# (New) Importing flask_jwt_extended for JWT authentication
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required, JWTManager, set_access_cookies, set_refresh_cookies

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# (New) setting up some configs for the flask_jwt_extended
# app.config['JWT_TOKEN_LOCATION'] = ['headers', 'query_string']
app.config['JWT_SECRET_KEY'] = 'midtermproject'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
jwt = JWTManager(app)

# (New) Setting up some configs the file upload 
# Path should be working but it not. Below is a template you can use to configure
# app.config['UPLOAD_FOLDER'] = '/Users/phuocnguyen/Desktop/449_MidtermProject/files'
app.config['UPLOAD_FOLDER'] = os.getcwd() + '/files'
app.config['MAX_CONTENT_SIZE'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif', '.txt', '.pdf']

# Establishing the connection to the MYSQL server
conn = pymysql.connect(
        host='localhost', 
        user='root', 
        password='1234567890',
        db='449_Midterm',
        cursorclass=pymysql.cursors.DictCursor
        )
cur = conn.cursor()

''' /register
    Allows user to register with a username and password that would be saved in the database
    The user's username can only contain english letters and numbers
'''
@app.route('/')
@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        print('In Register')
        username = request.form['username']
        password = request.form['password']
        cur.execute('SELECT * FROM accounts WHERE username= % s', (username))
        account = cur.fetchone()
        print(account)
        conn.commit()
        # Error Checking
        if account:
            msg = 'Account already exists'
        # Use regular expression to ensure only English letters and numbers are allowed
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username is not valid. Please use only english letters and numbers!'
        else:
            cur.execute('INSERT INTO accounts VALUES (NULL, % s, % s)', (username, password))
            conn.commit()
            print('Inserted into database')
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    
    return render_template('register.html', msg = msg)

''' /login
    If the user is registered, they should be able to login and be directed to the upload page.
    The user there would be able to upload files into a public viewing area.
    The upload page should be protected by a JWT token.
'''
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cur.execute('SELECT * FROM accounts WHERE username = % s and password = % s', (username, password))
        conn.commit()
        account = cur.fetchone()

        # If successfully logged in, create an access token
        if account:
            # access_token = create_access_token(identity=username)
            msg = ''
            return redirect(url_for('upload'))
        else:
            msg = 'Incorrect username or password!'
         
    return render_template('login.html', msg = msg)

''' /upload
    A protected page only accesible through authentication through JWT tokens.
    Here the user is able to upload 5 different kind of files.
    ['.jpg', '.png', '.gif', '.txt', '.pdf']
'''
@app.route('/upload', methods=['GET', 'POST'])
# @jwt_required()
def upload():
    msg = ''
    if request.method == 'POST':
        if 'file' not in request.files:
            print('Here')
            msg = 'Failed to upload'
        uploaded_file = request.files['file']
        print(uploaded_file)
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            print('Not in configured extensions')
            msg = 'File type not accepted'
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print("Uploaded file")
        msg = 'Uploaded file successfully'
    return render_template('upload.html', msg=msg)

''' /uploaded 
    A public page where users are able too view uploaded files.
    The user would be directed to the corresponding page.
'''
@app.route('/uploaded', defaults={'req_path': ''})
@app.route('/<path:req_path>')
def viewFiles(req_path):
    # This first line neeeds to be here as sometimes the page would just not load without it
    absolute_path = os.path.join(app.config['UPLOAD_FOLDER'], req_path)
    
    # Splits at '/' to get the wanted file name
    path = req_path.split('/')
    
    # If path is successfully split, create the correct path
    if (len(path) > 1):
        absolute_path = os.path.join(app.config['UPLOAD_FOLDER'], path[1])

    # This indicates a file that does not exist
    if not os.path.exists(absolute_path):
        print('In abort', absolute_path)
        return abort(404)
    
    # Found the file
    if os.path.isfile(absolute_path):
        print('In send file', absolute_path)
        return send_file(absolute_path)

    # Prints all the given files for user to choose from                             
    files = os.listdir(absolute_path)
    print(files)
    return render_template('view.html', files=files)


# Error handler for 400 Bad Request
@app.errorhandler(400)
def bad_request(error):
    return {'Message': 'Bad Request.'}, 400

# Error handler for 401 Unauthorized
@app.errorhandler(401)
def unauthorized(error):
    return {'Message': 'Unauthorized.'}, 401

#Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return {'Message': 'The requested page does not exist.'}, 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(error):
    return {'Message': 'Internal Server Error.'}, 500

if __name__ == "__main__":
	app.run(host ="localhost", port = int("5000"), debug=True)