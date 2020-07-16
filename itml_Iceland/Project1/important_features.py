from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import seaborn as sns

def get_important_features(X_train, y_train, attributes):
	tree = DecisionTreeClassifier();
	tree.fit(X_train, y_train)
	fature_importances = tree.feature_importances_
	pairs_attr_value = list(zip(attributes, fature_importances))
	ordered = sorted(pairs_attr_value, key=lambda x: (-x[1]))
	x = [a[0] for a in ordered]
	y = [b[1] for b in ordered]
	plt.figure(figsize=(15,5))
	plt.title("Feature importances")
	sns.barplot(x, y)
	plt.show()
