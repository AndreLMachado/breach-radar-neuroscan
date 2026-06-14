from app.database import Base, engine

# Importa os models para registrar as tabelas
from app.models import Asset, Vulnerability, SyncAudit

Base.metadata.create_all(bind=engine)

print("Tables created!")
