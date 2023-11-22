#!/usr/bin/env python
# coding: utf-8

# In[1]:


def outlier_detection(df):
    """
    Detect potential outliers in a DataFrame using the Interquartile Range (IQR) method.

    Parameters:
    - df (pandas.DataFrame): The input DataFrame containing numerical data.

    Returns:
    - pandas.Series: A Series containing potential outlier values.
    
    The function calculates the first quartile (Q1), third quartile (Q3), and the Interquartile Range (IQR).
    It then identifies potential outliers below the lower bound (Q1 - 1.5 * IQR) or above the upper bound (Q3 + 1.5 * IQR).
    The result is a Series containing the values in the DataFrame that are potential outliers.

    Example:
    >>> data = {'Column1': [2, 4, 5, 7, 8, 9, 10, 11, 12, 50]}
    >>> df = pd.DataFrame(data)
    >>> outlier_detection(df['Column1'])
    Returns:
    9    50
    Name: Column1, dtype: int64
    """
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    upper_end = Q3 + 1.5 * IQR
    lower_end = Q1 - 1.5 * IQR
    outliers = df[(df > upper_end) | (df < lower_end)]
    return outliers
def filter_by_substring(df, column_name, substring, case = True):
    """
    Filter DataFrame rows based on a substring match in a specific column.

    Parameters:
    - df (pandas.DataFrame): The input DataFrame.
    - column_name (str): The name of the column to check for the substring.
    - substring (str): The substring to search for in the specified column.

    Returns:
    - pandas.DataFrame: A DataFrame containing rows where the specified substring is found in the specified column.
    """
    return df[df[column_name].str.contains(substring, case=case)]
def boxplot(data, column_name):
    """
    Create a box plot for a specified column in a DataFrame.

    Parameters:
    - data (pandas.DataFrame): The input DataFrame.
    - column_name (str): The name of the column for which to create the box plot.

    Returns:
    - None

    This function uses Matplotlib and Seaborn to generate a box plot for the specified column.
    """
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=data[column_name])

    # Add labels and a title
    plt.xlabel('Data')
    plt.ylabel('Values')
    plt.title(f'Box Plot for {column_name}')
    plt.grid(True)
    plt.show()
def get_missing_features(data):
    """
    Get the features (columns) in a DataFrame that have missing values.

    Parameters:
    - data (pandas.DataFrame): The input DataFrame.

    Returns:
    - list: A list of feature names with missing values.
    """
    missing_features = data.columns[data.isnull().any()].tolist()
    return missing_features


# In[ ]:




