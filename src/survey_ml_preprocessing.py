import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def preprocess_survey_label_normalized(df, exclude_cols=None):
    if exclude_cols is None:
        exclude_cols = ['Sr.No.', 'Response No']
    df_ml = df.drop(columns=[col for col in exclude_cols if col in df.columns]).copy()
    label_maps = {}
    for col in df_ml.columns:
        if not pd.api.types.is_numeric_dtype(df_ml[col]):
            le = LabelEncoder()
            df_ml[col] = le.fit_transform(df_ml[col].astype(str))
            label_maps[col] = dict(zip(le.classes_, le.transform(le.classes_)))
    scaler = StandardScaler()
    df_norm = pd.DataFrame(scaler.fit_transform(df_ml), columns=df_ml.columns)
    return df_norm, label_maps
