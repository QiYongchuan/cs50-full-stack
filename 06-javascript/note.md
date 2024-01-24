# Javascropt  在客户端运行的代码

> 区别于之前的Django，是运行的服务器端的代码。js则是运行在客户端的代码，使网页更具交互性，直接操控页面中的Dom元素。



一些需要注意的点：

1.函数的立即调用和函数的引用



2.注意自上而下的加载DOM

```
     
    document.querySelector("button").onclick = count;
  </script>
</head>

<body>
  <h1>0</h1>
  <button>count</button>
</body>

</html>

在上面的代码中，因为自上而下的运行代码，会导致获取不到button的值，null


   document.addEventListener('DOMContentLoaded',function(){
    document.querySelector("button").onclick = count;
    // 或者写成
    // document.querySelector("button").addEventListener('click',count)
   })
    // document.querySelector("button").onclick = count;


```


### querySelector
* document.querySelector('tag')
* document.querySelector('#id')
* document.querySelector(".class")

### querySelectorAll

返回相同类的数组，可以进行遍历获取每一个元素

* 注：这里的data-color是存储，然后通过button.dataset.color读取
* forEach(function (button){})  这里forEach传入参数button
```


<script>

    document.addEventListener('DOMContentLoaded', function () {
      document.querySelectorAll('button').forEach(function (button) {
        button.onclick = function () {
          document.querySelector('#hello').style.color = button.dataset.color;
        }
      })
    })

  </script>
</head>

<body>
  <h1 id="hello"> hello!</h1>
  <button data-color="red">Red</button>
  <button data-color="Blue">Blue</button>
  <button data-color="Green">Green</button>
</body>

```

