import os
from sklearn.feature_extraction.text import CountVectorizer

def load_ll_files(folder_path, label):
    codes = []
    labels = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".ll"):  # only process .ll files
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as f:
                codes.append(f.read())
                labels.append(label)
    return codes, labels

def prepare_dataset(benign_folder, malicious_folder):
    benign_codes, benign_labels = load_ll_files(benign_folder, 0)
    malicious_codes, malicious_labels = load_ll_files(malicious_folder, 1)
    
    # combine all data
    X_text = benign_codes + malicious_codes
    y = benign_labels + malicious_labels
    
    # simple vectorization
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(X_text)
    
    return X, y, vectorizer
