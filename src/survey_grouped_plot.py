import matplotlib.pyplot as plt

def plot_group_answers(df, group_col, group_value, answer_col):
    """
    Bar plot of answers for a specific group.
    Args:
        df (pd.DataFrame): Survey dataframe.
        group_col (str): Column to group by.
        group_value (str): Value to filter the group.
        answer_col (str): Column to plot.
    """
    filtered = df[df[group_col] == group_value]
    counts = filtered[answer_col].value_counts()
    counts.plot(kind='bar')
    plt.title(f"{answer_col} distribution for {group_value} in {group_col}")
    plt.ylabel("Count")
    plt.xlabel(answer_col)
    plt.tight_layout()
    plt.show()
