#  Malware Detection using Machine Learning

---

##  Overview

This project aims to detect whether a given piece of code is **malicious or benign** using machine learning.  
We started simple — with a **logistic regression model** — and are now moving toward more powerful **tree-based classifiers** like Random Forest.


## Prerequistes 
`conda create --name lime python=3.12 `
`conda activate lime`
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

###  How Logistic Regression Works

The main idea behind logistic regression is to estimate the probability that a given input `x` belongs to a certain class — in our case, whether a piece of code is **malicious** or **benign**.

We use the **sigmoid (logistic) function** to convert any real value into a range between 0 and 1:

h_theta(x) = 1 / (1 + exp(-theta^T * x))

Here:
- `x` = feature vector representing the code (after TF-IDF transformation)
- `theta` = model parameters (weights)
- `h_theta(x)` = probability that the code is malicious  

We then classify as:
- malicious if h_theta(x) >= 0.5  
- benign otherwise  

---

###  Loss Function (Cost Function)

To measure how well our model is predicting, we use the **log loss** or **binary cross-entropy** function:

J(theta) = -(1/m) * Σ [ y(i) * log(h_theta(x(i))) + (1 - y(i)) * log(1 - h_theta(x(i))) ]

Where:
- `m` = number of training samples  
- `y(i)` ∈ {0, 1} = true label (0 = benign, 1 = malicious)  
- `h_theta(x(i))` = predicted probability for sample `i`

This loss penalizes confident wrong predictions heavily — encouraging the model to output accurate probabilities.

---

###  Parameter Update (Newton’s Method)

To minimize J(theta), we iteratively update the model parameters using **Newton’s Method**, which uses both the gradient (first derivative) and the Hessian (second derivative) of the cost function.

theta_new = theta - inverse(H) * gradient

Where:
- gradient = (1/m) * X^T * (h_theta(x) - y)
- H (Hessian) = (1/m) * X^T * diag(h_theta(x) * (1 - h_theta(x))) * X

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
