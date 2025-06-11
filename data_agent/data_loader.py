import pandas as pd
from .api_client import get_crypto_data

def load_crypto_dataframe():
    data = get_crypto_data()
    df = pd.DataFrame(data)
    return df[["id", "symbol", "current_price", "market_cap", "price_change_percentage_24h"]]
