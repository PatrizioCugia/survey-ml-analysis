import pandas as pd

def survey_clean(file_path):
    """
    Reads and cleans the survey data.
    Args:
        file_path (str): Path to CSV file.
    Returns:
        pd.DataFrame: Cleaned dataframe.
    """
    df = pd.read_csv(file_path)
    # Example cleaning: drop NaNs, remove duplicate responses, etc.
    df = df.dropna(how='all')  # Remove completely empty rows
    df = df.drop_duplicates()  # Remove duplicates
    # Add more cleaning steps as needed!
    return df
