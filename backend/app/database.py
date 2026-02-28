from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ===== LOCAL PC =====
#DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/finlab_db"

# ===== CODESPACE =====
#DATABASE_URL=mysql+pymysql://root:root@db:3306/finsys

# ===== DESENVOLVIMENTO (SQLite) =====
DATABASE_URL = "sqlite:///./finsys.db"

#Engine mysql
engine = create_engine(DATABASE_URL)

#Engine SQLite
engine = create_engine(DATABASE_URL,connect_args={"check_same_thread":False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()