import sqlite3
import random
from datetime import datetime, timedelta

# Connect to the SQLite database
conn = sqlite3.connect("health_data.db")
cursor = conn.cursor()

# Ensure table schema matches database.py
cursor.execute("""
CREATE TABLE IF NOT EXISTS records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT,
    diagnosis TEXT,
    confidence REAL,
    risk_level TEXT,
    latitude REAL,
    longitude REAL,
    timestamp DATETIME
)
""")

DIAGNOSES = [
    ("PNEUMONIA", "High Risk (Outbreak Warning)"),
    ("NORMAL", "Low Risk (Normal)"),
    ("PNEUMONIA", "High Risk (Outbreak Warning)"),
    ("NORMAL", "Low Risk (Normal)"),
    ("NORMAL", "Low Risk (Normal)"),
]

PATIENT_NAMES = [
    "Rajesh Kumar", "Ananya Sharma", "Amit Patel", "Priya Singh", 
    "Suresh Verma", "Neha Gupta", "Vikram Rathore", "Pooja Joshi"
]

BASE_LAT, BASE_LNG = 26.9124, 75.7873
records_to_insert = []
now = datetime.utcnow()

for i in range(25):
    patient = random.choice(PATIENT_NAMES)
    diag, risk = random.choice(DIAGNOSES)
    confidence = round(random.uniform(88.5, 99.2), 2)
    
    lat = round(BASE_LAT + random.uniform(-0.08, 0.08), 4)
    lng = round(BASE_LNG + random.uniform(-0.08, 0.08), 4)
    
    time_offset = timedelta(hours=random.randint(1, 48), minutes=random.randint(0, 59))
    timestamp = (now - time_offset).strftime("%Y-%m-%d %H:%M:%S")

    records_to_insert.append((patient, diag, confidence, risk, lat, lng, timestamp))

cursor.executemany("""
INSERT INTO records (patient_name, diagnosis, confidence, risk_level, latitude, longitude, timestamp)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", records_to_insert)

conn.commit()
conn.close()

print(f"Successfully seeded {len(records_to_insert)} mock patient records into 'health_data.db'!")
