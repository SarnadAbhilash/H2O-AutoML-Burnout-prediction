import pandas as pd
import h2o
from h2o.automl import H2OAutoML

def train_h2o():
    """
    Function to train the model using H2o auto ML
    """

    train = h2o.import_file("data/train.csv")
    train_as_df = h2o.as_list(train,use_pandas=True)
    train_as_df = train_as_df[train_as_df['Burn Rate'].notna()]
    train_as_df = train_as_df[train_as_df['Mental Fatigue Score'].notna()]
    train_as_df = train_as_df[train_as_df['Resource Allocation'].notna()]
    train = h2o.H2OFrame(train_as_df)
    x = train.columns
    y = "Burn Rate"
    x.remove(y)

    aml = H2OAutoML(max_models=10, seed=1)
    aml.train(x=x, y=y, training_frame=train)

    return aml

if __name__ == "__main__":
    train_h2o()