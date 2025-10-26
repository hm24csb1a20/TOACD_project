import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_curve, auc
from joblib import dump, load
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import HtmlFormatter

# --- 1. CONFIGURATION AND UTILITIES ---

# Placeholder for feature definition (matching the image)
FEATURE_DEFINITIONS = {
    "embedded_code": "Indicator of suspicious embedded or obfuscated code patterns.",
    "backdoor_marker": "Presence of typical backdoor entry points or hardcoded C2.",
    "command_injection": "Use of suspicious `system()`, `popen()`, `exec*` calls with untrusted inputs.",
    "buffer_overflow": "Usage of unsafe string/memory functions like `gets()`, `strcpy()`, `sprintf()`.",
    "memory_corruption": "Indicators of manual, suspicious memory allocation/deallocation patterns.",
    "path_hijacking": "Suspicious file path handling or use of relative paths in security-sensitive areas."
}

# Placeholder function for complex logic (to be implemented in feature_extractor.py)
@st.cache_data
def load_sample_data():
    """Generates or loads a minimal toy dataset."""
    st.write("Loading toy dataset...")
    # This data is completely synthetic and for demonstration only.
    data = {}
    for feature in FEATURE_DEFINITIONS:
        data[feature] = np.random.randint(0, 5, 100)
    data['target'] = np.random.choice([0, 1], 100, p=[0.7, 0.3]) # 0: Benign, 1: Malicious
    df = pd.DataFrame(data)
    return df.astype({'target': 'int'})

# Placeholder for feature_extractor.py functions
def extract_features_from_c_file(c_code: str):
    """
    Conceptual function to interface with clang and extract features.
    
    You must implement the logic to run clang subprocess (or libclang),
    parse the AST/IR, and map constructs to numeric features.
    """
    st.info("⚠️ Simulating clang compilation and feature extraction...")
    # Simulate extraction success and return features
    features = {f: np.random.randint(0, 5) for f in FEATURE_DEFINITIONS}
    
    # Example for IR/AST output
    ir_output = "Conceptual Clang AST/IR snippet:\nTranslationUnitDecl 0x... <line:1:1, line:10:1>...\nFunctionDecl 0x... 'main' 'int ()'...\n"
    
    # Simulate a compile error for demonstration
    if 'gets(' in c_code: # A simple heuristic for a compile "error"
        raise Exception("Clang error: Usage of deprecated and unsafe function 'gets()' detected.")

    return pd.Series(features).to_frame().T, ir_output

# Placeholder for a loaded model (Train it in 'Modeling' section first)
MODEL = None

# --- 2. STREAMLIT APP LAYOUT ---

st.set_page_config(layout="wide", page_title="Malicious C Code Detector (ML-Based Static Analysis)")

st.title("🤖 ML-Based Malicious C Code Detection")
st.subheader("Leveraging Static Analysis & Parser Tree Features for Security")

st.markdown("""---""")

## Overview & Feature Explanation

st.header("1️⃣ Overview & Feature Explanation")

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("**Core Idea:** We classify C source files as benign or malicious by extracting a set of static, CWE-like features, then training a classifier (LR/RF) on these numerical indicators.")
    st.image("https://i.imgur.com/G5qWv4D.png", caption="Conceptual Feature Set (CWE-like Indicators)", use_column_width=True) # Replace with local image path if possible
    
with col2:
    st.subheader("Feature Schema & Explanation")
    st.markdown("The model uses **counts and presence markers** corresponding to common security vulnerabilities and malicious indicators:")
    
    features_df = pd.DataFrame({
        "Feature Field": FEATURE_DEFINITIONS.keys(),
        "Description": FEATURE_DEFINITIONS.values()
    })
    st.table(features_df)

st.markdown("""---""")

## Data + Visualization

st.header("2️⃣ Data + Visualization")

st.info("💡 Data is synthetic for demonstration. Feature values represent counts or binary presence markers.")

df = load_sample_data()
st.session_state['df'] = df # Store for later use

st.subheader("Dataset Structure")
st.dataframe(df.head())
st.write(f"Dataset Shape: **{df.shape}**")

# Interactive Visualizations
st.subheader("Interactive Visualizations")

tab_dist, tab_corr, tab_pair = st.tabs(["Class Balance & Distributions", "Correlation Heatmap", "Pair Plot"])

with tab_dist:
    st.markdown("**Class Balance:** (0: Benign, 1: Malicious)")
    fig_class = px.histogram(df, x='target', color='target', title='Target Class Distribution')
    st.plotly_chart(fig_class, use_container_width=True)
    
    st.markdown("**Feature Distributions by Class:**")
    feature_to_plot = st.selectbox("Select Feature to Visualize Distribution", list(FEATURE_DEFINITIONS.keys()))
    fig_feat = px.histogram(df, x=feature_to_plot, color='target', marginal='box', barmode='group', title=f'{feature_to_plot} Distribution by Target')
    st.plotly_chart(fig_feat, use_container_width=True)

with tab_corr:
    st.markdown("**Feature Correlation Heatmap:** (Identify highly correlated features)")
    corr_matrix = df.drop(columns=['target']).corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm')
    st.pyplot(plt)

with tab_pair:
    st.markdown("**Feature Pair Plot:** (Visualize feature interactions across classes - takes time for many features)")
    features_for_pairplot = st.multiselect("Select up to 4 features for Pair Plot", list(FEATURE_DEFINITIONS.keys()), default=list(FEATURE_DEFINITIONS.keys())[:4])
    if features_for_pairplot:
        # Use a subset for performance
        fig_pair = sns.pairplot(df, vars=features_for_pairplot, hue='target', markers=["o", "s"], diag_kind="kde")
        st.pyplot(fig_pair)

# Code Viewer
st.subheader("C Code Viewer")
code_example = st.selectbox("Select Sample C File to View", ["benign_example.c", "malicious_example.c"])

# Placeholder for reading C file content
if code_example == "benign_example.c":
    c_code = """
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    // A standard, benign C program
    printf("Hello, Secure World!\\n");
    if (argc > 1) {
        printf("Received argument: %s\\n", argv[1]);
    }
    return 0;
}
"""
else:
    c_code = """
#include <stdio.h>
#include <stdlib.h>

// CWE-78: Improper Neutralization of Special Elements used in an OS Command ('system')
void run_command(char *input) {
    char command[100];
    sprintf(command, "echo input: %s", input);
    system(command); // Suspicious system call
}

int main(int argc, char *argv[]) {
    if (argc > 1) {
        run_command(argv[1]);
    }
    // Hardcoded credentials - CWE-798
    char *password = "supersecret123"; 
    printf("Password check complete.\\n");
    return 0;
}
"""

# Pygments for syntax highlighting
lexer = CLexer()
formatter = HtmlFormatter(style='monokai', full=True, linenos=True)
html_code = highlight(c_code, lexer, formatter)

st.components.v1.html(html_code, height=400, scrolling=True)

st.markdown("""---""")

## Modeling & Training

st.header("3️⃣ Modeling & Training")

if 'df' not in st.session_state:
    st.warning("Please load data first.")
else:
    X = st.session_state['df'].drop(columns=['target'])
    y = st.session_state['df']['target']

    st.markdown("""
    **Model Rationale:**
    1. **Logistic Regression (LR):** Used as a simple, interpretable baseline model. It performs well when data is linearly separable and provides easily-understood feature coefficients (rationale).
    2. **Random Forest (RF):** A powerful ensemble method. It typically performs better on complex, non-linear data. However, for a **small, synthetic dataset**, complex models like RF can easily **overfit** and may show poor generalization compared to the simpler LR.
    """)

    # Model Controls
    with st.form("training_form"):
        st.subheader("Training Parameters")
        
        col_model, col_split, col_cv = st.columns(3)
        
        with col_model:
            model_name = st.selectbox("Select Model", ["Logistic Regression", "Random Forest"])
        with col_split:
            test_size = st.slider("Train/Test Split (%)", 10, 50, 20) / 100
        with col_cv:
            cv_folds = st.slider("Cross-Validation Folds (k)", 2, 10, 5)

        # Hyperparameter tuning (simplified)
        if model_name == "Logistic Regression":
            C_param = st.slider("Regularization Strength (C)", 0.01, 10.0, 1.0, 0.01)
            model = LogisticRegression(C=C_param, max_iter=1000, random_state=42)
        else: # Random Forest
            n_estimators = st.slider("Number of Trees", 10, 200, 100, 10)
            max_depth = st.slider("Max Depth", 2, 20, 10)
            model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)

        train_button = st.form_submit_button("🚀 Train Model")

    if train_button:
        with st.spinner(f"Training {model_name}..."):
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42, stratify=y)
            
            # Training
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            y_proba = model.predict_proba(X_test)[:, 1]
            
            # Cross-Validation
            cv_scores = cross_val_score(model, X, y, cv=cv_folds, scoring='accuracy')

            st.session_state['trained_model'] = model
            st.session_state['model_name'] = model_name
            
            # --- Results Display ---
            st.subheader("Training Results")

            col_met, col_cv = st.columns(2)
            
            with col_met:
                st.metric("Accuracy", f"{accuracy_score(y_test, y_pred):.4f}")
                st.metric("Precision", f"{precision_score(y_test, y_pred):.4f}")
                st.metric("Recall", f"{recall_score(y_test, y_pred):.4f}")
                st.metric("F1 Score", f"{f1_score(y_test, y_pred):.4f}")

            with col_cv:
                st.metric(f"{cv_folds}-Fold CV Accuracy (Mean)", f"{cv_scores.mean():.4f}")
                st.metric(f"{cv_folds}-Fold CV Accuracy (Std Dev)", f"{cv_scores.std():.4f}")
                
                # Save model logic (conceptual)
                dump(model, 'best_model.joblib')
                st.success("Model trained and (conceptually) saved to `best_model.joblib`")
            
            # Confusion Matrix
            cm = confusion_matrix(y_test, y_pred)
            fig_cm, ax_cm = plt.subplots()
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax_cm, 
                        xticklabels=['Benign (0)', 'Malicious (1)'], 
                        yticklabels=['Benign (0)', 'Malicious (1)'])
            ax_cm.set_title("Confusion Matrix")
            ax_cm.set_ylabel('True Label')
            ax_cm.set_xlabel('Predicted Label')
            st.pyplot(fig_cm)
            
            # ROC Curve
            fpr, tpr, thresholds = roc_curve(y_test, y_proba)
            roc_auc = auc(fpr, tpr)
            fig_roc, ax_roc = plt.subplots()
            ax_roc.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
            ax_roc.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
            ax_roc.set_xlim([0.0, 1.0])
            ax_roc.set_ylim([0.0, 1.05])
            ax_roc.set_xlabel('False Positive Rate')
            ax_roc.set_ylabel('True Positive Rate')
            ax_roc.set_title('Receiver Operating Characteristic')
            ax_roc.legend(loc="lower right")
            st.pyplot(fig_roc)
            
            # Feature Importance
            st.subheader("Feature Importance / Coefficients")
            if model_name == "Logistic Regression":
                coef_df = pd.DataFrame({'Feature': X.columns, 'Coefficient': model.coef_[0]})
                coef_df['Abs_Coefficient'] = coef_df['Coefficient'].abs()
                coef_df = coef_df.sort_values(by='Abs_Coefficient', ascending=False)
            else: # Random Forest
                coef_df = pd.DataFrame({'Feature': X.columns, 'Importance': model.feature_importances_})
                coef_df = coef_df.sort_values(by='Importance', ascending=False)
                
            fig_feat_imp = px.bar(coef_df, x='Feature', y=coef_df.columns[1], title=f"{model_name} Feature {coef_df.columns[1]}")
            st.plotly_chart(fig_feat_imp, use_container_width=True)


st.markdown("""---""")

## Compile / Parser / Prediction & IR

st.header("4️⃣ Prediction Demo: Compile, Extract Features, and Predict")

if 'trained_model' not in st.session_state:
    st.warning("Please train a model in Section 3 first.")
else:
    
    st.subheader(f"Using Trained Model: **{st.session_state['model_name']}**")
    
    # File selection/upload
    code_for_pred = st.text_area("Paste C Source Code Here (or select a sample)", value=c_code, height=300)

    predict_button = st.button("🔬 Analyze & Predict")
    
    if predict_button:
        try:
            with st.spinner("Running clang frontend and extracting features..."):
                # 1. Feature Extraction
                features_df, ir_output = extract_features_from_c_file(code_for_pred)
                
                st.success("Feature extraction successful!")
                st.subheader("Extracted Features")
                st.dataframe(features_df)
                
                # 2. Prediction
                model = st.session_state['trained_model']
                prediction = model.predict(features_df)[0]
                probability = model.predict_proba(features_df)[0]
                
                
                # 3. Rationale (Top Contributing Features)
                rationale_list = []
                if st.session_state['model_name'] == "Logistic Regression":
                    coefs = model.coef_[0]
                    # Simple scoring by multiplying feature value by coefficient
                    scores = features_df.iloc[0] * coefs
                    top_features = scores.abs().sort_values(ascending=False).head(3)
                    rationale_list = [f"**{feat}**: Score contribution of {score:.2f}" for feat, score in top_features.items()]
                else: # Random Forest - use feature importance from training
                    # Use feature values and importance heuristically
                    importances = pd.Series(model.feature_importances_, index=features_df.columns)
                    top_features = importances.sort_values(ascending=False).head(3)
                    rationale_list = [f"**{feat}**: High feature value ({features_df.iloc[0][feat]}) combined with high importance ({imp:.2f})" for feat, imp in top_features.items()]

                # 4. Display Results
                st.subheader("Prediction Result")
                
                is_malicious = prediction == 1
                
                if is_malicious:
                    st.error(f"🔴 CLASSIFIED AS **MALICIOUS**")
                else:
                    st.success(f"🟢 CLASSIFIED AS **BENIGN**")
                    
                st.metric("Probability (Malicious)", f"{probability[1]*100:.2f}%")
                
                st.markdown("**Top Rationale (Contributing Features):**")
                for rationale in rationale_list:
                    st.markdown(f"- {rationale}")
                    
                # 5. Export IR / Intermediate features
                st.subheader("Intermediate Output")
                
                col_ir, col_feat = st.columns(2)
                with col_ir:
                    st.code(ir_output, language='text', height=200)
                    st.download_button("Download Conceptual AST/IR", ir_output, file_name="ast_ir_output.txt")
                with col_feat:
                    st.dataframe(features_df)
                    st.download_button("Download Extracted Features (CSV)", features_df.to_csv(index=False).encode('utf-8'), file_name="extracted_features.csv")

        except Exception as e:
            st.error(f"🛑 **Analysis Error:** Failed to compile or extract features. Ensure `clang` is installed and the code is valid C.")
            st.exception(e)