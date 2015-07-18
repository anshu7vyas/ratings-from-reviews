__author__ = 'ANSHUL'


import json
import os

'''
#################################################################################################
#This script enables to extract only those reviews for which the category is only Restaurants.
#
##################################################################################################
'''


"""Takes the Business data as input and returns the instances where category = Restaurants"""
def onlyRestaurants():
    i=0
    bussPath = os.path.abspath("OutputFiles/restaurants.json")
    yelpPath = os.path.abspath("InputFiles/yelp_academic_dataset_business.json")
    with open(bussPath,'w+') as inres:
        with open(yelpPath) as business:
            for line in business:
                   jbus=json.loads(line)
                   jcate=jbus['categories']
                   if 'Restaurants' in jcate:
                       i += jbus['review_count']
                       inres.write(json.dumps(jbus)+'\n')
                       
        print "restaurants.json succefully created."
    inres.close()
    business.close()

"""Takes input the generated restaurants.json and the Yelp! Review dataset and returns only instances of reviews which match the business id"""
def onlyRestaurantReviews():
    bussPath = os.path.abspath("OutputFiles/restaurants.json")
    revPath = os.path.abspath("OutputFiles/restaurants_review.json")
    inputPath = os.path.abspath("InputFiles/yelp_academic_dataset_review.json")
    res = open(bussPath)
    review = open(inputPath)
    res_review = open(revPath,'w+')

    ids = []
    for rline in res:
        ids.append(json.loads(rline)['business_id'])

    i=0
    for reline in review:
        jreview = json.loads(reline)
        reid = jreview['business_id']
        if reid in ids:
            i+=1
            res_review.write(json.dumps(jreview)+'\n')

    print "restaurants_review.json successfully created."
    res.close()
    review.close()
    res_review.close()

onlyRestaurants()
onlyRestaurantReviews()