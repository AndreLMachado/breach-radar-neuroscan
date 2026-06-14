from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from app.database import Base


class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)

    vendor = Column(String, nullable=False)
    product = Column(String, nullable=False)


class Vulnerability(Base):
    __tablename__ = "vulnerabilities"

    cve_id = Column(String, primary_key=True)

    vendor_project = Column(String, nullable=False)
    product = Column(String, nullable=False)

    vulnerability_name = Column(String, nullable=False)

    date_added = Column(DateTime, nullable=False)
    due_date = Column(DateTime, nullable=False)

    notes = Column(Text, nullable=True)


class SyncAudit(Base):
    __tablename__ = "sync_audit"

    id = Column(Integer, primary_key=True, index=True)

    started_at = Column(DateTime, default=datetime.utcnow)

    finished_at = Column(DateTime)

    status = Column(String)

    created_count = Column(Integer, default=0)
    updated_count = Column(Integer, default=0)
