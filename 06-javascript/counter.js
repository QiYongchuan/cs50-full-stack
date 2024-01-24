let counter = 0;
function count() {
  counter++;
  document.querySelector("h1").innerHTML = counter;

  if (counter % 10 === 0) {
    alert(`count is now ${counter}`)
  }
}
//  DOMContentLoaded  DOM加载完成之后
document.addEventListener('DOMContentLoaded', function () {
  document.querySelector("button").onclick = count;
  // 或者写成
  // document.querySelector("button").addEventListener('click',count)
})
// document.querySelector("button").onclick = count;