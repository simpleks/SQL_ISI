# Zadanie SQL ISI

Do sprawdzenia zapytań wykorzystywałem probram ``DB Browser for SQLite``

## 2.1 Select

- polecenie ``` sql
select * from little_penguins;```
![img.png](screen/img.png)  

  
  - polecenie ```sql
select
    species,
    island,
    sex
from little_penguins;```

![img_1.png](screen/img_1.png)

- polecenie  ``select
    species,
    sex,
    island
from little_penguins
order by island asc, sex desc;``  

![img_2.png](screen/img_2.png)


- plecenie ``select
    species,
    sex,
    island
from penguins
order by species, sex, island
limit 10;``  

![img_3.png](screen/img_3.png)

- polecenie ``select
    species,
    sex,
    island
from penguins
order by species, sex, island
limit 10 offset 3;``

![img_4.png](screen/img_4.png)


- polecenie ``select distinct
    species,
    sex,
    island
from penguins;``

![img_5.png](screen/img_5.png)

- polecenie ``` sql
select distinct
    species,
    sex,
    island
from penguins
where island = 'Biscoe';```

![img_6.png](screen/img_6.png)


- polecenie ``
select distinct
    species,
    sex,
    island
from penguins
where island = 'Biscoe' and sex != 'MALE';
``


![img_7.png](screen/img_7.png)


- polecenie ``select
    flipper_length_mm / 10.0,
    body_mass_g / 1000.0
from penguins
limit 3;``


![img_8.png](screen/img_8.png)


- polecenie ``select
    flipper_length_mm / 10.0 as flipper_cm,
    body_mass_g / 1000.0 as weight_kg,
    island as where_found
from penguins
limit 3;``

![img_9.png](screen/img_9.png)

- polecenie ``select
    flipper_length_mm / 10.0 as flipper_cm,
    body_mass_g / 1000.0 as weight_kg,
    island as where_found
from penguins
limit 5;``

![img_10.png](screen/img_10.png)

- polecenie ``select distinct
    species,
    sex,
    island
from penguins
where island = 'Biscoe';``

![img_11.png](screen/img_11.png)

- polecenie ``select distinct
    species,
    sex,
    island
from penguins
where island = 'Biscoe' and sex = 'FEMALE';``

![img_12.png](screen/img_12.png)


- polecenie ``select distinct
    species,
    sex,
    island
from penguins
where island = 'Biscoe' and sex = 'FEMALE';``  

![img_13.png](screen/img_13.png)

- polecenie ``select null = null;``

![img_14.png](screen/img_14.png)


- polecenie ``select
    species,
    sex,
    island
from penguins
where sex is null;``  

![img_15.png](screen/img_15.png)

- polecenie ``select sum(body_mass_g) as total_mass
from penguins;``

![img_16.png](screen/img_16.png)


- polecenie ``select
    max(bill_length_mm) as longest_bill,
    min(flipper_length_mm) as shortest_flipper,
    avg(bill_length_mm) / avg(bill_depth_mm) as weird_ratio
from penguins;``

![img_17.png](screen/img_17.png)


- polecenie ``select
    count(*) as count_star,
    count(sex) as count_specific,
    count(distinct sex) as count_distinct
from penguins;``


![img_18.png](screen/img_18.png)

- polecenie ``select avg(body_mass_g) as average_mass_g
from penguins
group by sex;``

![img_19.png](screen/img_19.png)


- polecenie ``select
    sex,
    avg(body_mass_g) as average_mass_g
from penguins
group by sex;``  

![img_20.png](screen/img_20.png)


- polecenie ``select
    sex,
    body_mass_g
from penguins
group by sex;``


![img_21.png](screen/img_21.png)


- polecenie ``select
    sex,
    avg(body_mass_g) as average_mass_g
from penguins
group by sex
having average_mass_g > 4000.0;``


![img_22.png](screen/img_22.png)


- polcenie ``select
    sex,
    round(avg(body_mass_g), 1) as average_mass_g
from penguins
group by sex
having average_mass_g > 4000.0;``

![img_23.png](screen/img_23.png)

- polecenie ``select
    sex,
    round(
        avg(body_mass_g) filter (where body_mass_g < 4000.0),
        1
    ) as average_mass_g
from penguins
group by sex;``

![img_24.png](screen/img_24.png)


- polecenie ``select *
from penguins cross join little_penguins;``


![img_25.png](screen/img_25.png)


- polecenie ``delete from work
where person = 'tae';
select * from work;``

![img_26.png](screen/img_26.png)

- polecenie ``select *
from work cross join job;``

![img_27.png](screen/img_27.png)


- polecenie ``select
    work.person,
    sum(job.billable) as pay
from work inner join job
    on work.job = job.name
group by work.person;``

![img_28.png](screen/img_28.png)

- polecenie ``select *
from work left join job
    on work.job = job.name;``

![img_29.png](screen/img_29.png)


# Tools

- polecenie ``select distinct person
from work
where job != 'calibrate';``

![img_30.png](screen/img_30.png)

- polecenie ``select *
from work
where person not in ('mik', 'tay');``


![img_31.png](screen/img_31.png)


- polecenie ``select distinct person
from work
where person not in (
    select distinct person
    from work
    where job = 'calibrate'
);``

![img_32.png](screen/img_32.png)


- polecenie ``create table lab_equipment (
    size real not null,
    color text not null,
    num integer not null,
    primary key (size, color)
);
insert into lab_equipment values
(1.5, 'blue', 2),
(1.5, 'green', 1),
(2.5, 'blue', 1);
select * from lab_equipment;
insert into lab_equipment values
(1.5, 'green', 2);``


![img_33.png](screen/img_33.png)


- polecenie ``alter table job
add ident integer not null default -1;
update job
set ident = 1
where name = 'calibrate';
update job
set ident = 2
where name = 'clean';
select * from job;``

![img_34.png](screen/img_34.png)

- polecenie ``create table new_work (
    person_id integer not null,
    job_id integer not null,
    foreign key (person_id) references person (ident),
    foreign key (job_id) references job (ident)
);
insert into new_work
select
    person.ident as person_id,
    job.ident as job_id
from
    (person inner join work on person.name = work.person)
    inner join job on job.name = work.job;
select * from new_work;``
- 
![img_35.png](screen/img_35.png)


- polecenie ``select body_mass_g
from penguins
where
    body_mass_g > (
        select avg(body_mass_g)
        from penguins
    )
limit 5;``


![img_36.png](screen/img_36.png)


- polecenie ``select
    penguins.species,
    penguins.body_mass_g,
    round(averaged.avg_mass_g, 1) as avg_mass_g
from penguins inner join (
    select
        species,
        avg(body_mass_g) as avg_mass_g
    from penguins
    group by species
) as averaged
    on penguins.species = averaged.species
where penguins.body_mass_g > averaged.avg_mass_g
limit 5;``

![img_37.png](screen/img_37.png)


- polecenie ``select
    rowid,
    species,
    island
from penguins
limit 5;``

![img_38.png](screen/img_38.png)


- polecenie ``with sized_penguins as (
    select
        species,
        iif(
            body_mass_g < 3500,
            'small',
            'large'
        ) as size
    from penguins
    where body_mass_g is not null
)
select
    species,
    size,
    count(*) as num
from sized_penguins
group by species, size
order by species, num;``

![img_39.png](screen/img_39.png)


- polecenie ``with sized_penguins as (
    select
        species,
        case
            when body_mass_g < 3500 then 'small'
            when body_mass_g < 5000 then 'medium'
            else 'large'
        end as size
    from penguins
    where body_mass_g is not null
)
select
    species,
    size,
    count(*) as num
from sized_penguins
group by species, size
order by species, num;``

![img_40.png](screen/img_40.png)


- polecenie ``with sized_penguins as (
    select
        species,
        case
            when body_mass_g between 3500 and 5000 then 'normal'
            else 'abnormal'
        end as size
    from penguins
    where body_mass_g is not null
)
select
    species,
    size,
    count(*) as num
from sized_penguins
group by species, size
order by species, num;``

![img_41.png](screen/img_41.png)



- polecenie ``select * from staff;``

![img_42.png](screen/img_42.png)


- polecenie ``select
    personal,
    family
from staff
where personal like '%ya%';``

![img_43.png](screen/img_43.png)


- polecenie ``select * from (
    select * from (select * from experiment order by started asc limit 5)
    union all
    select * from (select * from experiment order by started desc limit 5)
)
order by started asc;``

![img_44.png](screen/img_44.png)

- polecenie ``select
    personal,
    family,
    dept,
    age
from staff
where dept = 'mb'
intersect
select
    personal,
    family,
    dept,
    age from staff
where age < 50;``

![img_45.png](screen/img_45.png)

- polecenie ``select
    personal,
    family,
    dept,
    age
from staff
where dept = 'mb'
except
    select
        personal,
        family,
        dept,
        age from staff
    where age < 50;``


![img_46.png](screen/img_46.png)


- polecenie ``with decorated as (
    select random() as rand,
    personal || ' ' || family as name
    from staff
)

select
    rand,
    abs(rand) % 10 as selector,
    name
from decorated
where selector < 5;``

![img_47.png](screen/img_47.png)


- polecenie ``explain query plan
select filename
from plate
where filename like '%07%';
create index plate_file on plate(filename);
explain query plan
select filename
from plate
where filename like '%07%';``

![img_48.png](screen/img_48.png)

- polecenie ``with person as (
    select
        ident,
        personal || ' ' || family as name
    from staff
)
select
    left_person.name,
    right_person.name
from person as left_person inner join person as right_person
on left_person.ident < right_person.ident
where left_person.ident <= 4 and right_person.ident <= 4;``


![img_49.png](screen/img_49.png)


- polecenie ``with
person as (
    select
        ident,
        personal || ' ' || family as name
    from staff
),
together as (
    select
        left_perf.staff as left_staff,
        right_perf.staff as right_staff
    from performed as left_perf inner join performed as right_perf
        on left_perf.experiment = right_perf.experiment
    where left_staff < right_staff
)
select
    left_person.name as person_1,
    right_person.name as person_2
from person as left_person inner join person as right_person join together
    on left_person.ident = left_staff and right_person.ident = right_staff;``

![img_50.png](screen/img_50.png)

- polecenie ``select
    name,
    building
from department
where
    exists (
        select 1
        from staff
        where dept = department.ident
    )
order by name;``

![img_51.png](screen/img_51.png)

- polecenie ``select
    name,
    building
from department
where
    not exists (
        select 1
        from staff
        where dept = department.ident
    )
order by name;``

![img_52.png](screen/img_52.png)


- polecenie ``select distinct
    department.name as name,
    department.building as building
from department inner join staff
    on department.ident = staff.dept
order by name;``

![img_53.png](screen/img_53.png)


- polecenie ``with ym_num as (
    select
        strftime('%Y-%m', started) as ym,
        count(*) as num
    from experiment
    group by ym
)
select
    ym,
    lag(num) over (order by ym) as prev_num,
    num,
    lead(num) over (order by ym) as next_num
from ym_num
order by ym;``

![img_54.png](screen/img_54.png)


- polecenie ``with ym_num as (
    select
        strftime('%Y-%m', started) as ym,
        count(*) as num
    from experiment
    group by ym
)
select
    ym,
    num,
    sum(num) over (order by ym) as num_done,
    (sum(num) over (order by ym) * 1.00) / (select sum(num) from ym_num) as completed_progress,
    cume_dist() over (order by ym) as linear_progress
from ym_num
order by ym;``


![img_55.png](screen/img_55.png)


- polecenie ``explain query plan
with ym_num as (
    select
        strftime('%Y-%m', started) as ym,
        count(*) as num
    from experiment
    group by ym
)
select
    ym,
    num,
    sum(num) over (order by ym) as num_done,
    cume_dist() over (order by ym) as progress
from ym_num
order by ym;``


![img_56.png](screen/img_56.png)


- polecenie ``with y_m_num as (
    select
        strftime('%Y', started) as year,
        strftime('%m', started) as month,
        count(*) as num
    from experiment
    group by year, month
)
select
    year,
    month,
    num,
    sum(num) over (partition by year order by month) as num_done
from y_m_num
order by year, month;``

![img_57.png](screen/img_57.png)

- polecenie ``select * from machine;``

![img_58.png](screen/img_58.png)


- polecenie ``select
    ident,
    json_each.key as key,
    json_each.value as value
from usage, json_each(usage.log)
limit 10;``

![img_59.png](screen/img_59.png)

- polecenie ``select
    ident,
    name,
    json_set(details, '$.sold', json_quote('2024-01-25')) as updated
from machine;``

![img_60.png](screen/img_60.png)

- polecenie ``select
    species,
    count(*) as num
from penguins
group by species;``

![img_62.png](screen/img_62.png)

- polecenie ``alter table penguins
add active integer not null default 1;
update penguins
set active = iif(species = 'Adelie', 0, 1);
select
    species,
    count(*) as num
from penguins
where active
group by species;``

![img_63.png](screen/img_63.png)


- polecenie ``create table lineage (
    parent text not null,
    child text not null
);
insert into lineage values
('Arturo', 'Clemente'),
('Darío', 'Clemente'),
('Clemente', 'Homero'),
('Clemente', 'Ivonne'),
('Ivonne', 'Lourdes'),
('Soledad', 'Lourdes'),
('Lourdes', 'Santiago');
select * from lineage;``

![img_64.png](screen/img_64.png)

- polecenie ``with recursive descendent as (
    select
        'Clemente' as person,
        0 as generations
    union all
    select
        lineage.child as person,
        descendent.generations + 1 as generations
    from descendent inner join lineage
        on descendent.person = lineage.parent
)
select
    person,
    generations
from descendent;``
![img_65.png](screen/img_65.png)





# Skrypt

```python

import sqlite3

db_path = '/db/penguins.db'
connection = sqlite3.connect(db_path)
cursor = connection.execute("select count(*) from penguins;")
rows = cursor.fetchall()
print(rows)
```

wynik:
![img_66.png](img_66.png)


```python
import sqlite3

db_path = 'C:/Users/zbign/Desktop/ISI__LAB/sql-tutorial/db/penguins.db'
connection = sqlite3.connect(db_path)
cursor = connection.cursor()
cursor = cursor.execute("select species, island from penguins limit 5;")
while row := cursor.fetchone():
    print(row)
```

![img_67.png](img_67.png)

```python
 connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    cursor.execute("create table example(num integer);")

    cursor.execute("insert into example values (10), (20);")
    print("after insertion", cursor.execute("select * from example;").fetchall())

    cursor.execute("delete from example where num < 15;")
    print("after deletion", cursor.execute("select * from example;").fetchall())

```

![img_68.png](img_68.png)

```python
connection = sqlite3.connect(":memory:")
cursor = connection.cursor()
cursor.execute("create table example(num integer);")

cursor.executemany("insert into example values (?);", [(10,), (20,)])
print("after insertion", cursor.execute("select * from example;").fetchall())
```

![img_69.png](img_69.png)


```python
SETUP = """\
drop table if exists example;
create table example(num integer);
insert into example values (10), (20);
"""

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()
cursor.executescript(SETUP)
print("after insertion", cursor.execute("select * from example;").fetchall())
```

![img_70.png](img_70.png)


```python
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
```

![img_71.png](img_71.png)


```python
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
```

![img_72.png](img_72.png)

```python
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
```
![img_73.png](img_73.png)


```python
db_path = 'C:/Users/zbign/Desktop/ISI__LAB/sql-tutorial/db/penguins.db'
        connection = sqlite3.connect(db_path)
        query = "select species, count(*) as num from penguins group by species;"
        df = pd.read_sql(query, connection)
        print(df)
```

![img_74.png](img_74.png)


```python

class Department(SQLModel, table=True):
    ident: str = Field(default=None, primary_key=True)
    name: str
    building: str


db_uri = "sqlite:///C:/Users/zbign/Desktop/ISI__LAB/sql-tutorial/db/assays.db"
engine = create_engine(db_uri)
with Session(engine) as session:
    statement = select(Department)
    for result in session.exec(statement).all():
        print(result)
```

![img_75.png](img_75.png)


```python
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
```

![img_76.png](img_76.png)




