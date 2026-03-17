from __future__ import annotations

from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class User(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    telegram_id: Mapped[int] = mapped_column(Integer, unique=True, index=True)
    username: Mapped[str | None] = mapped_column(String(64), nullable=True)
    full_name: Mapped[str] = mapped_column(String(128))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    orders: Mapped[list[Order]] = relationship(back_populates="user")


class Venue(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(128))
    address: Mapped[str] = mapped_column(String(255))
    capacity: Mapped[int] = mapped_column(Integer)

    events: Mapped[list[Event]] = relationship(back_populates="venue")


class Event(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    venue_id: Mapped[int] = mapped_column(ForeignKey("venue.id"))
    title: Mapped[str] = mapped_column(String(160))
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    start_at: Mapped[datetime] = mapped_column(DateTime)
    end_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    venue: Mapped[Venue] = relationship(back_populates="events")
    seats: Mapped[list[Seat]] = relationship(back_populates="event")


class Seat(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    event_id: Mapped[int] = mapped_column(ForeignKey("event.id"))
    section: Mapped[str] = mapped_column(String(64))
    row: Mapped[str] = mapped_column(String(16))
    number: Mapped[str] = mapped_column(String(16))
    price: Mapped[float] = mapped_column(Numeric(10, 2))
    is_available: Mapped[bool] = mapped_column(Boolean, default=True)

    event: Mapped[Event] = relationship(back_populates="seats")
    tickets: Mapped[list[Ticket]] = relationship(back_populates="seat")


class Order(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    status: Mapped[str] = mapped_column(String(32), default="pending")
    total_amount: Mapped[float] = mapped_column(Numeric(10, 2), default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    user: Mapped[User] = relationship(back_populates="orders")
    tickets: Mapped[list[Ticket]] = relationship(back_populates="order")


class Ticket(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("order.id"))
    seat_id: Mapped[int] = mapped_column(ForeignKey("seat.id"))
    qr_code: Mapped[str | None] = mapped_column(String(255), nullable=True)
    issued_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    order: Mapped[Order] = relationship(back_populates="tickets")
    seat: Mapped[Seat] = relationship(back_populates="tickets")
