import json
import psycopg2
from datetime import datetime

conn = psycopg2.connect(
    dbname="schemeassist",
    user="username",
    password="password",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

with open("backend/data/schemes.json") as f:
    schemes = json.load(f)["schemes"]

for s in schemes:
    cur.execute(
        """
        INSERT INTO schemes (
            scheme_id, name, level, state,
            min_age, max_age,
            min_income, max_income,
            target_groups, benefits,
            documents_required, deadline
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT (scheme_id) DO NOTHING;
        """,
        (
            s["scheme_id"],
            s["name"],
            s["level"],
            s["state"],
            s["min_age"],
            s["max_age"],
            s["min_income"],
            s["max_income"],
            s["target_groups"],
            s["benefits"],
            s["documents_required"],
            datetime.strptime(s["deadline"], "%Y-%m-%d").date()
        )
    )

conn.commit()
cur.close()
conn.close()

print("Seeded!")
