CREATE TABLE IF NOT EXISTS retail_transactions (
    invoice VARCHAR(50),
    stock_code VARCHAR(50),
    description TEXT,
    quantity INTEGER,
    invoice_date TIMESTAMP,
    price NUMERIC(12, 2),
    customer_id VARCHAR(50),
    country VARCHAR(100),
    is_cancellation BOOLEAN,
    line_total NUMERIC(14, 2)
);