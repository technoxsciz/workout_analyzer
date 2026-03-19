import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
password = os.getenv("DB_PASSWORD")

# Connect to Postgres
engine = create_engine(f"postgresql://postgres:{password}@localhost:5432/workout_analyzer")

# Load CSV — update the path to where your file is
df = pd.read_csv("gym_exercise_dataset.csv")

# Clean column names
df.columns = (df.columns
              .str.strip()
              .str.lower()
              .str.replace(" ", "_")
              .str.replace("(", "")
              .str.replace(")", ""))

# Load into Postgres
df.to_sql("exercises", engine, if_exists="replace", index=False)

print(f"✅ Done! {len(df)} rows loaded into 'exercises' table")