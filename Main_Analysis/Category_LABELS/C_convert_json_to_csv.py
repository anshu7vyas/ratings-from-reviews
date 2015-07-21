__author__ = 'ANSHUL'

"""
#############################################################################################
#This script is used to convert various datasets which are in JSON to CSV, we will be using 
#this script for different sizes of datasets.
#
#############################################################################################
"""
 
import json
import pandas as pd
from glob import glob

"""Convert a json string to a python dict which can be passed into Pandas dataframe."""
def convert(x):
    ob = json.loads(x)
    for k, v in ob.items():
        if isinstance(v, list):
            ob[k] = ','.join(v)
        elif isinstance(v, dict):
            for kk, vv in v.items():
                ob['%s_%s' % (k, kk)] = vv
            del ob[k]
    return ob

"""Labeling the data into 3 categories - Positive, Neutral and Negative"""
def labelData(values):
    if values == 5 or values == 4:
        return "positive"
    elif values == 3:
        return "neutral"
    else:
        return "negative"

"""conversion of the JSON files to CSV files and remove unused attributes from the dataset."""
def json2csv():

    #USED ONCE: IT TAKES A LOT OF TIME TO PROCESS JSON TO CSV CONVERSION
    for json_filename in glob('B_Split_JSON/*.json'):
        csv_filename = '%s.csv' % json_filename[:-5]
        print 'Converting %s to %s' % (json_filename, csv_filename)
        df = pd.DataFrame([convert(line) for line in file(json_filename)])
        df.columns = ['BUSINESS_ID', 'DATE', 'REVIEW_ID','STARS','TEXT_REVIEW','TYPE','USER_ID','VOTES_COOL','VOTES_FUNNY','VOTES_USEFUL']
        #Dropping the columns we have no use of
        df = df.drop('BUSINESS_ID', 1)
        df = df.drop('DATE', 1)
        df = df.drop('REVIEW_ID', 1)
        df = df.drop('TYPE', 1)
        df = df.drop('USER_ID', 1)
        df = df.drop('VOTES_COOL', 1)
        df = df.drop('VOTES_FUNNY', 1)
        df = df.drop('VOTES_USEFUL', 1)
        df['LABEL'] = df['STARS'].apply(lambda y:labelData(y))
        df.to_csv(csv_filename, encoding='utf-8', index=False)
        print "Conversion complete %s to %s" % (json_filename, csv_filename)

'''
"""@deprecated This function creates a CSV file of only the relevant attributes"""
def csvNeeded(file_name):

    dataSet = pd.read_csv(file_name)
    
    dataSet.columns = ['BUSINESS_ID', 'DATE', 'REVIEW_ID','STARS','TEXT_REVIEW','TYPE','USER_ID','VOTES_COOL','VOTES_FUNNY','VOTES_USEFUL']
    
    #Dropping the columns we have no use of
    #dataSet = dataSet.drop('BUSINESS_ID', 1)
    #dataSet = dataSet.drop('DATE', 1)
    dataSet = dataSet.drop('REVIEW_ID', 1)
    dataSet = dataSet.drop('TYPE', 1)
    #dataSet = dataSet.drop('USER_ID', 1)
    dataSet = dataSet.drop('VOTES_COOL', 1)
    dataSet = dataSet.drop('VOTES_FUNNY', 1)
    dataSet = dataSet.drop('VOTES_USEFUL', 1)
    
    csv_file = "relevant-38000.csv"
    dataSet.to_csv(csv_file, encoding='utf-8',index=False)
    print "conversion of relevant columns completed: %s" % (csv_file)
    
    return csv_file
'''