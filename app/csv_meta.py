from sqlalchemy import Column, String, Integer, DateTime, func

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CSVMeta(Base):
    __tablename__ = 'csv_meta'
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    date = Column(DateTime(timezone=True), server_default=func.now())
