import pandas as pd
from data_agent.data_loader import load_crypto_dataframe

def test_dataframe_structure():
    df = load_crypto_dataframe()
    assert isinstance(df, pd.DataFrame)
    assert all(col in df.columns for col in ["id", "symbol", "current_price", "market_cap", "price_change_percentage_24h"])
    assert not df.empty
