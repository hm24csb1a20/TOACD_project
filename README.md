# TOACD_project

# 🧩 Malware Detection using Machine Learning

---

## 🧠 Overview

This project aims to detect whether a given piece of code is **malicious or benign** using machine learning.  
We started simple — with a **logistic regression model** — and are now moving toward more powerful **tree-based classifiers** like Random Forest.

---

## 📦 Data Collection — the first big hurdle

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

## ⚙️ Data Loader

We wrote a **custom loader** that reads all the `.c` / `.cpp` / `.py` files,  
cleans them, tokenizes them, and transforms the code into a **vectorized form** suitable for ML models (using something like TF-IDF).

Example workflow:
```python
X, y, vectorizer = prepare_dataset(benign_path, malicious_path)
