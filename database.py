from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import text

DATABASE_URL = "postgresql+psycopg2://postgres:XkCMKctKfIEMgqfgofbl@database-2.cqh4uwqw89ad.us-east-1.rds.amazonaws.com:5432/postgres"
print('DB',DATABASE_URL)
engine = create_engine(DATABASE_URL, echo=True)
print('engine',engine)
SessionLocal = sessionmaker(bind=engine)
print('SessionLocal',SessionLocal)
Base = declarative_base()
print('Base',Base)
session = SessionLocal()

try:
    # Test a simple query to check the connection
    result = session.execute(text("SELECT 1"))
    print("Connection successful:", result.scalar())
except Exception as e:
    print("Error during DB connection:", str(e))
finally:
    session.close()