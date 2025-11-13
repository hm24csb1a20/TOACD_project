import os 
import pandas as pd
import numpy as np
from makesyntaxtree import parse_c_file
from collections import Counter
from itertools import chain
# predined to save time 
FEATURE_LIST = ['ARRAY_SUBSCRIPT_EXPR', 'ASM_LABEL_ATTR', 'BINARY_OPERATOR',
                 'BREAK_STMT', 'CALL_EXPR', 'CASE_STMT', 'CHARACTER_LITERAL',
                   'COMPOUND_ASSIGNMENT_OPERATOR', 'COMPOUND_LITERAL_EXPR', 'COMPOUND_STMT',
                     'CONDITIONAL_OPERATOR', 'CONTINUE_STMT', 'CSTYLE_CAST_EXPR', 'CXX_UNARY_EXPR',
                       'DECL_REF_EXPR', 'DECL_STMT', 'DEFAULT_STMT', 'DO_STMT', 'ENUM_CONSTANT_DECL'
                         'ENUM_DECL', 'FIELD_DECL', 'FLOATING_LITERAL', 'FOR_STMT', 'FUNCTION_DECL',
                           'GOTO_STMT', 'IF_STMT', 'INIT_LIST_EXPR', 'INTEGER_LITERAL', 'LABEL_REF',
                             'LABEL_STMT', 'MEMBER_REF', 'MEMBER_REF_EXPR', 'NULL_STMT', 'PAREN_EXPR',
                               'PARM_DECL', 'RETURN_STMT', 'STATIC_ASSERT', 'STRING_LITERAL', 'STRUCT_DECL',
                                 'SWITCH_STMT', 'TRANSLATION_UNIT', 'TYPEDEF_DECL', 'TYPE_REF', 'UNARY_OPERATOR', 
                                 'UNEXPOSED_ATTR', 'UNEXPOSED_DECL', 'UNEXPOSED_EXPR', 'UNION_DECL', 'VAR_DECL',
                                   'WHILE_STMT']


def getallfields(file_path):
    """
    if given {"benign"} or {"malicious"} gets all the filenames of those files"""
    current = os.getcwd()
    root = os.path.join(current,"cpp_tests",file_path)
    return os.listdir(root)
  
def parse_all_files(file_path):
    """"
    if given {"benign"} or {"malicious"} gets the parses of all those"""
    suffixes = [f for f in getallfields(file_path) if f.endswith('.c')]
    root = os.path.join(os.getcwd(),"cpp_tests",file_path)
    results =[]
    for i in suffixes:
        results.append(parse_c_file(os.path.join(root,i)))
    return (results)
def vectorize_parse_all_files(file_path,FEATURE_LIST = FEATURE_LIST):
    """"
    if given {"benign"} or {"malicious"} gets the parses of all those"""
    suffixes = getallfields(file_path)
    root = os.path.join(os.getcwd(),"cpp_tests",file_path)
    results =[]
    for i in suffixes:
        results.append(parser_to_vector(parse_c_file(os.path.join(root,i)),FEATURE_LIST))
    return np.array(results)

def parser_to_vector(node_kinds,FEATURE_LIST = FEATURE_LIST):
    # gives dictionary of all the words and their freq
    features = Counter(node_kinds)
    return np.array([features.get(k, 0) for k in FEATURE_LIST])

def makeFEATURELIST( file_path1="benign",file_path2="malicious"):
    """
    first time running program made this to get the hyperparameter 
    FEATURE_LIST"""
    benign_featrues = parse_all_files(file_path1)  
    malicious_features =parse_all_files(file_path2)
    all_features = benign_featrues+malicious_features  

    temp = set(chain.from_iterable(all_features))
    FEATURE_LIST = sorted(temp)
    return(FEATURE_LIST)

def make_the_ml_datasets(random_seed=42,file_path1="benign",file_path2="malicious"):
    np.random.seed(random_seed)
    # FEATURE_LIST = makeFEATURELIST(file_path1,file_path2)
    benign_vectors =vectorize_parse_all_files(file_path1,FEATURE_LIST)
    malicious_vectors = vectorize_parse_all_files(file_path2,FEATURE_LIST)
    # labelling for making y 
    benign_labels = np.zeros(len(benign_vectors), dtype=int)       # 0 = benign
    malicious_labels = np.ones(len(malicious_vectors), dtype=int)  # 1 = malicious
    X = np.vstack([benign_vectors, malicious_vectors])
    y = np.concatenate([benign_labels, malicious_labels])

    n = np.arange(X.shape[0])
    np.random.shuffle(n)
    # now not just all benign then all malicious 
    # now random
    X = X[n]
    y = y[n]
    return X,y





if __name__ =="__main__":
    # current = os.path.dirname(os.path.abspath(__file__))
    # file_path = os.path.join(current, "cpp_tests", "benign","__cos.c")
    # node_kinds = parse_c_file(file_path=file_path)
    # print(pareser_to_vector(node_kinds))

    # the first time u run the program make the feture list 
    # computationally expnesive so predefining in my case
    # FEATURE_LIST = makeFEATURELIST("benign","malicious")
    print(make_the_ml_datasets())
