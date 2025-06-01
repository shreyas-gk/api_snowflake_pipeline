import os
import csv
from dotenv import load_dotenv
import snowflake.connector

# Load environment variables from .env file
load_dotenv()

SNOWFLAKE_USER = os.getenv("SNOWFLAKE_USER")
SNOWFLAKE_PASSWORD = os.getenv("SNOWFLAKE_PASSWORD")
SNOWFLAKE_ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT")
SNOWFLAKE_WAREHOUSE = os.getenv("SNOWFLAKE_WAREHOUSE")
SNOWFLAKE_DATABASE = os.getenv("SNOWFLAKE_DATABASE")
SNOWFLAKE_SCHEMA = os.getenv("SNOWFLAKE_SCHEMA")

def get_latest_csv_file(folder_path, prefix):
    """
    Find the latest CSV file in folder_path starting with prefix
    """
    csv_files = [f for f in os.listdir(folder_path) if f.startswith(prefix) and f.endswith(".csv")]
    if not csv_files:
        return None
    csv_files.sort(reverse=True)
    return os.path.join(folder_path, csv_files[0])

def load_csv_to_snowflake(table_name, csv_file, create_table_sql, insert_sql, csv_columns):
    print(f"\nLoading data for table '{table_name}' from file: {csv_file}")

    conn = None
    cursor = None
    try:
        # Check env variables
        if not all([SNOWFLAKE_USER, SNOWFLAKE_PASSWORD, SNOWFLAKE_ACCOUNT, SNOWFLAKE_WAREHOUSE, SNOWFLAKE_DATABASE, SNOWFLAKE_SCHEMA]):
            raise Exception("One or more Snowflake connection environment variables are missing. Please check your .env file.")

        print(f"Connecting to Snowflake account: {SNOWFLAKE_ACCOUNT}, database: {SNOWFLAKE_DATABASE}, schema: {SNOWFLAKE_SCHEMA}")
        conn = snowflake.connector.connect(
            user=SNOWFLAKE_USER,
            password=SNOWFLAKE_PASSWORD,
            account=SNOWFLAKE_ACCOUNT,
            warehouse=SNOWFLAKE_WAREHOUSE,
            database=SNOWFLAKE_DATABASE,
            schema=SNOWFLAKE_SCHEMA
        )
        cursor = conn.cursor()

        print(f"Creating table '{table_name}' if not exists...")
        cursor.execute(create_table_sql)
        print(f"Table '{table_name}' ready.")

        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data = []
            for row in reader:
                record = tuple(row[col] for col in csv_columns)
                data.append(record)

        print(f"Inserting {len(data)} records into '{table_name}'...")
        cursor.executemany(insert_sql, data)
        conn.commit()
        print(f"Inserted {len(data)} records into '{table_name}' successfully.")

    except Exception as e:
        print(f"Error loading data into '{table_name}': {e}")
    finally:
        if cursor:
            try:
                cursor.close()
            except Exception as ce:
                print(f"Error closing cursor: {ce}")
        if conn:
            try:
                conn.close()
            except Exception as ce:
                print(f"Error closing connection: {ce}")

def main():
    print("Starting Snowflake data load process...")

    # Define table schemas, insert SQL, and CSV column order - column names uppercased in SQL statements
    tables = {
        "patients": {
            "folder": "data/patients",
            "prefix": "patients_",
            "create_sql": """
                CREATE TABLE IF NOT EXISTS patients (
                    PATIENT_ID STRING,
                    FIRST_NAME STRING,
                    LAST_NAME STRING,
                    BIRTHDATE DATE,
                    EMAIL STRING,
                    PHONE STRING,
                    ADDRESS STRING,
                    GENDER STRING
                )
            """,
            "insert_sql": """
                INSERT INTO patients
                (PATIENT_ID, FIRST_NAME, LAST_NAME, BIRTHDATE, EMAIL, PHONE, ADDRESS, GENDER)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            "csv_columns": ['patient_id', 'first_name', 'last_name', 'birthdate', 'email', 'phone', 'address', 'gender'],
        },
        "appointments": {
            "folder": "data/appointments",
            "prefix": "appointments_",
            "create_sql": """
                CREATE TABLE IF NOT EXISTS appointments (
                    APPOINTMENT_ID STRING,
                    PATIENT_ID STRING,
                    DOCTOR_NAME STRING,
                    APPOINTMENT_DATE TIMESTAMP,
                    DEPARTMENT STRING
                )
            """,
            "insert_sql": """
                INSERT INTO appointments
                (APPOINTMENT_ID, PATIENT_ID, DOCTOR_NAME, APPOINTMENT_DATE, DEPARTMENT)
                VALUES (%s, %s, %s, %s, %s)
            """,
            "csv_columns": ['appointment_id', 'patient_id', 'doctor_name', 'appointment_date', 'department'],
        },
        "prescriptions": {
            "folder": "data/prescriptions",
            "prefix": "prescriptions_",
            "create_sql": """
                CREATE TABLE IF NOT EXISTS prescriptions (
                    PRESCRIPTION_ID STRING,
                    PATIENT_ID STRING,
                    MEDICATION_NAME STRING,
                    DOSAGE STRING,
                    START_DATE DATE,
                    END_DATE DATE
                )
            """,
            "insert_sql": """
                INSERT INTO prescriptions
                (PRESCRIPTION_ID, PATIENT_ID, MEDICATION_NAME, DOSAGE, START_DATE, END_DATE)
                VALUES (%s, %s, %s, %s, %s, %s)
            """,
            "csv_columns": ['prescription_id', 'patient_id', 'medication_name', 'dosage', 'start_date', 'end_date'],
        }
    }

    for table_name, config in tables.items():
        latest_csv = get_latest_csv_file(config["folder"], config["prefix"])
        if latest_csv:
            load_csv_to_snowflake(
                table_name=table_name,
                csv_file=latest_csv,
                create_table_sql=config["create_sql"],
                insert_sql=config["insert_sql"],
                csv_columns=config["csv_columns"]
            )
        else:
            print(f"No CSV files found for table '{table_name}' in folder '{config['folder']}'.")

if __name__ == "__main__":
    main()
