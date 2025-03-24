from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table,inspect
import pandas as pd


# Create an SQLite database connection
engine = create_engine("sqlite:///test.db")
metadata = MetaData()

# # Define a sample table
users = Table(
    "users", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("age", Integer)
)

# # Create the table in the database
metadata.create_all(engine)

print("Database and table created successfully!")


# Use SQLAlchemy Inspector to check tables
inspector = inspect(engine)
tables = inspector.get_table_names()

# Check if "users" table exists
if "users" in tables:
    print("'users' table exists in the database!")
else:
    print("'users' table NOT found!")

# Insert 10 sample records
sample_data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 28},
    {"name": "Emma", "age": 22},
    {"name": "Frank", "age": 40},
    {"name": "Grace", "age": 27},
    {"name": "Henry", "age": 32},
    {"name": "Ivy", "age": 29},
    {"name": "Jack", "age": 26}
]

# Insert data into the database
with engine.connect() as conn:
    conn.execute(users.insert(), sample_data)
    conn.commit()

print("10 records inserted successfully!")

# Check if "users" table exists
if "users" in tables:
    print("'users' table exists in the database!")

    # Read data from the table using Pandas
    query = "SELECT * FROM users"
    df = pd.read_sql(query, engine)

    if df.empty:
        print("'users' table is empty!")
    else:
        print("Table Data:")
        print(df)
else:
    print("'users' table NOT found!")