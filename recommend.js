/* Set the width of the side navigation to 250px and the left margin of the page content to 250px and add a black background color to body */
function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
  document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
}

/* Set the width of the side navigation to 0 and the left margin of the page content to 0, and the background color of body to white */
function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("main").style.marginLeft = "0";
  document.body.style.backgroundColor = "white";
}

/*function randomNumsShow(min, max) {
  const random = Math.floor(Math.random() * (max - min)) + min;
   showReason(random);
}

function showReason(num) {
  let result = reasons[num].content;
  document.getElementById("display").innerHTML = result;
};*/

function randomString(){
let sValue = ['Lorem', 'Ipsum', 'Dolor' ,'코끼리 식당', '기린 식당','빼빼로식당'
,'ㅇㅇ','ㅇㄹㄴ','ㄹㅇㅇㄴ'];
let sPick = Math.floor(Math.random() * sValue.length);
document.getElementById("display").innerHTML = sValue[sPick];
}

  