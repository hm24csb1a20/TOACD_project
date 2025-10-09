import os  #for the fiel management
from loader import prepare_dataset #premade file handler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# set base path dynamically
base_path = os.path.join(os.getcwd(), "data")  # current working directory + "data"
benign_path = os.path.join(base_path, "benign")
malicious_path = os.path.join(base_path, "malicious")

# load dataset
X, y, vectorizer = prepare_dataset(benign_path, malicious_path)

# split train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# train model
clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, y_train)

# predict and evaluate
y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
