# import psycopg2
# import pandas as pd
# from django.conf import settings

# # Function to connect to the PostgreSQL database using Django settings
# def connect_to_db():
#     try:
#         conn = psycopg2.connect(
#             dbname=settings.DATABASES['default']['NAME'],
#             user=settings.DATABASES['default']['USER'],
#             password=settings.DATABASES['default']['PASSWORD'],
#             host=settings.DATABASES['default']['HOST'],
#             port=settings.DATABASES['default']['PORT']
#         )
#         return conn
#     except psycopg2.Error as e:
#         print(f"Error connecting to the database: {e}")
#         return None

# # Function to execute a query and return results as a DataFrame
# def query_to_dataframe(query, params=None):
#     conn = connect_to_db()
#     if conn is None:
#         return None
    
#     try:
#         cursor = conn.cursor()
#         cursor.execute(query, params)
#         results = cursor.fetchall()
#         columns = [desc[0] for desc in cursor.description]  # Get column names
#         cursor.close()
        
#         # Convert results to DataFrame
#         df = pd.DataFrame(results, columns=columns)
#         return df
#     except psycopg2.Error as e:
#         print(f"Error executing query: {e}")
#         return None
#     finally:
#         conn.close()

# # Example usage: Function to fetch all rows from the 'opusnet_table' as a DataFrame
# def fetch_all_opusnet_data():
#     query = "SELECT * FROM public.opusnet_table"
#     return query_to_dataframe(query)

# import pandas as pd
# from sqlalchemy import create_engine
# from django.conf import settings

# # Database connection string (you can store this in Django settings if you prefer)
# db_url = "postgresql://default:w2KGfbOSHy6R@ep-twilight-sunset-a45mqvb6.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require"

# # Create a SQLAlchemy engine
# engine = create_engine(db_url)

# # Function to execute a query and return results as a DataFrame
# def query_to_dataframe(query, params=None):
#     try:
#         # Execute query and fetch data into a DataFrame
#         with engine.connect() as connection:
#             df = pd.read_sql(query, connection, params=params)
#         return df
#     except Exception as e:
#         print(f"Error executing query: {e}")
#         return None

# # Example usage: Function to fetch all rows from the 'opusnet_table' as a DataFrame
# def fetch_all_opusnet_data():
#     query = "SELECT * FROM opusnet_table"
#     return query_to_dataframe(query)


import pandas as pd
from sqlalchemy import create_engine
from django.conf import settings

# Create a database connection URL from Django settings
db_url = f"postgresql://{settings.DATABASES['default']['USER']}:{settings.DATABASES['default']['PASSWORD']}@" \
         f"{settings.DATABASES['default']['HOST']}:{settings.DATABASES['default']['PORT']}/{settings.DATABASES['default']['NAME']}?sslmode=require"

# Create a SQLAlchemy engine
engine = create_engine(db_url)

# Function to execute a query and return results as a DataFrame
def query_to_dataframe(query, params=None):
    try:
        # Execute query and fetch data into a DataFrame
        with engine.connect() as connection:
            df = pd.read_sql(query, connection, params=params)
        return df
    except Exception as e:
        print(f"Error executing query: {e}")
        return None

# Example usage: Function to fetch all rows from the 'opusnet_converted_corrected_1' as a DataFrame
def fetch_all_opusnet_data():
    query = "SELECT * FROM opusnet_converted_corrected_1"
    return query_to_dataframe(query)