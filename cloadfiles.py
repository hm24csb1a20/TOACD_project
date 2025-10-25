import os 
import pandas as pd
import numpy as np
from makesyntaxtree import parse_c_file
from collections import Counter
from itertools import chain

FEATURE_LIST = ['ARRAY_SUBSCRIPT_EXPR', 'BINARY_OPERATOR', 'BREAK_STMT', 'CALL_EXPR', 'CASE_STMT', 'CHARACTER_LITERAL',
                 'COMPOUND_ASSIGNMENT_OPERATOR', 'COMPOUND_LITERAL_EXPR', 'COMPOUND_STMT', 'CONDITIONAL_OPERATOR', 'CONTINUE_STMT',
                   'CSTYLE_CAST_EXPR', 'CXX_UNARY_EXPR', 'DECL_REF_EXPR', 'DECL_STMT', 'DEFAULT_STMT', 'DO_STMT', 'ENUM_CONSTANT_DECL', 'ENUM_DECL', 
                   'FIELD_DECL', 'FLOATING_LITERAL', 'FOR_STMT', 'FUNCTION_DECL', 'GOTO_STMT', 'IF_STMT', 'INIT_LIST_EXPR', 'INTEGER_LITERAL', 'LABEL_REF',
                     'LABEL_STMT', 'MEMBER_REF_EXPR', 'NULL_STMT', 'PAREN_EXPR', 'PARM_DECL', 'RETURN_STMT', 'STATIC_ASSERT', 'STRING_LITERAL', 'STRUCT_DECL',
                       'SWITCH_STMT', 'TRANSLATION_UNIT', 'TYPEDEF_DECL', 'TYPE_REF', 'UNARY_OPERATOR', 'UNEXPOSED_ATTR', 'UNEXPOSED_DECL', 'UNEXPOSED_EXPR',
                         'UNION_DECL', 'VAR_DECL', 'WHILE_STMT']

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
    return (results)

def pareser_to_vector(node_kinds):
    # gives dictionary of all the words and their freq
    features = Counter(node_kinds)
    return np.array([features.get(k, 0) for k in features])

def makeFEATURELIST(filepaht1,filepaht2):
    benign_featrues = parse_all_files(filepaht1)  
    malicious_features =parse_all_files(filepaht2)
    all_features = benign_featrues+malicious_features  

    temp = set(chain.from_iterable(all_features))
    FEATURE_LIST = sorted(temp)
    return(FEATURE_LIST)


if __name__ =="__main__":

    # current = os.path.dirname(os.path.abspath(__file__))
    # file_path = os.path.join(current, "cpp_tests", "benign","__cos.c")
    # node_kinds = parse_c_file(file_path=file_path)
    # print(pareser_to_vector(node_kinds))

    # the first time u run the program make the feture list 
    # computationally expnesive so predefining in my case
    FEATURE_LIST = makeFEATURELIST("benign","malicious")
