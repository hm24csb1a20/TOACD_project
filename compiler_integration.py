import joblib
from makesyntaxtree import parse_c_file
from cloadfiles import parser_to_vector
from ml_data_visualization import FEATURE_LIST
import subprocess
import os
import numpy as np
import re

def generate_ir(file_path,output_dir = "ir_files"):
    """converts c file to LLVM IR using clang"""
    os.makedirs(output_dir, exist_ok=True)
    base_name = os.path.basename(file_path)
    ir_file = os.path.join(output_dir, base_name.replace('.c', '.ll'))
    try:
        out = file_path.replace(".c", ".exe")
        subprocess.run(["clang", file_path, "-o", out], check=True)
        subprocess.run([out], check=True)

    except subprocess.CalledProcessError as e:
        print(f"Failed to generate IR for {file_path}: {e}")


def valid_c_file(file_path):
    """
    Allow only safe system headers.
    
    Note: #include "libm.h" and #inckyde <libm.h> are not same.
    "libm.h" could be any file in the system while <libm.h> is a secure library
    """
    SAFE_HEADERS = {
    "<assert.h>",
    "<complex.h>",
    "<ctype.h>",
    "<errno.h>",
    "<fenv.h>",
    "<float.h>",
    "<inttypes.h>",
    "<iso646.h>",
    "<limits.h>",
    "<locale.h>",
    "<math.h>",
    "<setjmp.h>",
    "<signal.h>",
    "<stdalign.h>",
    "<stdarg.h>",
    "<stdatomic.h>",
    "<stdbool.h>",
    "<stddef.h>",
    "<stdint.h>",
    "<stdio.h>",
    "<stdlib.h>",
    "<stdnoreturn.h>",
    "<string.h>",
    "<tgmath.h>",
    "<threads.h>",
    "<time.h>",
    "<uchar.h>",
    "<wchar.h>",
    "<wctype.h>",
    "<libm.h>"
}


    INCLUDE_PATTERN = re.compile(r'#\s*include\s*([<"].+[>"])')
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            match = INCLUDE_PATTERN.match(line.strip())
            if match:
                header = match.group(1)
                if header not in SAFE_HEADERS:
                    print(f"[!] Rejected UNSAFE header: {header}")
                    return False

    return True


def check_and_generate_IR(model, file_path, FEATURE_LIST = FEATURE_LIST):
    """chekc if safe then generate IR"""
    node_kinds = parse_c_file(file_path=file_path)
    xvec = parser_to_vector(node_kinds,FEATURE_LIST).reshape(1,-1)
    pred = model.predict(xvec)[0]
    if(pred==0):
       if(valid_c_file(file_path)):
        print("The file is benign and not harmful")
        print("OUTPUT: ")
        generate_ir(file_path)
    else:
        print(f"{file_path} is a malicious file thus not proceeding with compilation")



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
    
    file_path = r"C:\Users\prana\TOACD\TOACD_project\cpp_tests\benign\fibonacci.c"
    node_kinds = parse_c_file(file_path)
    xvec = parser_to_vector(node_kinds, FEATURE_LIST).reshape(1, -1)
    pred = model.predict(xvec)[0]
    if pred == 0 and valid_c_file(file_path):
        print(f"Selected benign file: {file_path}")
        generate_ir(file_path)
        generated = True
    elif pred==1:
        print(f"MALICIOUS file: {file_path} \n Skipping")
    else:
        print(f"skipped file as #include is proprietary")

    # max_iter= 50  
    # attempt = 0
    # generated = False

    # while attempt < max_iter and not generated:
    #     file_path, label = randomly_pick_file(RANDOM_SEED + attempt)
    #     node_kinds = parse_c_file(file_path)
    #     xvec = parser_to_vector(node_kinds, FEATURE_LIST).reshape(1, -1)
    #     pred = model.predict(xvec)[0]

    #     if pred == 0 and valid_c_file(file_path):
    #         print(f"Selected benign file: {file_path}")
    #         generate_ir(file_path)
    #         generated = True
    #     elif pred==1:
    #         print(f"MALICIOUS file: {file_path} \n Skipping")
    #     else:
    #         print(f"skipped file as #include is proprietary")
    #     attempt += 1
    #     print("\n")
    # if not generated:
    #     print("No valid benign file found after max attempts.")