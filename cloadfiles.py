import os 
import pandas as pd
import numpy as np
from makesyntaxtree import parse_c_file


def getallfiels(file_path):
    """
    if given {"benign"} or {"malicious"} gets all the filenames of those files"""
    current = os.getcwd()
    root = os.path.join(current,"cpp_tests",file_path)
    return os.listdir(root)

def parse_all_files(file_path):
    """"
    if given {"benign"} or {"malicious"} gets the parses of all those"""
    suffixes = getallfiels(file_path)
    root = os.path.join(os.getcwd(),"cpp_tests",file_path)
    results =[]
    for i in suffixes:
        results.append(parse_c_file(os.path.join(root,i)))
    return np.array(results)

parse_all_files("benign")    