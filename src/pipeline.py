import pandas as pd

def extract_data(file_path: str) -> pd.DataFrame:
    """Read raw retail data from an Excel file."""

    return pd.read_excel(file_path)


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and transform raw retail transaction data.
    
    1. Rename columns to consistent snake_case
    2. Convert customer_id to a nullable string type
    3. Make sure invoice_date is a proper datetime
    4. Add is_cancellation based on invoices beginning with C
    5. Add line_total = quantity × price
    6. Keep missing values rather than inventing data
    7. Keep unusual/negative values rather than silently deleting them
    8. Don't remove duplicates
    """

    df = df.copy()

    # Standardize column names
    df = df.rename(columns={
            "Invoice": "invoice",
            "StockCode": "stock_code",
            "Description": "description",
            "Quantity": "quantity",
            "InvoiceDate": "invoice_date",
            "Price": "price",
            "Customer ID": "customer_id",
            "Country": "country",
        }
    )

    # Convert data types
    df["invoice_date"] = pd.to_datetime(df["invoice_date"])
    df["customer_id"] = df["customer_id"].astype("Int64").astype("string")
    df["invoice"] = df["invoice"].astype("string")
    df["stock_code"] = df["stock_code"].astype("string")

    # Flag cancellations
    df["is_cancellation"] = df["invoice"].str.startswith("C")

    # Calculate transaction value
    df["line_total"] = df["quantity"] * df["price"]

    return df

