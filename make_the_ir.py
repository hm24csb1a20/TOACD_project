import joblib
from makesyntaxtree import parse_c_file
from cloadfiles import pareser_to_vector
from ml_data_visualization import FEATURE_LIST
import subprocess
import os
import numpy as np

def generate_ir(file_path,output_dir = "ir_files"):
    """converts c file to LLVM IR using clang"""
    os.makedirs(output_dir, exist_ok=True)
    base_name = os.path.basename(file_path)
    ir_file = os.path.join(output_dir, base_name.replace('.c', '.ll'))
    try:
        subprocess.run(
            ["clang", "-S", "-emit-llvm", file_path, "-o", ir_file],
            check=True
        )
        print(f"IR generated: {ir_file}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to generate IR for {file_path}: {e}")
def valid_c_file(file_path):
    """return false if the file contains any #include line."""
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if line.strip().startswith(("#include","# include")):
                return False
    return True
def check_and_generate_IR(model, file_path, FEATURE_LIST = FEATURE_LIST):
    """chekc if safe then generate IR"""
    node_kinds = parse_c_file(file_path=file_path)
    xvec = pareser_to_vector(node_kinds,FEATURE_LIST).reshape(1,-1)
    pred = model.predict(xvec)[0]
    if(pred==0):
       if(valid_c_file(file_path)):
        print(f" Benign file the IR  is: in the folder")
        generate_ir(file_path)
    else:
        print(f"{file_path} is a malicious file not constructiong compiller")



def randomly_pick_file(RANDOM_SEED,folder_paths = ("benign", "malicious"),max_iter = 20 ):
    """
    randomly picks soem file in the 2 folder "benign", "malicious"

    """
    np.random.seed(RANDOM_SEED)
    fld = np.random.choice(folder_paths)
    current = os.getcwd()
    prefix = os.path.join(current,"cpp_tests",fld)

    # only to pick c files
    c_files = [f for f in os.listdir(prefix) if f.endswith('.c')]
    chosen_file = np.random.choice(c_files)
    final_path = os.path.join(prefix,chosen_file)

    label = 0 if fld == "benign" else 1
    return final_path,label
    
if __name__ == "__main__":
    RANDOM_SEED = 46
    model = joblib.load("final_logreg_model")

    max_iter= 50  
    attempt = 0
    generated = False

    while attempt < max_iter and not generated:
        file_path, label = randomly_pick_file(RANDOM_SEED + attempt)
        node_kinds = parse_c_file(file_path)
        xvec = pareser_to_vector(node_kinds, FEATURE_LIST).reshape(1, -1)
        pred = model.predict(xvec)[0]

        if pred == 0 and valid_c_file(file_path):
            print(f"Selected benign file: {file_path}")
            generate_ir(file_path)
            generated = True
        elif pred==1:
            print(f"MALICIOUS file: {file_path} \n Skipping")
        else:
            print(f"skipped file as #include is proprietary")
        attempt += 1
        print("\n")
    if not generated:
        print("No valid benign file found after max attempts.")