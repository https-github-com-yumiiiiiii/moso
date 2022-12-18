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
let sValue = ['여우카페', '이화키친', 'Je T’aime' ,'코끼리 식당'];
let sPick = Math.floor(Math.random() * sValue.length);
document.getElementById("display").innerHTML = sValue[sPick];
}

  