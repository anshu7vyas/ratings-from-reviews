__author__ = 'ANSHUL'

from F_MultinomialNB_sklearn_ import *
from G_SVC_sklearn_ import *

def main():
	print "\n##############################################################"
	print "\nMultinomial Naive Bayes:"
	print "\nFeature Sets:\n"
	print "\n1. Most common Features in the dataset"
	print "\n2. Bi Grams"
	print "\n3. Tri Grams"
	print "\n##############################################################\n"
	multinomialNBClassifier()
	print "\n##############################################################"
	print "\nSVC:"
	print "\nFeature Sets:\n"
	print "\n1. Most common Features in the dataset"
	print "\n2. Bi Grams"
	print "\n3. Tri Grams"
	print "\n##############################################################\n"
	SVCClassifier()

main()