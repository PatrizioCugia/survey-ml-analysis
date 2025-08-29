import pandas as pd
import numpy as np

def generate_synthetic_survey(n=100):
    """
    Generates synthetic survey data.
    Args:
        n (int): Number of synthetic responses.
    Returns:
        pd.DataFrame: Synthetic survey dataframe.
    """
    roles = ["Data Scientist", "ML Engineer", "Researcher", "Student"]
    years = ["<1", "1-3", "3-5", "5+"]
    tools = ["TensorFlow", "PyTorch", "Scikit-learn", "None"]
    hardware = ["GPU", "CPU", "TPU"]
    data = {
        "What is your primary role?": np.random.choice(roles, n),
        "How many years have you been working with machine learning?": np.random.choice(years, n),
        "Preferred ML library": np.random.choice(tools, n),
        "Main hardware used": np.random.choice(hardware, n),
    }
    return pd.DataFrame(data)
