from c_file_classifcation import logistic_regressoin_classificaton
import joblib

if (__name__=="__main__"):
    model = logistic_regressoin_classificaton()
    joblib.dump(model,"final_logreg_model")
    print("model saved in cache")