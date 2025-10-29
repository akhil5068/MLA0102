import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score
data = pd.read_csv("Iris.csv")
X = data.iloc[:, 1:-1] 
y = data.iloc[:, -1]   
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
clf = DecisionTreeClassifier(criterion='gini', random_state=1)
clf.fit(X_train, y_train)
print("Decision Tree Rules:\n")
print(export_text(clf, feature_names=list(X.columns)))
sample = [[5.1, 3.5, 1.4, 0.2]]
print("\nPredicted Class for", sample, ":", clf.predict(sample)[0])
y_pred = clf.predict(X_test)
print("\nModel Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")
