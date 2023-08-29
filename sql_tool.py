from sqlalchemy import MetaData

metadata_obj = MetaData()

from sqlalchemy import ForeignKey

from sqlalchemy import Table, Column, Integer, String

user_table = Table(
    "user",
    metadata_obj,
    Column("user_id", Integer, primary_key=True, nullable=False),
    Column("name", String(30), nullable=False),
    Column("fullname", String),
)

address_table = Table(
    "address",
    metadata_obj,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("user_id", ForeignKey("user.id"), nullable=False),
    Column("email_address", String, nullable=False),
)

parkplatz_table = Table(
    "parkplatz",
    metadata_obj,
    Column("parkplatz_id", Integer, primary_key=True, nullable=False),
    Column("besetzt", String(30), nullable=False),
)

arbeitzplatz_table = Table(
    "arbeitzplatz",
    metadata_obj,
    Column("arbeitzplatz_id", Integer, primary_key=True),
    Column("besetzt", String(30), nullable=False),
    Column("user_id", ForeignKey("user_.id"), nullable=False),
)

arbeitzplatz_table = Table(
    "arbeitzplatz",
    metadata_obj,
    Column("game_id", Integer, primary_key=True),
    Column("score", Integer),
    Column("user_id", ForeignKey("user_.id"), nullable=False),
)
