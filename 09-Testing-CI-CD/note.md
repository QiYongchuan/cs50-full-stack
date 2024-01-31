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