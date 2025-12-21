import pandas as pd
import numpy as np
import os

def preprocess_data(input_path, output_path):
    df = pd.read_csv(input_path)

    num_cols = df.select_dtypes(include=np.number).columns
    cat_cols = df.select_dtypes(include='object').columns

    df[num_cols] = df[num_cols].fillna(df[num_cols].median())

    for col in cat_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    df = df.drop(columns=['island', 'sex'])

    df.to_csv(output_path, index=False)
    print("Preprocessing selesai. File disimpan di:", output_path)


if __name__ == "__main__":
    input_path = os.path.join("..", "penguins.csv")
    output_path = os.path.join("penguins_preprocessing.csv")
    
    preprocess_data(input_path, output_path)