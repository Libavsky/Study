from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.pipeline
import sklearn.neighbors as knn
import sklearn.ensemble as ens
import sklearn.naive_bayes as nba
from sklearn import svm

#%%
# Load data
data = load_breast_cancer()
X_train, X_test, Y_train, Y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=111)

#%%
# Function to test a classifier
def testfunction(name,steps,parameters):

    pipeline = sklearn.pipeline.Pipeline(steps)
    cv = sklearn.model_selection.GridSearchCV(pipeline, param_grid=parameters)
    cv.fit(X_train, Y_train)
    y_predictions = cv.predict(X_test)
    report = sklearn.metrics.classification_report(Y_test, y_predictions)

    print(report)
    print("Train score (" + name + "):", cv.score(X_train, Y_train))
    print("Test score (" + name + "):", cv.score(X_test, Y_test))

    plt.figure(figsize=(1,1))
    plt.title("Confusion matrix")
    sns.heatmap(sklearn.metrics.confusion_matrix(Y_test, y_predictions), annot=True, fmt="d")
    plt.show()

    plt.figure(figsize=(6,1))
    plt.title("Precision score")
    sns.barplot(sklearn.metrics.precision_score(Y_test, y_predictions, average=None), data.target_names)
    plt.show()

    plt.figure(figsize=(6,1))
    plt.title("Recall score")
    sns.barplot(sklearn.metrics.recall_score(Y_test, y_predictions, average=None), data.target_names)
    plt.show()

#%%
# function to test kNearestNeighbours classifier
def kNeighbours():
    classifier = knn.KNeighborsClassifier()

    ktable = [1,3,5,6,7,8,9]
    steps = [('classifier', classifier)]

    parameters = dict(classifier__n_neighbors = ktable)

    testfunction("kNearestNeighbours",steps,parameters)
    
kNeighbours();

#%%
# function to test Multinomial Naive Bayes classifier
def multiNomialNB():
    classifier = nba.MultinomialNB()
    
    alphas = [0.0, 0.4, 0.8, 1.0, 1.4, 2.0]
    
    steps = [('classifier', classifier)]
    parameters = dict(classifier__alpha = alphas)

    testfunction("NaiveBayes",steps,parameters)

multiNomialNB();

#%%
# function to test Gaussian Naive Bayes classifier
def gaussianNB():
    classifier = nba.GaussianNB()
    
    steps = [('classifier', classifier)]
    parameters = dict()

    testfunction("NaiveBayes",steps,parameters)

gaussianNB();

#%%
# function to test SVM classifier
def SVM():
    classifier = svm.SVC()

    steps = [('classifier', classifier)]

    parameters = dict(classifier__kernel=["sigmoid", "rbf","linear"],
                      classifier__decision_function_shape=["ovo", "ovr"],
                      classifier__gamma=[0.001, 0.5, 0.2, 0.02, 0.002, "auto"],
                      classifier__coef0=[0.001, 0.01, 0.1, 0.3, 0.0])

    testfunction("SVM",steps, parameters)
    #Non-linear approaches offer accuracy of ~95%
   
SVM();

#%%    
# function to test bagging
def bagging():
    classifier = ens.BaggingClassifier();

    ntable = [7,13,21]
    max_samples = max_features = [0.10,0.25,0.35,0.60]
    bootstrap_features = bootstrap = [True, False]
    
    steps = [('classifier', classifier)]

    parameters = dict(classifier__n_estimators = ntable,
                      classifier__max_samples = max_samples,
                      classifier__max_features = max_features,
                      classifier__bootstrap_features = bootstrap_features,
                      classifier__bootstrap = bootstrap)

    testfunction("bagging",steps,parameters)
    
bagging();