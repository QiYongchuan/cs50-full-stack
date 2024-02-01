### Testing 测试

assert 断言


### unitest 
python中的单元测试库

```

C:\Users\\Desktop\2024NewStart\cs50fullstack\09-Testing-CI-CD>python tests1.py
...F..      表示第4个测试失败，不符合预期==>返回检查程序
======================================================================
FAIL: test_25 (__main__.Tests)
Check 25 is not prime
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\\Desktop\2024NewStart\cs50fullstack\09-Testing-CI-CD\tests1.py", line 24, in test_25
    self.assertFalse(is_prime(25))
AssertionError: True is not false

----------------------------------------------------------------------
Ran 6 tests in 0.002s

FAILED (failures=1)

```

程序如下：

```
import math
def is_prime(n):
  if n<2:
    return False
  for i in range(2, int(math.sqrt(n))):
    if n % i ==0:
      return False
  return True
```

应该修改成
```
  for i in range(2, int(math.sqrt(n))+1):
```
因为range 的范围不包括后面的值，当25的时候，其实是算的2-4，而不是2-5

修改后再次测试：

```
......
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK

```


在之前的项目flights中测试model

先是在model中写了一条供测试的代码：
-airline
 --flights
  ---models.py
```
  def is_valid_flight(self):
    return self.origin != self.destination or self.duration >= 0
```

```
from django.test import TestCase

from .models import Airport,Flight,Passenger

# Create your tests here.
class FlightTestCase(TestCase):
  def setUp(self):
    #Create airports
    a1 = Airport.objects.create(code="AAA",city="City A")
    a2 = Airport.objects.create(code= "BBB",city="City B")
    
    #Create flights
    Flight.objects.create(origin=a1,destination=a2,duration=100)
    Flight.objects.create(origin=a1,destination=a1,duration=200)
    Flight.objects.create(origin=a1,destination=a2,duration=-100)
    
  def test_departures_count(self):
    a = Airport.objects.get(code="AAA")
    self.assertEqual(a.departures.count(),3)
    
  def test_arrivals_count(self):
    a = Airport.objects.get(code="AAA")
    self.assertEqual(a.arrivals.count(),1)

  def test_valid_flight(self):
    a1 = Airport.objects.get(code="AAA")
    a2 = Airport.objects.get(code = "BBB")
    f = Flight.objects.get(origin=a1,destination=a2,duration=100)
    self.assertTrue(f.is_valid_flight())
    #这里的is_valid_flight()是之前在代码model中写好的函数，来判断航班是否有效的；在这里进行测试， self.assertTrue（），
    # 是假定f = Flight.objects.get(origin=a1,destination=a2,duration=100)  这条数据是有效的航班，看代码是否也运行的结果是True
    
  def test_invalid_flight_destination(self):
    a1 = Airport.objects.get(code="AAA")
    f=Flight.objects.get(origin=a1,destination=a1)
    self.assertFalse(f.is_valid_flight())
    
  def test_invalid_flight_duration(self):
    a1 = Airport.objects.get(code="AAA")
    a2 = Airport.objects.get(code="BBB")
    f = Flight.objects.get(origin=a1,destination=a2,duration=-100)
    self.assertFalse(f.is_valid_flight())
    
  def test_index(self):
    pass
  
  
```

结果：
Found 6 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
...FF.
======================================================================
FAIL: test_invalid_flight_destination (flights.tests.FlightTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\\Desktop\2024NewStart\cs50fullstack\05-SQL-Models-Migrations\airline\flights\tests.py", line 36, in test_invalid_flight_destination
    self.assertFalse(f.is_valid_flight())
AssertionError: True is not false
===>  应该是false，但是程序运行的结果是True
======================================================================
FAIL: test_invalid_flight_duration (flights.tests.FlightTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\亓永传\Desktop\2024NewStart\cs50fullstack\05-SQL-Models-Migrations\airline\flights\tests.py", line 42, in test_invalid_flight_duration    self.assertFalse(f.is_valid_flight())
AssertionError: True is not false
===>  应该是false，但是程序运行的结果是True
----------------------------------------------------------------------
Ran 6 tests in 0.016s

FAILED (failures=2)
Destroying test database for alias 'default'...

```
通过创建和销毁额外的数据库，并没有对原来的数据库进行数据的修改。

