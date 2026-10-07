import pandas as pd

from src.pipeline import transform_data


def test_line_total():
    df = pd.DataFrame({
        "Invoice": ["12345"],
        "StockCode": ["ABC"],
        "Description": ["Test product"],
        "Quantity": [5],
        "InvoiceDate": ["2010-01-01"],
        "Price": [2.0],
        "Customer ID": [12345],
        "Country": ["United Kingdom"]
    })

    result = transform_data(df)

    assert result.loc[0, "line_total"] == 10.0


def test_cancellation_flag():
    df = pd.DataFrame({
        "Invoice": ["C12345"],
        "StockCode": ["ABC"],
        "Description": ["Test product"],
        "Quantity": [-2],
        "InvoiceDate": ["2010-01-01"],
        "Price": [5.0],
        "Customer ID": [12345],
        "Country": ["United Kingdom"]
    })

    result = transform_data(df)

    assert result.loc[0, "is_cancellation"] == True


def test_customer_id_is_string():
    df = pd.DataFrame({
        "Invoice": ["12345"],
        "StockCode": ["ABC"],
        "Description": ["Test product"],
        "Quantity": [2],
        "InvoiceDate": ["2010-01-01"],
        "Price": [5.0],
        "Customer ID": [12345],
        "Country": ["United Kingdom"]
    })

    result = transform_data(df)

    assert result.loc[0, "customer_id"] == "12345"