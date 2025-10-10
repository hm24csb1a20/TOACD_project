#  Malware Detection using Machine Learning

---

##  Overview

This project aims to detect whether a given piece of code is **malicious or benign** using machine learning.  
We started simple — with a **logistic regression model** — and are now moving toward more powerful **tree-based classifiers** like Random Forest.

---

##  Data Collection — the first big hurdle

One of the hardest parts wasn’t even the ML, it was **finding proper data**.

There’s no large, clean open dataset of raw code labeled as *malicious* vs *safe*.  
So we had to **understand what makes code “malicious”** — for example:
- commands that delete files or format drives  
- scripts that modify system files  
- or code that sends network requests in suspicious ways  

Since real malware samples can be unsafe or restricted,  
we decided to **create a dummy dataset** ourselves — simulating both:
- harmless snippets (`print("Hello World")`, loops, file reading)
- and “malicious” patterns (`system("rm -rf /")`, file deletion, etc.)

This custom dataset became the base for our experiments.

---

##  Data Loader

We wrote a **custom loader** that reads all the `.c` / `.cpp` / `.py` files,  
cleans them, tokenizes them, and transforms the code into a **vectorized form** suitable for ML models (using something like TF-IDF).

Example workflow:
```python
X, y, vectorizer = prepare_dataset(benign_path, malicious_path)
```
---
## Logistic Regression — first model attempt

We first implemented Logistic Regression manually using Newton’s Method (instead of using sklearn).
This helped us really understand the math behind the optimization.

```python
# basic steps:
grad = (1 / m) * (X.T @ (h - y))
H = (1 / m) * (X.T @ np.diag(h * (1 - h)) @ X)
update = np.linalg.inv(H) @ grad
theta = theta - update
```

While it successfully ran and converged, the accuracy was limited:

Model	Accuracy
Custom Logistic Regression	~33%
Sklearn Logistic Regression	~60–70%

This clearly showed that the relationship between code tokens and maliciousness isn’t linear — logistic regression was too simple to capture it.

## Random Forest Classifier

To capture nonlinear patterns, we began experimenting with a Random Forest Classifier, which builds multiple decision trees and averages their predictions.

```python
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight='balanced'
)
rf.fit(X_train, y_train)
```
