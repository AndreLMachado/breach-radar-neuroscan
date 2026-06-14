from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String

from app.database import Base


class SyncAudit(Base):
    __tablename__ = "sync_audit"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    started_at = Column(
        DateTime,
        default=datetime.utcnow,
    )

    finished_at = Column(
        DateTime,
    )

    status = Column(
        String,
    )

    created_count = Column(
        Integer,
        default=0,
    )

    updated_count = Column(
        Integer,
        default=0,
    )
