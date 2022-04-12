from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.session import Base


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)

    users = relationship('User', back_populates="user_role")
    # users = relationship(
    #     "User",
    #     cascade="all,delete-orphan",
    #     back_populates="user_role",
    #     uselist=True,
    # )
