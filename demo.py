import os
import time
import json
from deepomatic import deepomatic
from pprint import pprint
import requests
import datetime
from threadgenius import ThreadGenius
from threadgenius.types import ImageUrlInput
from threadgenius.types import ImageFileInput
import base64
import json
import requests
from pprint import pprint
from base64 import b64encode
import itertools
import operator
import collections
from flask import Flask, render_template, request
import webcolors



import numpy as np
# import cv2
#from twython import Twython
import json
import csv
import random

from datetime import datetime

from pymongo import MongoClient
client = MongoClient('127.0.0.1:27017')
db = client.clothing
tops = db.tops
bottoms = db.bottoms
shoes = db.shoes
app = Flask(__name__)
@app.route('/createoutfit', methods = ['GET', 'POST'])
@app.route('/createoutfit', methods = ['GET', 'POST'])
def getAllTops():
	topsauce = []
	for stuff in db.tops.find():
		topsauce.append(stuff)
	return topsauce	
@app.route('/createoutfit', methods = ['GET', 'POST'])
def getAllBottoms():
	bottomsauce = []
	for stuff in db.bottoms.find():
		bottomsauce.append(stuff)
	return bottomsauce	
@app.route('/createoutfit', methods = ['GET', 'POST'])
def getAllShoes():
	shoesauce = []
	for stuff in db.shoes.find():
		shoesauce.append(stuff)
	return shoesauce	
if __name__ == '__main__':
   app.run(debug = True)




	

# creatOutfit()
