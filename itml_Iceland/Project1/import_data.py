# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
import sklearn.pipeline
import sklearn.neighbors as knn
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.naive_bayes as nba
from sklearn import svm

#%%

# Include other files
import show_attr_distrib
import important_features

print("---> Importing data ...")
columns=["cl", "c-sh", "c-su", "c-co", "bru",
		"odor", "g-at", "g-sp", "g-si", "g-co", 
		"s-sh", "s-ro", "s-sar", "s-sbr", "s-car", 
		"s-cbr", "v-ty", "v-co", "r-nu", "r-ty", 
		"spc", "pop", "hab"]
mush = pd.read_csv("mushrooms.csv", header=None, names=columns)

# Remove the attribute with missing values
del mush["s-ro"]
del columns[11]

attributes = columns[1:]

classes=['edible', 'poisonous']
labelEncoders = {}

# Use label encoder to change string values into numerical values
for column in columns:  
    le = LabelEncoder()
    labelEncoders[column] = le
    mush[column] = le.fit_transform(mush[column].values)

y = mush["cl"]
X = mush.drop("cl", 1)

print("---> Splitting data to train and test set ...")
X_train_orig, X_test_orig, y_train_orig, y_test_orig = train_test_split(X, y, test_size=0.2, random_state=6)

print("---> Show attribute distributions ...")
show_attr_distrib.grid_of_plots(attributes, X_train_orig, X_test_orig)

print("---> Show class distributions ...")
show_attr_distrib.class_distribution(y_train_orig, y_test_orig)

#%%
# Encode nominal attributes into binary values
enc_train = OneHotEncoder()
X_train = enc_train.fit_transform(X_train_orig)
X_test = enc_train.transform(X_test_orig)

y_train = y_train_orig
y_test = y_test_orig

classifier_results = {}
    
#%%
# Function to test a classifier
def testfunction(name,steps,parameters):

    print("---> Classifying using", name, "...")

    pipeline = sklearn.pipeline.Pipeline(steps)
    cv = sklearn.model_selection.GridSearchCV(pipeline, param_grid=parameters)
    cv.fit(X_train, y_train)
    y_predictions = cv.predict(X_test)
    print("Parameters chosen:")
    key_list = parameters.keys()
    for i in key_list:
        print(i[12:]," = ",cv.best_params_[i])
    report = sklearn.metrics.classification_report(y_test, y_predictions)
    print("***Classification report***")
    print(report)
    print("Train score (" + name + "):", cv.score(X_train, y_train))
    print("Test score (" + name + "):", cv.score(X_test, y_test))

    plt.figure(figsize=(8, 3))
    plt.title("Confusion matrix (" + name + ")")
    sns.heatmap(sklearn.metrics.confusion_matrix(y_test, y_predictions), annot=True, fmt="d")
    plt.show()

    plt.figure(figsize=(8,3))
    plt.title("Precision score (" + name + ")")
    sns.barplot(sklearn.metrics.precision_score(y_test, y_predictions, average=None), classes)
    plt.show()

    plt.figure(figsize=(8,3))
    plt.title("Recall score (" + name + ")")
    sns.barplot(sklearn.metrics.recall_score(y_test, y_predictions, average=None), classes)
    plt.show()
    
    min_mean = cv.cv_results_['mean_test_score'].min()
    max_mean = cv.cv_results_['mean_test_score'].max()
    
    print("Mean test scores for hyperparameter combinations are in range:",
          round(min_mean, 4), "-", round(max_mean, 4))
    
    classifier_results[name] = cv.cv_results_
    
    return cv.cv_results_

def plot_hyperparameters(classifier_name,hyper_name,hyper_values,results):
    mean_scores = results['mean_test_score']
    
    plt.plot(hyper_values, mean_scores)
    plt.title('Hyperparameter tuning (' + classifier_name + ')')
    plt.xlabel(hyper_name)
    plt.ylabel('Mean test score (cross-validation)')
    plt.xscale('log')
    plt.show()

#%%
# Function to test kNearestNeighbours classifier
def kNeighbours():
    classifier = knn.KNeighborsClassifier()

    ktable = [1,2,5,10,50,100]
    steps = [('classifier', classifier)]

    parameters = dict(classifier__n_neighbors = ktable)

    results = testfunction("kNearestNeighbours",steps,parameters)
    plot_hyperparameters("kNearestNeighbours","k",ktable,results)
    
kNeighbours();

#%%
# Function to test Multinomial Naive Bayes classifier
def multiNomialNB():
    classifier = nba.MultinomialNB()

    alphas = [1e-4, 1e-3, 1e-2, 0.1, 0.4, 0.8, 1.0]

    steps = [('classifier', classifier)]
    parameters = dict(classifier__alpha = alphas)

    results = testfunction("NaiveBayes",steps,parameters)
    plot_hyperparameters("NaiveBayes","alpha",alphas,results)

multiNomialNB();

#%%
# Function to test SVM classifier
def SVM():
    classifier = svm.SVC()

    steps = [('classifier', classifier)]

    parameters = dict(classifier__kernel=["linear"],
                      classifier__decision_function_shape=["ovo", "ovr"],
                      classifier__gamma=[0.001, 0.002, 0.02, 0.2, 0.5, "auto"],
                      classifier__coef0=[0, 0.001, 0.01, 0.1, 0.3])

    testfunction("SVM",steps, parameters)

SVM();

#%%
# Function to test decision tree classifier
def forest():
    classifier = DecisionTreeClassifier();
    max_features = [0.10,0.25,0.35,0.60]
    min_samples_leaf = [2,3,5]

    steps = [('classifier', classifier)]

    parameters = dict(classifier__min_samples_leaf = min_samples_leaf,
                      classifier__max_features = max_features)

    testfunction("Decision tree",steps,parameters)

forest();

#%%
# Function to test neural network classifier
def NeuralNetwork():
    classifier = MLPClassifier()
    steps = [('classifier', classifier)]

    parameters = dict(classifier__activation=["logistic"],
                      classifier__hidden_layer_sizes=[(50,50),(20,20),(120,)],
                      classifier__solver = ["sgd","adam"],
                      classifier__learning_rate = ["constant"],
                      classifier__momentum = [0.5,0.1],
                      classifier__max_iter = [2000,1000],
                      classifier__learning_rate_init = [0.1,0.2,0.01])

    testfunction("Neural Network", steps, parameters)

NeuralNetwork();

#%%
important_features.get_important_features(X_train_orig, y_train_orig, attributes)

#%%
def result_summary():
    print('%-20s%-12s%-12s%-12s' % ("Classifier", "Min score", "Max score", "Combinations"))
    
    for classifier in sorted(classifier_results):
        min_mean = classifier_results[classifier]['mean_test_score'].min()
        max_mean = classifier_results[classifier]['mean_test_score'].max()
        combinations = len(classifier_results[classifier]['mean_test_score'])
        print ('%-20s%-12.3f%-12.3f%-12i' % (classifier, min_mean, max_mean, combinations))
        
result_summary()
