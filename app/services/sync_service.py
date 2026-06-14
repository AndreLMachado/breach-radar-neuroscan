from sqlalchemy.orm import Session

from app.clients.hibp import fetch_breaches
from app.repositories import upsert_breach


def sync_breaches(
    db: Session,
) -> dict:
    created_count = 0
    updated_count = 0

    breaches = fetch_breaches()

    for breach in breaches:
        created = upsert_breach(
            db=db,
            breach_data=breach,
        )

        if created:
            created_count += 1
        else:
            updated_count += 1

    db.commit()

    return {
        "created": created_count,
        "updated": updated_count,
    }
