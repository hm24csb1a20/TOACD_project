from cloadfiles import make_the_ml_datasets
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from logistic_regression import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score



def logistic_regressoin_classificaton(random_seed =42):
    X,y=make_the_ml_datasets(random_seed=random_seed)
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size= 0.2, stratify=y)

    model = LogisticRegression(random_seed=random_seed)
    model.fit(X=X_train,y=y_train)
    y_pred = model.predict(X_test)
    acc= accuracy_score(y_pred=y_pred,y_true=y_test)
    print(acc)

logistic_regressoin_classificaton(random_seed=42)



