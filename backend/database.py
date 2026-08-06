from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# Zero-config SQLite database engine
SQLALCHEMY_DATABASE_URL = "sqlite:///./health_data.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class DiagnosticRecord(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String, default="Patient Anonymous")
    diagnosis = Column(String)
    confidence = Column(Float)
    risk_level = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

Base.metadata.create_all(bind=engine)
