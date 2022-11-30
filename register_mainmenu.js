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

function go(){
    var menu = document.getElementById("menu_name");
    var price = document.getElementById("price");
    var image = document.getElementById("file");

    if(menu.value==""){
      alert("메뉴명을 입력해주세요!")
    }
    else if(price.value==""){
      alert("가격을 입력해주세요!")
    }
    else if(image.value==""){
      alert("음식 사진을 등록해주세요!");
    }
    else{
      location.href="view_mainmenu.html"
    }

  }