from data_agent.data_loader import load_crypto_dataframe

def main():
    df = load_crypto_dataframe()
    print("Available symbols:", ", ".join(df["symbol"].values))

    while True:
        query = input("Enter a crypto symbol (or 'exit'): ").lower()
        if query == "exit":
            break
        result = df[df["symbol"] == query]
        if result.empty:
            print("Symbol not found.")
        else:
            row = result.iloc[0]
            print(f"{row['id'].title()} - Price: ${row['current_price']:.2f}, 24h Change: {row['price_change_percentage_24h']:.2f}%")

if __name__ == "__main__":
    main()
