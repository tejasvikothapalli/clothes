import os
import sys
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
import webcolors
from flask import Flask, render_template, request, jsonify



import numpy as np
# import cv2
#from twython import Twython
import json
import csv
import random


from datetime import datetime

from pymongo import MongoClient
app = Flask(__name__)
client = MongoClient('127.0.0.1:27017')
db = client.clothing
tops = db.tops
bottoms = db.bottoms
shoes = db.shoes
# model = model.clothing


modelData = [{"link":"http://54.200.230.168/images%20(12).jpg","top-shirt":"white","shoe":"brown","pants":"light blue"},{"link":"http://54.200.230.168/images%20(86).jpg","top-shirt":"charcoal","shoe":"grey","pants":"charcoal"},{"link":"http://54.200.230.168/images%20(60).jpg","top-shirt":"military green","shoe":"","pants":"charcoal"},{"link":"http://54.200.230.168/images%20(63).jpg","top-shirt":"grey","shoe":"camel","pants":"brown"},{"link":"http://54.200.230.168/images%20(66).jpg","top-shirt":"military green","shoe":"nude","pants":"charcoal"},{"link":"http://54.200.230.168/images%20(13).jpg","top-shirt":"blackwhite","shoe":"","pants":"heather grey"},{"link":"http://54.200.230.168/images%20(14).jpg","top-shirt":"white","shoe":"","pants":"dark wash denim"},{"link":"http://54.200.230.168/9k=%20(11).jpg","top-shirt":"light blue","shoe":"charcoal","pants":"charcoal"},{"link":"http://54.200.230.168/Z%20(2).jpg","top-shirt":"white","shoe":"","pants":"white"},{"link":"http://54.200.230.168/images%20(30).jpg","top-shirt":"navy","shoe":"","pants":"light blue"},{"link":"http://54.200.230.168/Z%20(19).jpg","top-shirt":"light blue","shoe":"silver","pants":"bright blue"},{"link":"http://54.200.230.168/images.jpg","top-shirt":"brown","shoe":"brown","pants":"white"},{"link":"http://54.200.230.168/images%20(51).jpg","top-shirt":"navy","shoe":"","pants":"beige"},{"link":"http://54.200.230.168/images%20(11).jpg","top-shirt":"charcoal","shoe":"","pants":"charcoal"},{"link":"http://54.200.230.168/9k=%20(2).jpg","top-shirt":"light blue","shoe":"silver","pants":"grey"},{"link":"http://54.200.230.168/Z%20(4).jpg","top-shirt":"navy","shoe":"bordeaux","pants":"navy"},{"link":"http://54.200.230.168/images%20(99).jpg","top-shirt":"white","shoe":"brown","pants":"grey"},{"link":"http://54.200.230.168/images%20(91).jpg","top-shirt":"white","shoe":"","pants":"light blue"},{"link":"http://54.200.230.168/images%20(48).jpg","top-shirt":"charcoal","shoe":"charcoal","pants":"charcoal"},{"link":"http://54.200.230.168/images%20(80).jpg","top-shirt":"white","shoe":"white","pants":"heather grey"},{"link":"http://54.200.230.168/images%20(59).jpg","top-shirt":"white","shoe":"black","pants":"charcoal"},{"link":"http://54.200.230.168/Z%20(7).jpg","top-shirt":"navy","shoe":"navy","pants":"light blue"},{"link":"http://54.200.230.168/images%20(89).jpg","top-shirt":"white","shoe":"","pants":"charcoal"},{"link":"http://54.200.230.168/images%20(32).jpg","top-shirt":"white","shoe":"nude","pants":"charcoal"},{"link":"http://54.200.230.168/images%20(83).jpg","top-shirt":"heather grey","shoe":"grey","pants":"military green"},{"link":"http://54.200.230.168/images%20(61).jpg","top-shirt":"white","shoe":"goldplated","pants":"charcoal"},{"link":"http://54.200.230.168/images%20(95).jpg","top-shirt":"grey","shoe":"brown","pants":"light blue"},{"link":"http://54.200.230.168/images%20(93).jpg","top-shirt":"light blue","shoe":"camel","pants":"charcoal"},{"link":"http://54.200.230.168/Z%20(12).jpg","top-shirt":"navy","shoe":"brown","pants":"white"},{"link":"http://54.200.230.168/Z%20(10).jpg","top-shirt":"charcoal","shoe":"","pants":"charcoal"},{"link":"http://54.200.230.168/images%20(6).jpg","top-shirt":"charcoal","shoe":"white","pants":"camel"},{"link":"http://54.200.230.168/images%20(43).jpg","top-shirt":"light blue","shoe":"charcoal","pants":"charcoal"},{"link":"http://54.200.230.168/images%20(84).jpg","top-shirt":"grey","shoe":"white","pants":"navy"},{"link":"http://54.200.230.168/images%20(5).jpg","top-shirt":"","shoe":"","pants":"white"},{"link":"http://54.200.230.168/images%20(45).jpg","top-shirt":"grey","shoe":"navy","pants":"light blue"},{"link":"http://54.200.230.168/images%20(76).jpg","top-shirt":"white","shoe":"white","pants":"grey"},{"link":"http://54.200.230.168/images%20(62).jpg","top-shirt":"","shoe":"","pants":"charcoal"},{"link":"http://54.200.230.168/9k=.jpg","top-shirt":"military green","shoe":"nude","pants":"charcoal"},{"link":"http://54.200.230.168/images%20(7).jpg","top-shirt":"white","shoe":"silver","pants":"navy"},{"link":"http://54.200.230.168/Z%20(18).jpg","top-shirt":"navy","shoe":"navy","pants":"light blue"},{"link":"http://54.200.230.168/images%20(31).jpg","top-shirt":"grey","shoe":"nude","pants":"charcoal"},{"link":"http://54.200.230.168/Z%20(15).jpg","top-shirt":"navy","shoe":"bordeaux","pants":"navy"},{"link":"http://54.200.230.168/images%20(21).jpg","top-shirt":"white","shoe":"","pants":"charcoal"},{"link":"http://54.200.230.168/images%20(19).jpg","top-shirt":"white","shoe":"silver","pants":"charcoal"},{"link":"http://54.200.230.168/Z%20(1).jpg","top-shirt":"navy","shoe":"brown","pants":"white"},{"link":"http://54.200.230.168/images%20(38).jpg","top-shirt":"grey","shoe":"brown","pants":"brown"},{"link":"http://54.200.230.168/2Q==%20(4).jpg","top-shirt":"light blue","shoe":"silver","pants":"charcoal"},{"link":"http://54.200.230.168/Z%20(8).jpg","top-shirt":"light blue","shoe":"silver","pants":"bright blue"},{"link":"http://54.200.230.168/images%20(82).jpg","top-shirt":"","shoe":"camel","pants":"light blue"},{"link":"http://54.200.230.168/2Q==%20(5).jpg","top-shirt":"grey","shoe":"","pants":"heather grey"},{"link":"http://54.200.230.168/images%20(94).jpg","top-shirt":"white","shoe":"","pants":"light blue"},{"link":"http://54.200.230.168/images%20(75).jpg","top-shirt":"grey","shoe":"grey","pants":"camel"},{"link":"http://54.200.230.168/images%20(56).jpg","top-shirt":"light blue","shoe":"white","pants":"grey"},{"link":"http://54.200.230.168/images%20(55).jpg","top-shirt":"navy","shoe":"silver","pants":"beige"},{"link":"http://54.200.230.168/images%20(73).jpg","top-shirt":"charcoal","shoe":"","pants":"navy"},{"link":"http://54.200.230.168/images%20(98).jpg","top-shirt":"beige","shoe":"brown","pants":"light blue"},{"link":"http://54.200.230.168/9k=%20(1).jpg","top-shirt":"white","shoe":"","pants":"light blue"},{"link":"http://54.200.230.168/images%20(74).jpg","top-shirt":"charcoal","shoe":"black","pants":"charcoal"},{"link":"http://54.200.230.168/Z%20(9).jpg","top-shirt":"white","shoe":"brown","pants":"light blue"},{"link":"http://54.200.230.168/images%20(85).jpg","top-shirt":"cream","shoe":"white","pants":"grey"},{"link":"http://54.200.230.168/images%20(28).jpg","top-shirt":"light blue","shoe":"grey","pants":"white"},{"link":"http://54.200.230.168/Z%20(5).jpg","top-shirt":"","shoe":"white","pants":"light blue"},{"link":"http://54.200.230.168/images%20(8).jpg","top-shirt":"military green","shoe":"white","pants":"charcoal"},{"link":"http://54.200.230.168/images%20(78).jpg","top-shirt":"grey","shoe":"","pants":"black"},{"link":"http://54.200.230.168/images%20(72).jpg","top-shirt":"grey","shoe":"white","pants":"light blue"},{"link":"http://54.200.230.168/images%20(77).jpg","top-shirt":"grey","shoe":"","pants":"navy"},{"link":"http://54.200.230.168/images%20(39).jpg","top-shirt":"","shoe":"","pants":"charcoal"},{"link":"http://54.200.230.168/images%20(25).jpg","top-shirt":"","shoe":"","pants":"light blue"},{"link":"http://54.200.230.168/images%20(34).jpg","top-shirt":"white","shoe":"","pants":"light green"},{"link":"http://54.200.230.168/images%20(88).jpg","top-shirt":"white","shoe":"white","pants":"light blue"},{"link":"http://54.200.230.168/images%20(90).jpg","top-shirt":"white","shoe":"silver","pants":"light blue"},{"link":"http://54.200.230.168/images%20(40).jpg","top-shirt":"navy","shoe":"brown","pants":"light blue"},{"link":"http://54.200.230.168/9k=%20(7).jpg","top-shirt":"white","shoe":"","pants":"light blue"},{"link":"http://54.200.230.168/images%20(22).jpg","top-shirt":"brown","shoe":"brown","pants":"charcoal"},{"link":"http://54.200.230.168/9k=%20(8).jpg","top-shirt":"light blue","shoe":"silver","pants":"grey"},{"link":"http://54.200.230.168/images%20(97).jpg","top-shirt":"grey","shoe":"white","pants":"charcoal"},{"link":"http://54.200.230.168/images%20(58).jpg","top-shirt":"white","shoe":"white","pants":"heather grey"},{"link":"http://54.200.230.168/Z%20(16).jpg","top-shirt":"","shoe":"white","pants":"light blue"},{"link":"http://54.200.230.168/9k=%20(9).jpg","top-shirt":"bordeaux","shoe":"","pants":"light blue"},{"link":"http://54.200.230.168/images%20(20).jpg","top-shirt":"white","shoe":"","pants":"white"},{"link":"http://54.200.230.168/Z%20(17).jpg","top-shirt":"","shoe":"silver","pants":"grey"},{"link":"http://54.200.230.168/images%20(27).jpg","top-shirt":"white","shoe":"white","pants":"coral"},{"link":"http://54.200.230.168/images%20(18).jpg","top-shirt":"bordeaux","shoe":"charcoal","pants":"charcoal"},{"link":"http://54.200.230.168/images%20(57).jpg","top-shirt":"anthracite","shoe":"","pants":"heather grey"},{"link":"http://54.200.230.168/images%20(36).jpg","top-shirt":"white","shoe":"white","pants":"charcoal"},{"link":"http://54.200.230.168/images%20(4).jpg","top-shirt":"grey","shoe":"grey","pants":"charcoal"},{"link":"http://54.200.230.168/9k=%20(10).jpg","top-shirt":"white","shoe":"brown","pants":"light blue"},{"link":"http://54.200.230.168/images%20(79).jpg","top-shirt":"military green","shoe":"nude","pants":"grey"},{"link":"http://54.200.230.168/images%20(37).jpg","top-shirt":"","shoe":"brown","pants":"charcoal"},{"link":"http://54.200.230.168/images%20(26).jpg","top-shirt":"","shoe":"","pants":"dark wash denim"},{"link":"http://54.200.230.168/Z%20(3).jpg","top-shirt":"white","shoe":"","pants":"light blue"},{"link":"http://54.200.230.168/images%20(50).jpg","top-shirt":"white","shoe":"mandarin","pants":"light blue"},{"link":"http://54.200.230.168/9k=%20(3).jpg","top-shirt":"bordeaux","shoe":"","pants":"light blue"},{"link":"http://54.200.230.168/images%20(49).jpg","top-shirt":"light blue","shoe":"","pants":"light blue"},{"link":"http://54.200.230.168/images%20(16).jpg","top-shirt":"grey","shoe":"grey","pants":"light blue"},{"link":"http://54.200.230.168/images%20(44).jpg","top-shirt":"white","shoe":"beige","pants":"beige"},{"link":"http://54.200.230.168/images%20(71).jpg","top-shirt":"white","shoe":"","pants":"beige"},{"link":"http://54.200.230.168/images%20(52).jpg","top-shirt":"white","shoe":"","pants":"white"},{"link":"http://54.200.230.168/9k=%20(4).jpg","top-shirt":"white","shoe":"brown","pants":"light blue"},{"link":"http://54.200.230.168/images%20(10).jpg","top-shirt":"","shoe":"","pants":"charcoal"},{"link":"http://54.200.230.168/Z%20(20).jpg","top-shirt":"white","shoe":"brown","pants":"light blue"},{"link":"http://54.200.230.168/2Q==.jpg","top-shirt":"military green","shoe":"silver","pants":"charcoal"},{"link":"http://54.200.230.168/images%20(1).jpg","top-shirt":"white","shoe":"brown","pants":"navy"},{"link":"http://54.200.230.168/2Q==%20(2).jpg","top-shirt":"grey","shoe":"","pants":"heather grey"},{"link":"http://54.200.230.168/images%20(53).jpg","top-shirt":"navy","shoe":"white","pants":"grey"},{"link":"http://54.200.230.168/Z%20(14).jpg","top-shirt":"white","shoe":"","pants":"light blue"},{"link":"http://54.200.230.168/images%20(65).jpg","top-shirt":"","shoe":"","pants":"navy"},{"link":"http://54.200.230.168/Z%20(11).jpg","top-shirt":"light blue","shoe":"","pants":"charcoal"},{"link":"http://54.200.230.168/images%20(87).jpg","top-shirt":"","shoe":"silver","pants":"light blue"},{"link":"http://54.200.230.168/9k=%20(5).jpg","top-shirt":"light blue","shoe":"charcoal","pants":"charcoal"},{"link":"http://54.200.230.168/images%20(100).jpg","top-shirt":"white","shoe":"charcoal","pants":"dark wash denim"},{"link":"http://54.200.230.168/images%20(96).jpg","top-shirt":"","shoe":"silver","pants":"charcoal"},{"link":"http://54.200.230.168/9k=%20(6).jpg","top-shirt":"military green","shoe":"nude","pants":"charcoal"},{"link":"http://54.200.230.168/images%20(47).jpg","top-shirt":"white","shoe":"nude","pants":"light blue"},{"link":"http://54.200.230.168/2Q==%20(3).jpg","top-shirt":"military green","shoe":"silver","pants":"charcoal"},{"link":"http://54.200.230.168/images%20(92).jpg","top-shirt":"black","shoe":"charcoal","pants":"charcoal"},{"link":"http://54.200.230.168/images%20(64).jpg","top-shirt":"grey","shoe":"","pants":"charcoal"},{"link":"http://54.200.230.168/Z%20(13).jpg","top-shirt":"white","shoe":"","pants":"white"},{"link":"http://54.200.230.168/images%20(35).jpg","top-shirt":"","shoe":"brown","pants":"beige"},{"link":"http://54.200.230.168/images%20(2).jpg","top-shirt":"","shoe":"white","pants":"grey"},{"link":"http://54.200.230.168/images%20(23).jpg","top-shirt":"white","shoe":"white","pants":"charcoal"},{"link":"http://54.200.230.168/Z%20(21).jpg","top-shirt":"charcoal","shoe":"","pants":"charcoal"},{"link":"http://54.200.230.168/images%20(70).jpg","top-shirt":"white","shoe":"white","pants":"light blue"},{"link":"http://54.200.230.168/Z%20(6).jpg","top-shirt":"","shoe":"silver","pants":"grey"},{"link":"http://54.200.230.168/2Q==%20(1).jpg","top-shirt":"light blue","shoe":"silver","pants":"charcoal"},{"link":"http://54.200.230.168/images%20(68).jpg","top-shirt":"grey","shoe":"brown","pants":"charcoal"},{"link":"http://54.200.230.168/images%20(9).jpg","top-shirt":"","shoe":"","pants":"navy"},{"link":"http://54.200.230.168/images%20(54).jpg","top-shirt":"charcoal","shoe":"","pants":"grey"},{"link":"http://54.200.230.168/images%20(81).jpg","top-shirt":"","shoe":"silver","pants":"light blue"},{"link":"http://54.200.230.168/images%20(24).jpg","top-shirt":"charcoal","shoe":"brown","pants":"grey"},{"link":"http://54.200.230.168/images%20(33).jpg","top-shirt":"white","shoe":"","pants":"grey"},{"link":"http://54.200.230.168/images%20(69).jpg","top-shirt":"white","shoe":"","pants":"purple"},{"link":"http://54.200.230.168/images%20(42).jpg","top-shirt":"white","shoe":"white","pants":"light blue"}]

appID  = '227318977946'
apiKey = 'c4c34cb598804f448cd60bf44657d83c'

client = deepomatic.Client(appID, apiKey)

# ---------------------------------------------------------------------------------------------------
# For the sake of reproducibility, we always wait for the tasks to complete via a check on the taskID
# ---------------------------------------------------------------------------------------------------

@app.route('/')
def main():
    return "Server works"

def db_and_indexing(db_name_1, db_name_2) :

	print("--------------------------------------------------------------------------------------------")
	print("--------- DBs and indexing")
	print("--------------------------------------------------------------------------------------------")

	# Delete the dbs if they exists for reproductibily
	print("DELETE db %s if it exists." % db_name_1)
	if db_name_1 in client.getDBs()['dbs'] :
		client.deleteDB(db_name_1, wait = True)

	print("DELETE db %s if it exists." % db_name_2)
	if db_name_2 in client.getDBs()['dbs'] :
		client.deleteDB(db_name_2, wait = True)


	# POST an image into the db. An id is automatically created and returned.
	# A task id is also returned to track the completion of the task
	print("POST a new entry in %s with an auto-assigned id." % db_name_1)
	img = [{"url": "https://s3-eu-west-1.amazonaws.com/deepo-public/Demo/shoes/shoes_0.jpg"}]
	client.saveObject(db_name_1, imgs = img, wait = True)

	# PUT an image into the db with a defined id.
	# A task id is returned to track the completion of the task
	print("PUT a new entry in %s with a predefined id." % db_name_1)
	img = [{"url": "https://s3-eu-west-1.amazonaws.com/deepo-public/Demo/shoes/shoes_1.jpg"}]
	predefined_id = "shoes_1"
	client.saveObject(db_name_1, id = predefined_id, imgs = img, wait = True)

	print("POST a new entry in %s with an auto-assigned id." % db_name_2)

	bbox = deepomatic.Bbox(deepomatic.Point(0,0), deepomatic.Point(1,1))
	poly = deepomatic.Polygon()
	poly.addPoints([deepomatic.Point(0,0), deepomatic.Point(1,1), deepomatic.Point(0,1), deepomatic.Point(1,0)])
	obj = deepomatic.ImgsSend("url", "https://s3-eu-west-1.amazonaws.com/deepo-public/Demo/shoes/shoes_2.jpg", bbox = bbox.corners, polygon = poly.points)
	client.saveObject(db_name_2, imgs = obj.imgs, wait = True)

	print("DBs are %s." % ", ".join(client.getDBs()['dbs']))

	print("CLEAR db %s." % db_name_2)
	client.clearDB(db_name_2, wait = True)

	print("DBs are now %s." % ", ".join(client.getDBs()["dbs"]))

	print("DELETE db %s." % db_name_2)
	delete_task_3 = client.deleteDB(db_name_2, wait = True)

	print("DBs are now just %s." % ", ".join(client.getDBs()["dbs"]))

	print("DB %s has %s element." % (db_name_1, str(client.getCount(db_name_1)["count"])))

	print("GET object with id %s in db %s." % (predefined_id, db_name_1))
	get_result_box = client.getObject(db_name_1, predefined_id)['object']['imgs'][0]['bbox']
	print("Indexation has automatically cropped background color to {xmin: %.3f, ymin: %.3f, xmax: %.3f, ymax: %.3f}" % (get_result_box['xmin'], get_result_box['ymin'], get_result_box['xmax'], get_result_box['ymax']))

	print("DELETE object with id %s in db %s." % (predefined_id, db_name_1))
	object_delete = client.deleteObject(db_name_1, predefined_id, wait = True)

	print("DB %s has now %s element." % (db_name_1, str(client.getCount(db_name_1)["count"])))

# ---------------------------------------------------------------

def indexing_in_batch(db_name) :

	print("--------------------------------------------------------------------------------------------")
	print("--------- Indexing in batch")
	print("--------------------------------------------------------------------------------------------")

	print("DELETE db %s if it exists." % db_name)
	if db_name in client.getDBs()['dbs'] :
		client.deleteDB(db_name, wait = True)

	img = [{"url": "https://s3-eu-west-1.amazonaws.com/deepo-public/Demo/shoes/shoes_1.jpg"}]
	predefined_id = "batchTestClient"
	client.saveObject(db_name, id = predefined_id, imgs = img, wait = True)

	batch = deepomatic.BatchObject(db_name)

	print("PUT a batch of 20 images in %s with predefined ids." % db_name)
	url_base = "https://s3-eu-west-1.amazonaws.com/deepo-public/Demo/shoes/shoes_%s.jpg"
	for i in range(0,20) :
		obj = deepomatic.ImgsSend("url", url_base % i)
		batch.addObject(obj, "shoes_%d" % i)

	batch_response = client.batchRequest(batch, wait = True)


	print("DB %s has now %s element." % (db_name, str(client.getCount(db_name)['count'])))


# ---------------------------------------------------------------

def searching(db_name) :

	if not db_name in client.getDBs()["dbs"] :
		indexing_in_batch()

	print("--------------------------------------------------------------------------------------------")
	print("--------- searching")
	print("--------------------------------------------------------------------------------------------")

	img = [{"url": "https://s3-eu-west-1.amazonaws.com/deepo-public/Demo/shoes/shoes_0.jpg"}]
	client.saveObject(db_name, imgs = img, wait=True)
	image_test_url = {"url" : "https://s3-eu-west-1.amazonaws.com/deepo-public/Demo/shoes/shoes_20.jpg"}
	search_results = client.search(db_name, image_test_url, wait = True)
	print("The id of the image that is the most similar to the query is %s with a score of %.5f" % (search_results['hits'][0]['id'], search_results['hits'][0]['score']))

def perfect_match(db_name) :

	print("--------------------------------------------------------------------------------------------")
	print("--------- Perfect Match")
	print("--------------------------------------------------------------------------------------------")

	print("DELETE db %s if it exists." % db_name)
	if db_name in client.getDBs()['dbs'] :
		client.deleteDB(db_name, wait = True)

	url_base = "https://s3-eu-west-1.amazonaws.com/deepo-public/Demo/perfect_match/%s.jpg"
	poster_names = ['elle', 'jurassic_shark', 'le_chasseur', 'sos_fantome', 'the_dark_night']
	print("PUT 5 movie posters in db %s." % db_name)

	batch = deepomatic.BatchObject(db_name)
	for name in poster_names :
		obj = deepomatic.ImgsSend("url", url_base % name)
		batch.addObject(obj, name)

	batch_response = client.batchRequest(batch, wait = True)

	image_test = "https://s3-eu-west-1.amazonaws.com/deepo-public/Demo/perfect_match/query.jpg"
	search_results = client.search(db_name, {'url' : image_test}, wait = True)
	print("Did we found a perfect match: %s" % str(search_results['hits'][0]['is_perfect_match']))

def detection(imagename) :
	print imagename

	# print("--------------------------------------------------------------------------------------------")
	# print("--------- detection")
	# print("--------------------------------------------------------------------------------------------")


	#response = client.detect("fashion", img_file, wait = True)
	#response = client.detect("fashion", {"url" : imagename}, wait = True)

	
	response = client.detect("fashion", {"url" : imagename}, wait = True)





	# print("Here is what we have detected:")
	# print(json.dumps(response['boxes'], indent=2, sort_keys=True))
	return response['boxes']


# db_and_indexing("demo_1", "demo_2")
# indexing_in_batch("batch_indexing")
# searching("batch_indexing")
# perfect_match("perfect_match")


def analyzeModel(imagename):
	response = detection(imagename);
	# pprint(response);
	tg = ThreadGenius(api_key='key_MDZhYTYyNzM2OWQzM2Y1NGRmZTIwMDZhNWRjNjI4')

	returnval = {}

	for item in response:
		cr = [response[item][0]['xmin'], response[item][0]['ymin'], response[item][0]['xmax'],response[item][0]['ymax']]
		# pprint(cr)
		image = ImageUrlInput(url=imagename,crop = cr)#ImageFileInput(file_object=open(imagename),crop = cr)
		# 

	 	responsesauce = tg.tag_image(image=image)

	 	data = responsesauce

	 	# pprint(data)

	
	 	

	 	
	 	# ['response']['prediction']['data']['tags']
	 	for item1 in data['response']['prediction']['data']['tags']:
	 		# pprint(item)
	 		if (item1['type'] == 'color'):
	 			returnval[item]=  item1['name'].replace("color ", '')
	 			break;

	returnval["link"] = imagename
	return returnval



def runThruAllModels():
	counter = 0;
	overallJSON = []
	# modelList = ["https://cdn.shopify.com/s/files/1/0162/2116/files/Smart_Everyday_Outfit_Ideas_For_Men_2.jpg?v=1488179974", "https://i.pinimg.com/736x/6c/cf/18/6ccf181f6261dd2b290dc395ac1d9007--mens-fall-outfits-men-outfits.jpg"]
	print "hi"
	for subdir, dirs, files in os.walk('/home/ec2-user/clothes/clothes/fols'):
	    for file in files:
	    	
			    	filepath = str(subdir + os.sep + file)
			    	if "DS_Store" not in filepath:
					try:
						Htfile = 'http://54.200.230.168:80/'+file
						print Htfile
						Htfile = Htfile.replace(" ", '%20')
						overallJSON.append(analyzeModel(Htfile))
						counter = counter +1
						print counter
					except:
						print "Error"
	    		

	    	
	       	# analyzeModel(filepath)

	# for item in modelList:
	# 	analyzeModel(item);
	# pprint(overallJSON)

	overallJSON = str(overallJSON)
	overallJSON = overallJSON.replace('{u', '{')
	overallJSON = overallJSON.replace(": u'", ': "')
	overallJSON = overallJSON.replace(", u'", ', "')
	overallJSON = overallJSON.replace("'", '"')

	text_file = open("Output.txt", "w")
	text_file.write(overallJSON)
	text_file.close()

	# pprint(overallJSON)

	# overallJSON = json.loads(overallJSON)

	# pprint(overallJSON.text)
	# with open('data.txt', 'w') as outfile:
	# 	json.dump(overallJSON, outfile)
	# pprint(overallJSON)

topstuff = ['jacket-coat','jumpsuit','suit','sweater', 'dress','top-shirt']
bottomstuff = ['shorts','pants']
def addToWardrobe(dataVal):
	if dataVal['name'] in topstuff:
		db.tops.insert_one(dataVal)
		print 'added to tops'
	elif dataVal['name'] in bottomstuff:
		db.bottoms.insert_one(dataVal)
		print 'added to bottoms'
	else:
		db.shoes.insert_one(dataVal)

def analyzeSingleItem(imagename):

	response = detection(imagename);
	key = response.keys()[0] + ''
	tg = ThreadGenius(api_key='key_MDZhYTYyNzM2OWQzM2Y1NGRmZTIwMDZhNWRjNjI4')
	image =  ImageUrlInput(url=imagename)#ImageFileInput(file_object=open(imagename))


	response = tg.tag_image(image=image)

	data = response

	returnval = {}
	returnval['name'] = key
	returnval['link'] = imagename
	
	# pprint(data)
	for item1 in data['response']['prediction']['data']['tags']:
	 		# pprint(item)
	 		if (item1['type'] == 'color'):
	 			returnval['color']=  item1['name'].replace("color ", '')
	 			break;

	pprint (returnval)
	addToWardrobe(returnval)




def KToF(k):
	return (k -273 )*1.8 + 32

def getCurrentWeather(zipcode):
	# now = datetime.datetime.now()
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+ str(zipcode) +',us&APPID=c78409bb42ae498f81313fa87a7936b7')
	data = json.loads(r.text)
	dataNew = {}
	dataNew['min'] = KToF(data['main']['temp_min'])
	dataNew['max'] = KToF(data['main']['temp_max'])
	# json_data = json.dumps(dataNew)
	return dataNew

album = None # You can also enter an album ID here


def upload_kitten(path):
	client_id = '37b80e7e12ab5e0'

	headers = {"Authorization": "Client-ID 37b80e7e12ab5e0"}

	api_key = '48662df2d4e94875c8092380c3fe6f595c32db4d'

	url = "https://api.imgur.com/3/upload.json"

	j1 = requests.post(
	    url, 
	    headers = headers,
	    data = {
	        'key': api_key, 
	        'image': b64encode(open(path, 'rb').read()),
	        'type': 'base64',
	        'name': '1.jpg',
	        'title': 'Picture no. 1'
	    }
	)
	data = json.loads(j1.text)
	print data
	return data['data']['link']

# runThruAllModels()

# analyzeSingleItem("https://s7d2.scene7.com/is/image/aeo/1432_1093_475_f?$bvFeed$")


#def getOther2Garments(item):
	# itemType = item.type

	# allModelsWithSameColor = {}

	# for

	# firstOtherGarment

	# secondOtherGarment

	# for item in firstOtherGarment:

def compareRGBvals(c1, c2):
	# print(c1)
	diffRed   = abs(c1[0]   - c2[0]);
	diffGreen = abs(c1[1] - c2[1]);
	diffBlue  = abs(c1[2]  - c2[2]);
	# print(diffRed)
	pctDiffRed   = float(diffRed)   / float(255);
	pctDiffGreen = float(diffGreen) / float(255);
	pctDiffBlue   = float(diffBlue)  / float(255);
	# print "sauce"
	print (pctDiffRed + pctDiffGreen + pctDiffBlue) / 3 * 100

def colorSimilarity(input1, input2):
	input1 = input1.replace(" ", '')
	input2 = input2.replace(" ", '')
	try:
		# print type(webcolors.name_to_rgb(input1))
		# print webcolors.name_to_rgb(input2);

		if (compareRGBvals(webcolors.name_to_rgb(input1), webcolors.name_to_rgb(input2))<20):
			return True
		else:
			return False


	except:
		return False
	# return webcolors.name_to_rgb(input1)

def most_common(L):
  # get an iterable of (item, iterable) pairs
	SL = sorted((x, i) for i, x in enumerate(L))
  # print 'SL:', SL
  	groups = itertools.groupby(SL, key=operator.itemgetter(0))
  # auxiliary function to get "quality" for an item
  	def _auxfun(g):
	  	item, iterable = g
	  	count = 0
	  	min_index = len(L)
	  	for _, where in iterable:
	  		count += 1
	  		min_index = min(min_index, where)
    # print 'item %r, count %r, minind %r' % (item, count, min_index)
    		return count, -min_index
  # pick the highest-count/earliest item
  	return max(groups, key=_auxfun)[0]

def findMostPopularColors(modelArray):
	# printModelArray()
	shirtArray =[]
	pantArray =[]
	shoeArray =[]

	for outfit in modelArray:
		# print (outfit)
		shirtArray.append(outfit['top-shirt'])
		pantArray.append(outfit['pants'])
		shoeArray.append(outfit['shoe'])


	return {'shirtColor': most_common(shirtArray), 'pantColor': most_common(pantArray), 'shoeColor': most_common(shoeArray)}



def findAllModelGarmentColors(data):
	allPossibleModels = []


	# if data['name'] in topstuff:

	for stuff in modelData:
		
		if (colorSimilarity(data['color'], stuff['top-shirt'])):
			allPossibleModels.append(stuff)
	print("--------------------------------------------------------------------------------------------")
	print(len(allPossibleModels))

	# elif data['name'] in bottomstuff:
	# 	for stuff in modelData:
	# 		if (data['color'] == stuff['pant'])
	# 			allPossibleModels.append(stuff)

	
	return findMostPopularColors(allPossibleModels)




		

	arr = []
	for stuff in modelData:
		arr.append(stuff)

@app.route('/createOutfit', methods = ['GET', 'POST'])
def creatOutfit():
	

	idealOuterwearArray = []
	idealPantsArray = []
	idealShoesArray = []

	idealOuterwear= None
	idealPants = None
	idealShoes = None

	# hoodieNeeded = False
	# pantsNeeded = False

		# hoodieNeeded = True
		# pantsNeeded = True
	for document in db.tops.find():
		if (getCurrentWeather(95129)['max']<65 and (document['name']== 'jacket-coat' or document['name'] == 'sweater')):
			idealOuterwearArray.append(document)
		elif (getCurrentWeather(95129)['max']>65 and not(document['name'] == 'jacket-coat' or document['name'] == 'sweater')):
			idealOuterwearArray.append(document)
				# print(idealOuterwear)


	
	for doc in idealOuterwearArray:
		if(doc['color'] == 'silver' ):#getTwitterColor!!!!!!!!!!!!!!!!!!!!!!!!!!!!
			idealOuterwear = doc
			break;
		else:
			idealOuterwear = doc



	print(idealOuterwear)
	arr = findAllModelGarmentColors(idealOuterwear)

	# print(arr)


	for bottom in db.bottoms.find():
		if (colorSimilarity(bottom['color'], arr['pantColor'])):
			idealPants = bottom
			break;
		else:
			idealPants =bottom

	for shoe in db.shoes.find():
		if (colorSimilarity(shoe['color'],arr['shoeColor'])):
			idealShoes = shoe
			break;
		else:
			idealShoes = shoe
	del idealShoes['_id']
	del idealPants['_id']
	del IdealOuterwear['_id']


	return jsonify([idealOuterwear, idealPants, idealShoes])




	# else
	# 	hoodieNeeded = False

	# twitterColor = getTwitterColor()

	# foundTwitterColorInWardrobe = false

	# for document in db.tops.find():
	# 	if (item.color == twitterColor)
	# 		idealoutwear = item
	# 		foundTwitterColorInWardrobe = true

# creatOutfit();

#analyzeSingleItem('https://wordans-mxelda46illwc0hq.netdna-ssl.com/files/model_specifications/2015/8/28/116904/116904_big.jpg?1440802235')



# 	if(!foundTwitterColorInWardrobe)
# 		for item in pants
# 			if (item.color = twitterColor)
@app.route('/getTops', methods = ['GET', 'POST'])		
def getAllTops():
	topsauce = []
	for stuff in db.tops.find():
		del stuff['_id']
		topsauce.append(stuff)
	return jsonify(topsauce)	
@app.route('/getBottoms', methods = ['GET', 'POST'])
def getAllBottoms():
	bottomsauce = []
	for stuff in db.bottoms.find():
		del stuff['_id']
		bottomsauce.append(stuff)
	return jsonify(bottomsauce)	
@app.route('/getShoes', methods = ['GET', 'POST'])
def getAllShoes():
	shoesauce = []
	for stuff in db.shoes.find():
		del stuff['_id']
		shoesauce.append(stuff)
	return jsonify(shoesauce)
app.run(host="0.0.0.0", port=80)




	


