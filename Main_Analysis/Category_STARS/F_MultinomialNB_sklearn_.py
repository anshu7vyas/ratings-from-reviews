__author__ = 'ANSHUL'

from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import *
from sklearn import metrics
from sklearn.cross_validation import cross_val_score
from sklearn.metrics import confusion_matrix, classification_report, precision_score, recall_score, roc_auc_score
from E_loadDatasets import prepareDataset
import numpy as np
import matplotlib.pyplot as plt

"""Classifying the star labels using Multinomial Naive Bayes readily available in sk-learn. """
def multinomialNBClassifier():
	df, bal_df = prepareDataset()
	
	print "\n##############################################################"
	print "\nFor preprocessed dataset - Multinomial Naive Bayes"
	print "\n##############################################################\n"

	train_ten, test_ten, train_starsTen, test_starsTen = train_test_split(df.TEXT_REVIEW, df.STARS, test_size=0.20, random_state=42)
	
	"""Most common features vectorizer."""
	bow_vectorizer = CountVectorizer(analyzer = "word", tokenizer = None, preprocessor = None, 
												ngram_range = (1, 1), binary = False,strip_accents='unicode', max_features=700)

	"""Feature Matrix for training and test sets."""
	bow_Feature_train = bow_vectorizer.fit_transform(train_ten)
	bow_Feature_test = bow_vectorizer.transform(test_ten)
	bow_Feature_train, bow_Feature_test
	
	bow_clf = MultinomialNB()
	bow_clf.fit(bow_Feature_train, train_starsTen)
	bow_clf_prediction = bow_clf.predict(bow_Feature_test)
	print bow_clf_prediction

	"""BiGrams vectorizer."""
	biGram_vectorizer = CountVectorizer(analyzer = "word", tokenizer = None, preprocessor = None,
													ngram_range = (2, 2), strip_accents='unicode')

	biGramFeatMatrain = biGram_vectorizer.fit_transform(train_ten)
	biGramFeatMatest = biGram_vectorizer.transform(test_ten)
	biGramFeatMatrain, biGramFeatMatest

	biGram_clf = MultinomialNB()
	biGram_clf.fit(biGramFeatMatrain, train_starsTen)
	biGram_clf_prediction = biGram_clf.predict(biGramFeatMatest)
	print biGram_clf_prediction

	"""TriGrams vectorizer."""
	trigram_vectorizer = CountVectorizer(analyzer = "word", tokenizer = None, preprocessor = None,
													ngram_range = (3, 3), strip_accents='unicode')

	triGramFeatMatrain = trigram_vectorizer.fit_transform(train_ten)
	triGramFeatMatest = trigram_vectorizer.transform(test_ten)
	triGramFeatMatrain, triGramFeatMatest

	triGram_clf = MultinomialNB()
	triGram_clf.fit(triGramFeatMatrain, train_starsTen)
	triGram_clf_prediction = triGram_clf.predict(triGramFeatMatest)
	print triGram_clf_prediction	

	def NBEvaluationsPreprocessed(name, predictions):
		target_names = ['*', '**', '***', '****', '*****']

		print "MODEL: %s" % name
		print

		print 'Precision: ' + str(metrics.precision_score(test_starsTen, predictions))
		print 'Recall: ' + str(metrics.recall_score(test_starsTen, predictions))
		print 'F1: ' + str(metrics.f1_score(test_starsTen, predictions))
		print 'Accuracy: ' + str(metrics.accuracy_score(test_starsTen, predictions))

		print
		print 'Classification Report:'
		print classification_report(test_starsTen, predictions, target_names=target_names)

	NBEvaluationsPreprocessed('Most Common Features Multinomial Naive Bayes - preprocessed', bow_clf_prediction)
	NBEvaluationsPreprocessed('BiGram Multinomial Naive Bayes - preprocessed', biGram_clf_prediction)
	NBEvaluationsPreprocessed('TriGram Multinomial Naive Bayes - preprocessed', triGram_clf_prediction)
	
	print "\n##############################################################"
	print "\nFor balanced dataset - Multinomial Naive Bayes"
	print "\n##############################################################\n"

	train_bal, test_bal, train_bal_stars, test_bal_stars = train_test_split(bal_df.TEXT_REVIEW, bal_df.STARS, test_size=0.20, random_state=42)
	
	"""Most common features vectorizer."""
	bow_vectorizer = CountVectorizer(analyzer = "word", tokenizer = None, preprocessor = None, 
												ngram_range = (1, 1), binary = False,strip_accents='unicode', max_features=700)

	"""Feature Matrix for training and test sets."""
	bow_Feature_bal_train = bow_vectorizer.fit_transform(train_bal)
	bow_Feature_bal_test = bow_vectorizer.transform(test_bal)
	bow_Feature_bal_train, bow_Feature_bal_test
	
	bow_bal_clf = MultinomialNB()
	bow_bal_clf.fit(bow_Feature_bal_train, train_bal_stars)
	bow_bal_clf_prediction = bow_bal_clf.predict(bow_Feature_bal_test)
	print bow_bal_clf_prediction

	"""BiGrams vectorizer."""
	biGram_bal_vectorizer = CountVectorizer(analyzer = "word", tokenizer = None, preprocessor = None,
													ngram_range = (2, 2), strip_accents='unicode')

	biGram_Feature_bal_train = biGram_bal_vectorizer.fit_transform(train_bal)
	biGram_Feature_bal_test = biGram_bal_vectorizer.transform(test_bal)
	biGram_Feature_bal_train, biGram_Feature_bal_test 

	biGram_bal_clf = MultinomialNB()
	biGram_bal_clf.fit(biGram_Feature_bal_train, train_bal_stars)
	biGram_bal_clf_prediction = biGram_bal_clf.predict(biGram_Feature_bal_test)
	print biGram_bal_clf_prediction

	"""TriGrams vectorizer."""
	trigram_bal_vectorizer = CountVectorizer(analyzer = "word", tokenizer = None, preprocessor = None,
													ngram_range = (3, 3), strip_accents='unicode')

	triGram_Feature_bal_train = trigram_bal_vectorizer.fit_transform(train_bal)
	triGram_Feature_bal_test = trigram_bal_vectorizer.transform(test_bal)
	triGram_Feature_bal_train, triGram_Feature_bal_test

	triGram_bal_clf = MultinomialNB()
	triGram_bal_clf.fit(triGram_Feature_bal_train, train_bal_stars)
	triGram_bal_clf_prediction = triGram_bal_clf.predict(triGram_Feature_bal_test)
	print triGram_bal_clf_prediction

	def NBEvaluationsBalanced(name, predictions):
		target_names = ['*', '**', '***', '****', '*****']

		print "MODEL: %s" % name
		print

		print 'Precision: ' + str(metrics.precision_score(test_bal_stars, predictions))
		print 'Recall: ' + str(metrics.recall_score(test_bal_stars, predictions))
		print 'F1: ' + str(metrics.f1_score(test_bal_stars, predictions))
		print 'Accuracy: ' + str(metrics.accuracy_score(test_bal_stars, predictions))

		print
		print 'Classification Report:'
		print classification_report(test_bal_stars, predictions, target_names=target_names)

	NBEvaluationsBalanced('Most Common Features Multinomial Naive Bayes - balanced', bow_bal_clf_prediction)
	NBEvaluationsBalanced('BiGram Multinomial Naive Bayes - balanced', biGram_bal_clf_prediction)
	NBEvaluationsBalanced('TriGram Multinomial Naive Bayes - balanced', triGram_bal_clf_prediction)

multinomialNBClassifier()


