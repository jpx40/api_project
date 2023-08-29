from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref, Mapped, mapped_column
from database import Base

class Parkplatz(Base):
    __tablename__ = "parkplatz"
    parkplatz_id: Mapped[int] = mapped_column(primary_key=True)
    besetzt: Mapped[str] = mapped_column()



class Wechselarbeitzplatz(Base):
    __tablename__ = "arbeitzplatz"
    arbeitzplatz_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

class User(Base):
    __tablename__ = "user"
    user_id: Mapped[int] = mapped_column(primary_key=True)
    user: Mapped[str] = mapped_column()

class game(Base):
    __tablename__ = "game"
    game_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))



