// let counter = 0;

if (!localStorage.getItem('counter')) {
  localStorage.setItem('counter',0);
}

function count() {
  let counter = localStorage.getItem('counter');
  counter++;
  document.querySelector("h1").innerHTML = counter;
  localStorage.setItem('counter',counter);

  // if (counter % 10 === 0) {
  //   alert(`count is now ${counter}`)
  // }
}
//  DOMContentLoaded  DOM加载完成之后
document.addEventListener('DOMContentLoaded', function () {
  document.querySelector('h1').innerHTML = localStorage.getItem('counter');
  document.querySelector("button").onclick = count;
  // 或者写成
  // document.querySelector("button").addEventListener('click',count)

  setInterval(count,1000);  //间隔函数
})
// document.querySelector("button").onclick = count;