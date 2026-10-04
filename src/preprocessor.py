import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import (OneHotEncoder,StandardScaler)
def make_preprocessor(transaction ):
    data= pd.DataFrame(transaction)
    cat_cols=[col for col in data.columns if data[col].dtype == 'str']
    num_cols=[col for col in data.columns if data[col].dtype in ['int64', 'float64']]
    preprocessor =ColumnTransformer(
        transformers=[
            ('num',StandardScaler(),num_cols),
            ('cat',OneHotEncoder(handle_unknown='ignore'),cat_cols)
        ],
        remainder='passthrough')
    
    return preprocessor
    