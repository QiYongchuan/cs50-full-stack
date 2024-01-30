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


### Local Storage

* localStorage.getItem(key)
* localStorage.setItem(key,value)



### objects


###  API
application programming interfaces


JSON  javascript object notation,以js对象的形式传输数据



Ajax  是关于同步JavaScript的，即使在页面加载之后，使用JavaScript我们可以提出额外的网络请求去访问更多的信息，来自我们自己的网络服务器或者一些第三方的网络服务器，如果我们想在我们的页面上获取更多的信息，在这种情况下我们想要的是我们的页面做一个请求额外数据的同步请求

** 也就是只加载页面的一部分 **



### Window 

![Alt text](%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20240129132318.png)

* window 是目前窗口
* document是整个文档
* window.scrollY 窗口向下滑动的的距离，如果没有滑动就是0
* document.body.offsetHeight是整个文档的高度
* window.innerHeight与windo.innerWidth是当前窗口的高的宽

利用上述的属性,可以:
1.检测用户是否滑动到了底部？

window.scrollY+window.innerHeight = document.body.offsetHeight


2.结合ajax，实现无限滚动
  1.检测是否到浏览器的底部
  2.结合ajax使用JavaScript的异步操作，异步加载