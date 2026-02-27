from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ===== LOCAL PC =====
#DATABASE_URL = "mysql+pymysql://root:igor100@localhost:3306/finlab_db"

# ===== CODESPACE =====
DATABASE_URL=mysql+pymysql://root:root@db:3306/finsys


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()