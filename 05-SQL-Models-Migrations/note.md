# SQL -MOdel -Migrations

Datebase Management Systems

* MySql
* PostgreSQL
* SQLite


model 控制sql


SQLite

### 在一张表中：

核心：增删改查

命令行中：创建以及打开文件

```
mkdir flights.sql

sqlite3 flights.sql

一些其他命令行：

.table
/查看文件中创建的表

.mode columns
.headers yes
/增加表头标题

```


CREATE TABLE  创建一个表

```
CREATE TABLE flights(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  origin TEXT NOT NULL,
  destination TEXT NOT NULL,
  duration INTEGER NOT NULL
);

```

INSERT

插入数据--将数据插入到刚刚创建的flights的表中
```
INSERT INTO flights
(origin,destination,duration)
VALUES ("New York","London",415)

```

SELECT  查询

```
SELECT * FROM flights;

SELECT origin,destination from flights;

SELECT * FROM flights where id = 3;

```


UPDATE  
-更新表中数据

```
UPDATE flights
SET duration =430
WHERE origin = "New York"
AND destination = "London";

```

DELETE

```
DELETE FROM flights WHERE destination = 'Tokyo';

```


### foreign keys  多张表相互关联


表间关系：一对一、一对多、多对多

### JOIN  将多个表连接在一起

表passengers

|person_id|flight_id|
|--| --|
|1|1|
|2|1|
|2|4|
|3|2|
|4|4|
|5|6|
|6|6|

表flights

|id | origin   | destination | duration|
|--  |--------|  -----------|  --------|
|1 |  New York |London  |     415|
|2 |  Shanghai  |Tokey  |      120|
|3  | Beijing   |Tokey    |    400|
|4  | JiNan    | Tokey   |     150|
|5  | Lima     | New York |    455|
|6  | Shanghai | Paris    |    760|

连接查询
```
SELECT first,origin,destination
FROM flights JOIN passengers
ON passengers.flights_id = flights.id

从flights 和passengers表中选择first,origin,destination

ON 表示连接的方式：
```

### CREATE INDEX

创建索引，目的是增加查询的效率

```
CREATE INDEX name_index ON passengers(last)

在passengers表中的last项中创建，name_index的索引，方便快速查询
```

### SQL Injection

SQL 注入攻击

```
SELECT * FROM users
WHERE username = "hacker"--" AND password = ""

注：在sql中 -- 代表注释，相当于注释掉了AND password
```

避免sql injection 的方式，一是通过增加转义字符，正确表达--，而不是注释的含义；
另一种方式则是，增加一层model层，在django上控制sql，避免直接编写sql语句了。


### Race Conditions

当多个事件同时发生时，比如查询与删除同时发生时，如何更好处理？

--->  <strong>在数据库上加一个锁</strong>



### models.py  通过model层来控制sql

> 这里涉及到了**外键-多表连接查询**
```

from django.db import models

# Create your models here.

class Airport(models.Model):
  code = models.CharField(max_length =3)
  city = models.CharField(max_length=64)
  
  def __str__(self):
    return f"{self.city} ({self.code})"

class Flight(models.Model):
  origin = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="departures")
  destination = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="arrivals")
  duration = models.IntegerField()
  
  def __str__(self):
    return f"{self.id}: {self.origin} to {self.destination} ,duration:{self.duration}"
  
  
class Passenger(models.Model):
  first = models.CharField(max_length=64)
  last = models.CharField(max_length=64)
  flights = models.ManyToManyField(Flight,blank=True,related_name="passengers")    # 这里是指乘客与航班之间存在多对多的关系
  
  def __str__(self):
    return f"{self.first} {self.last}"

```


### python manage.py shell

```
In [1]: from flights.models import *

In [2]: jfk = Airport(code="JFK",city="New York")

In [3]: jfk.save()

In [4]: lhr = Airport(code="LHR",city="London")

In [5]: lhr.save()

In [6]: cdg = Airport(code = "CDG",city="Paris")

In [7]: cdg.save()

In [8]: nrt = Airport(code="NRT",city="Tokyo")

In [9]: nrt.save()

In [10]: cdg
Out[10]: <Airport: Paris (CDG)>

In [11]: f=Flight(origin=jfk,destination=lhr,duration=415)

In [12]: f.save()

In [13]: f
Out[13]: <Flight: 1: New York (JFK) to London (LHR) ,duration:415>

In [14]: f.origin
Out[14]: <Airport: New York (JFK)>

In [15]: f.origin.city
Out[15]: 'New York'

In [16]: f.origin.code
Out[16]: 'JFK'

In [17]: lhr.arrivals.all()
Out[17]: <QuerySet [<Flight: 1: New York (JFK) to London (LHR) ,duration:415>]>


```


Django 提供的admin 以及一些封装好的工具 ，比如login，logout，authentic等等，方便快捷。


注：

这里的login的前提是，已经有注册过了的账号了，这里是登录。
而注册，则是通过管理员手动注册的，目前没有开发用户自己注册。

