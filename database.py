import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

DB_URL = os.getenv("DATABASE_URL")

# Подключаемся к базе
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)

# Определяем базовый класс
Base = declarative_base()

# Создаём таблицу статей
class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)

# Создаём таблицы
Base.metadata.create_all(engine)
