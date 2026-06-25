import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

# -----------------------------
# Gold Metrics Data
# -----------------------------
data = {
    "event_type": [
        "purchase",
        "add_to_cart",
        "checkout",
        "view_item"
    ],
    "total_events": [
        250413,
        250621,
        249425,
        249541
    ],
    "total_revenue": [
        126782881.70,
        126444062.58,
        126006735.29,
        126130303.07
    ]
}

df = pd.DataFrame(data)

# -----------------------------
# PostgreSQL Connection
# -----------------------------
DATABASE_URL = "postgresql+psycopg2://admin:admin123@127.0.0.1:5433/warehouse"
try:
    engine = create_engine(DATABASE_URL)

    # Test Connection
    with engine.connect() as conn:
        print(" Connected to PostgreSQL")

    # Load Data
    df.to_sql(
        "gold_metrics",
        engine,
        if_exists="replace",
        index=False
    )

    print(" Gold metrics loaded successfully!")

except SQLAlchemyError as e:
    print("\n❌ Database Error:")
    print(e)

except Exception as e:
    print("\n❌ Error:")
    print(e)