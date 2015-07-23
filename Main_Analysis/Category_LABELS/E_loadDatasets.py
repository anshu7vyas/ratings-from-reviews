__author__ = 'ANSHUL'

'''
#######################################################################################
#This script acts as the main script as all other preprocessing steps are called and the 
#files are converted to a pandas dataframe, to use for the classifiers.
#
#######################################################################################
'''
import sys, os
import numpy as np
import pandas as pd
import random
from C_convert_json_to_csv import *
from D_Preprocess import *


"""Pipeline for all the steps. It returns a pandas dataframe which can be used as training set and test set when split."""
def prepareDataset():
	
	print "\n##############################################################"
	print "\nConverting JSON files to CSV"
	print "\n##############################################################\n"
	json2csv()
	print "COMPLETE"

	for csv_filename in glob("B_Split_JSON/*.csv"):
		print "Balancing Dataset: %s" % (csv_filename)
		df = pd.read_csv(csv_filename)
		df = balance_df(df)
		csv_new = '%s-balanced.csv' % csv_filename[:-4]
		df.to_csv(csv_new, encoding='utf-8', index=False)
		print "Balanced the dataset: %s-balanced.csv" % (csv_new)[:-4]

	tenPath = os.path.abspath("B_Split_JSON/10000_restaurant_ab.csv")
	tenBalancepath = os.path.abspath("B_Split_JSON/10000_restaurant_ab-balanced.csv")
	
	ten_df = pd.read_csv(tenPath)
	tenBalance_df = pd.read_csv(tenBalancepath)
	
	print "\n##############################################################################"
	print "\nNow doing preprocessing on the 10000_restaurant_ab.csv  & the balanced dataset"
	print "\n##############################################################################\n"
	ten_df['TEXT_REVIEW'] = ten_df['TEXT_REVIEW'].apply(preProcess)
	tenBalance_df['TEXT_REVIEW'] = tenBalance_df['TEXT_REVIEW'].apply(preProcess)
	
	'''
	for idx in range(5):
		print tenBalance_df.TEXT_REVIEW[idx]
	'''

	return ten_df, tenBalance_df

