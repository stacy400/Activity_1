# Activity 1 — Database Extraction & Transformation

## Summary
This workspace contains a small ETL script (`Activity 1.py`) that extracts data from a local MySQL database, performs a simple transformation, and saves the result to a CSV file (`sales_transformed.csv`).

## Files
- `Activity 1.py` — Connects to MySQL (`sample_db`), runs `SELECT * FROM sales`, computes a `total_sales` column as `quantity * price`, sorts by `total_sales` (descending), and writes the transformed table to `sales_transformed.csv`.
- `sales_transformed.csv` — Output produced by `Activity 1.py` containing the transformed and sorted sales data.

## How to run
1. Ensure MySQL is running and accessible with the credentials configured in `Activity 1.py` (host `localhost`, user `root`, password as set in the script, database `sample_db`).
2. Install required Python packages if not already installed:

```
python -m pip install pandas mysql-connector-python
```

3. Run the script:

```
python "Activity 1.py"
```

After running, `sales_transformed.csv` will be created/overwritten in the workspace.

## Notes & Next Steps
- Credentials are stored in the script for convenience; consider moving them to environment variables or a config file before sharing or deploying.
- Add error handling around the DB connection and SQL query.
- Add a requirements file (`requirements.txt`) or virtual environment for reproducibility.

If you'd like, I can: create `requirements.txt`, remove plaintext credentials, or add more detailed documentation.
