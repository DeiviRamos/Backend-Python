from database import engine
from app.models import Base

def init_db():
    print("Creating tables")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")
    
if __name__ == "__main__":
    init_db()