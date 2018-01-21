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


import numpy as np
# import cv2
#from twython import Twython
import json
import csv
import random

from datetime import datetime


appID  = '227318977946'
apiKey = 'c4c34cb598804f448cd60bf44657d83c'

client = deepomatic.Client(appID, apiKey)

# ---------------------------------------------------------------------------------------------------
# For the sake of reproducibility, we always wait for the tasks to complete via a check on the taskID
# ---------------------------------------------------------------------------------------------------

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
	for subdir, dirs, files in os.walk('/fols'):
	    for file in files:
	    	
			    	filepath = str(subdir + os.sep + file)
			    	if "DS_Store" not in filepath:
			    		Htfile = '0.0.0.0:8000/'+file
			    		Htfile = Htfile.replace(" ", '%20')
		    			overallJSON.append(analyzeModel(Htfile))
		    			counter = counter +1
		    			print counter
	    		

	    	
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



def analyzeSingleItem(imagename):

	response = detection(imagename);
	key = response.keys()[0] + ''
	tg = ThreadGenius(api_key='key_MDZhYTYyNzM2OWQzM2Y1NGRmZTIwMDZhNWRjNjI4')
	image =  ImageUrlInput(url=imagename)#ImageFileInput(file_object=open(imagename))


	response = tg.tag_image(image=image)

	data = response

	returnval = {}

	for item1 in data['response']['prediction']['data']['tags']:
	 		# pprint(item)
	 		if (item1['type'] == 'color'):
	 			returnval[key]=  item1['name'].replace("color ", '')
	 			break;

	pprint (returnval)

# analyzeSingleItem()


def KToF(k):
	return (k -273 )*1.8 + 32

def getCurrentWeather(zipcode):
	now = datetime.datetime.now()
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

runThruAllModels()

# analyzeSingleItem(upload_kitten('/Users/tejasvikothapalli/Desktop/pic.jpg'))


#def getOther2Garments(item):
	# itemType = item.type

	# allModelsWithSameColor = {}

	# for

	# firstOtherGarment

	# secondOtherGarment

	# for item in firstOtherGarment:



# def creatOutfit():
# 	hoodieNeeded = True
# 	if (getCurrentWeather(95129)['max']<65):
# 		hoodieNeeded = True
# 	else
# 		hoodieNeeded = False

# 	twitterColor = getTwitterColor()

# 	foundTwitterColorInWardrobe = false

# 	for item in outwearMongoArray:
# 		if (item.color == twitterColor)
# 			idealoutwear = item
# 			foundTwitterColorInWardrobe = true




# 	if(!foundTwitterColorInWardrobe)
# 		for item in pants
# 			if (item.color = twitterColor)
		

		


	

# creatOutfit()

