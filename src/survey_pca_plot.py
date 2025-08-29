import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import pandas as pd

def plot_pca_projection(df_norm, color_by=None, original_df=None):
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(df_norm)

    plt.figure(figsize=(8,6))
    if color_by and original_df is not None and color_by in original_df.columns:
        groups = original_df[color_by].astype(str).values
        unique_groups = pd.Series(groups).unique()
        colors = plt.cm.get_cmap("tab10", len(unique_groups))
        for idx, group in enumerate(unique_groups):
            mask = groups == group
            plt.scatter(X_pca[mask, 0], X_pca[mask, 1], 
                        label=group, alpha=0.7, s=40, color=colors(idx))
        plt.legend(title=color_by)
    else:
        plt.scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.7, s=40)
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.title("Survey responses projected onto first two principal components")
    plt.tight_layout()
    plt.show()
