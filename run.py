import pandas as pd

# Load the data
data = pd.read_pickle("data/dataset_1.pkl")

if __name__ == "__main__":
    print(data.head())