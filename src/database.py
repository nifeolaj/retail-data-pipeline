import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
import pandas as pd


load_dotenv()


def get_database_url():
    """Build the PostgreSQL connection URL from environment variables."""

    return (
        f"postgresql+psycopg://"
        f"{os.getenv('POSTGRES_USER')}:"
        f"{os.getenv('POSTGRES_PASSWORD')}@"
        f"{os.getenv('POSTGRES_HOST')}:"
        f"{os.getenv('POSTGRES_PORT')}/"
        f"{os.getenv('POSTGRES_DB')}"
    )


def get_engine():
    """Create and return a SQLAlchemy database engine."""

    database_url = get_database_url()

    return create_engine(database_url)


def load_data(df: pd.DataFrame, table_name: str = "retail_transactions"):
    """Load a DataFrame into a PostgreSQL table.
       Replace existing table data with the latest dataset.
    """

    engine = get_engine()

    #remove existing data in the table before loading new data
    with engine.begin() as connection:
        connection.execute(text(f"TRUNCATE TABLE {table_name}"))

    df.to_sql(table_name, engine, if_exists="append", index=False)


