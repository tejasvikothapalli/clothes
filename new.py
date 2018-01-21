from flask import Flask, render_template, request
from werkzeug import secure_filename
import datetime
import calendar
app = Flask(__name__)

	
@app.route('/')
def main():
    return "Server works"
		
if __name__ == '__main__':
   app.run(debug = True)
