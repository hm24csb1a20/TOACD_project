from cloadfiles import make_the_ml_datasets,FEATURE_LIST
import matplotlib.pyplot as plt
if __name__ =="__main__":
    X,y= make_the_ml_datasets()
    n_col = X.shape[1]
    
    X_b = X[y==0]
    X_m= X[y==1]
    # usally axis =1 so col elemnt of a row
    fX_b = X_b.sum(axis=0)
    fX_m = X_m.sum(axis=0)

    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    axes[0].bar(range(n_col),fX_b)
    axes[0].set_xticks(range(n_col))
    axes[0].set_xticklabels(FEATURE_LIST,rotation=-90)
    axes[0].set_title("benign")


    axes[1].bar(range(n_col),fX_m)
    axes[1].set_xticks(range(n_col))
    axes[1].set_xticklabels(FEATURE_LIST,rotation=-90)
    axes[1].set_title("malicious")

    plt.tight_layout()
    plt.show()