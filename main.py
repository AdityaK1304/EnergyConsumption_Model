from src.data_ingestion import data_ingestion
def main():
    df = data_ingestion()
    df = generate_reports(df)
    print(df)


if __name__ == "__main__":
    main()
