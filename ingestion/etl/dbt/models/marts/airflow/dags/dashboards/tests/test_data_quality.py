import pandas as pd

def test_no_null_user_ids():
    df = pd.read_parquet("data/processed/events")
    assert df["user_id"].isnull().sum() == 0
