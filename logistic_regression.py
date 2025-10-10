import os  #for the fiel management
from loader import prepare_dataset #premade file handler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

# set base path dynamically
base_path = os.path.join(os.getcwd(), "data")  # current working directory + "data"
benign_path = os.path.join(base_path, "benign")
malicious_path = os.path.join(base_path, "malicious")

# the logistic regression 
import numpy as np

class LogisticRegression:
    """logistic regression using newton method"""

    def __init__(self, eps=1e-6, max_iter=100, reg_lambda=1e-4):
        # attributes
        self.theta = None
        self.eps = eps
        self.max_iter = max_iter
        self.reg_lambda = reg_lambda  
    def sigmoid(self, z):
        # turns big positive to almost 1 and big neg to almost 0 
        return 1 / (1 + np.exp(-z))

    def fit(self, X, y):
        # do the actual training here newton style
        m, n = X.shape
        # if no theta yet just fill zeros
        self.theta = np.zeros(n) if self.theta is None else self.theta

        for _ in range(self.max_iter):
            h = self.sigmoid(X @ self.theta)
            # gradient or slope direction
            grad = (1 / m) * (X.T @ (h - y))

            # hessian = curvature of loss 
            D = np.diag(h * (1 - h))
            # add small reg term to avoid math problems
            H = (1 / m) * (X.T @ D @ X) + self.reg_lambda * np.eye(n)

            # try updating thetas with inverse of that thing
            try:
                update = np.linalg.inv(H) @ grad
            except np.linalg.LinAlgError:
                update = np.linalg.pinv(H) @ grad

            new_theta = self.theta - update

            # # check if no big changes
            # if np.linalg.norm(new_theta - self.theta, 1) < self.eps:
            #     self.theta = new_theta
            #     break

            # else keep looping
            self.theta = new_theta

    def predict_prob(self, X):
        # give probability score
        return self.sigmoid(X @ self.theta)

    def predict(self, X):
        # hard yes or no 1 or 0
        return (self.predict_prob(X) >= 0.5).astype(int)

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
