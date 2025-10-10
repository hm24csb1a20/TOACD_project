# we tested with logistic regression 
# we saw very low accuracy indicatint that the data we have been given is
# probably not linear
# now trying other models 


import os  #for the fiel management
from loader import prepare_dataset #premade file handler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


# set base path dynamically
base_path = os.path.join(os.getcwd(), "data")  # current working directory + "data"
benign_path = os.path.join(base_path, "benign")
malicious_path = os.path.join(base_path, "malicious")
X, y, vectorizer = prepare_dataset(benign_path, malicious_path)


# split your data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# define model
rf = RandomForestClassifier(
    n_estimators=200,   # number of trees
    max_depth=None,     # let trees grow fully
    random_state=42,
    class_weight='balanced'  # optional if dataset is imbalanced
)

# train
rf.fit(X_train, y_train)

# predict
y_pred = rf.predict(X_test)

# evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))