from src.pipeline import extract_data, transform_data
from src.database import load_data


def run_pipeline(file_path: str) -> None:
    """Run the complete retail data pipeline."""

    print("Extracting data...")
    raw_data = extract_data(file_path)

    print("Transforming data...")
    transformed_data = transform_data(raw_data)

    print("Loading data into PostgreSQL...")
    load_data(transformed_data)

    print("Pipeline completed successfully!")


if __name__ == "__main__":
    run_pipeline("data/online_retail_II.xlsx")