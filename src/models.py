from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    user_name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    firts_ame: Mapped[str] = mapped_column(String(120), nullable=False)
    last_name: Mapped[str] = mapped_column(String(120), nullable=False)
    subscription_date: Mapped[int] = mapped_column(nullable=False)
    save_data: Mapped[str]= mapped_column(String(5000))

    #favorite relationship
    favorites: Mapped[List["Favorite"]] = relationship(back_populates="user")
    

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    #favorite relationship
    favorite_id: Mapped[int] = mapped_column(ForeignKey("favorite.id"))
    favorite: Mapped["Favorite"] = relationship(back_populates="planets")
 
class People(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    #favorite relationship
    favorite_id: Mapped[int] = mapped_column(ForeignKey("favorite.id"))
    favorite: Mapped["Favorite"] = relationship(back_populates="people")

class Favorite(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    #User relationship
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="favorites")

    #Planets relationship
    planets: Mapped[List["Planets"]] = relationship(back_populates="favorite")

    #People relationship
    people: Mapped[List["People"]] = relationship(back_populates="favorite")