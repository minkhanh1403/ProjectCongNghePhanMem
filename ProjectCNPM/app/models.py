from sqlalchemy import Column, Integer, String
# from app import db

class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)

if __name__ == '__main__':
    from app import app
    with app.app_context():
        db.create_all()