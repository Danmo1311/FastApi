from sqlalchemy import create_engine, MetaData

engine = create_engine("postgresql://postgres:user@localhost:5432/Linnda-test")
meta=MetaData()
conn =engine.connect()

#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base = declarative_base()