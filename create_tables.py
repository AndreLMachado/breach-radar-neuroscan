from app.database import Base
from app.database import engine
from app import models  # noqa: F401


Base.metadata.create_all(bind=engine)

print("Tables created!")
