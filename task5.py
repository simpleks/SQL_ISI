from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select
from datetime import date
import pandas as pd
import sqlite3
import sys

db_path = 'C:/Users/zbign/Desktop/ISI__LAB/sql-tutorial/db/penguins.db'
connection = sqlite3.connect(db_path)
cursor = connection.execute("select count(*) from penguins;")
rows = cursor.fetchall()
# print(rows)


db_path = 'C:/Users/zbign/Desktop/ISI__LAB/sql-tutorial/db/penguins.db'
connection = sqlite3.connect(db_path)
cursor = connection.cursor()
cursor = cursor.execute("select species, island from penguins limit 5;")
while row := cursor.fetchone():
    # print(row)

    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    cursor.execute("create table example(num integer);")

    cursor.execute("insert into example values (10), (20);")
    # print("after insertion", cursor.execute("select * from example;").fetchall())

    cursor.execute("delete from example where num < 15;")
    # print("after deletion", cursor.execute("select * from example;").fetchall())

    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    cursor.execute("create table example(num integer);")

    cursor.executemany("insert into example values (?);", [(10,), (20,)])
    # print("after insertion", cursor.execute("select * from example;").fetchall())

    SETUP = """\
    drop table if exists example;
    create table example(num integer);
    insert into example values (10), (20);
    """

    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    cursor.executescript(SETUP)
    print("after insertion", cursor.execute("select * from example;").fetchall())

    SETUP = """\
    create table example(num integer check(num > 0));
    insert into example values (10);
    insert into example values (-1);
    insert into example values (20);
    """

    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    try:
        cursor.executescript(SETUP)
    except sqlite3.Error as exc:
        print(f"SQLite exception: {exc}")
    print("after execution", cursor.execute("select * from example;").fetchall())

    SETUP = """\
    create table example(num integer);
    insert into example values (-10), (10), (20), (30);
    """


    def clip(value):
        if value < 0:
            return 0
        if value > 20:
            return 20
        return value


    connection = sqlite3.connect(":memory:")
    connection.create_function("clip", 1, clip)
    cursor = connection.cursor()
    cursor.executescript(SETUP)
    for row in cursor.execute("select num, clip(num) from example;").fetchall():
        print(row)


    # Convert date to ISO-formatted string when writing to database
    def _adapt_date_iso(val):
        return val.isoformat()


    sqlite3.register_adapter(date, _adapt_date_iso)


    # Convert ISO-formatted string to date when reading from database
    def _convert_date(val):
        return date.fromisoformat(val.decode())


    sqlite3.register_converter("date", _convert_date)

    SETUP = """\
    create table events(
        happened date not null,
        description text not null
    );
    """

    connection = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = connection.cursor()
    cursor.execute(SETUP)

    cursor.executemany(
        "insert into events values (?, ?);",
        [(date(2024, 1, 10), "started tutorial"), (date(2024, 1, 29), "finished tutorial")],
    )

    for row in cursor.execute("select * from events;").fetchall():
        print(row)

        db_path = 'C:/Users/zbign/Desktop/ISI__LAB/sql-tutorial/db/penguins.db'
        connection = sqlite3.connect(db_path)
        query = "select species, count(*) as num from penguins group by species;"
        df = pd.read_sql(query, connection)
        print(df)


# class Department(SQLModel, table=True):
#     ident: str = Field(default=None, primary_key=True)
#     name: str
#     building: str
#
#
# db_uri = "sqlite:///C:/Users/zbign/Desktop/ISI__LAB/sql-tutorial/db/assays.db"
# engine = create_engine(db_uri)
# with Session(engine) as session:
#     statement = select(Department)
#     for result in session.exec(statement).all():
#         print(result)


class Staff(SQLModel, table=True):
    ident: str = Field(default=None, primary_key=True)
    personal: str
    family: str
    dept: Optional[str] = Field(default=None, foreign_key="department.ident")
    age: int


class Department(SQLModel, table=True):
    ident: str = Field(default=None, primary_key=True)
    name: str
    building: str


db_uri = "sqlite:///C:/Users/zbign/Desktop/ISI__LAB/sql-tutorial/db/assays.db"
engine = create_engine(db_uri)
SQLModel.metadata.create_all(engine)
with Session(engine) as session:
    statement = select(Department, Staff).where(Staff.dept == Department.ident)
    for dept, staff in session.exec(statement):
        print(f"{dept.name}: {staff.personal} {staff.family}")
