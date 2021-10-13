from sqlalchemy import Table, Column
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import Integer, TIMESTAMP, VARCHAR, NUMERIC

alpha = Table("alpha", meta, Column(
    "app_id", Integer, primary_key=True), Column("fecha", TIMESTAMP), Column("user_id", VARCHAR(300)),
              Column("order_id", VARCHAR(300)), Column("value_total", NUMERIC), Column("order_number", Integer),
              Column("currency", VARCHAR(300)))
meta.create_all(engine)
