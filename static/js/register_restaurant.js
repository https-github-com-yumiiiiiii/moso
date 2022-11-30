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

  function setThumbnail(event) {
    var reader = new FileReader();

    reader.onload = function(event) {
      var img = document.createElement("img");
      img.setAttribute("src", event.target.result);
      document.querySelector("div#image_container").appendChild(img);
      
      img.style.width = "360px"; 
      img.style.height = "300px";
    };

    reader.readAsDataURL(event.target.files[0]);
  }

  function add() {
    var date = document.getElementById("monToSun");
    var start = document.getElementById("open");
    var finish = document.getElementById("close");
    if(start.value!=""&&finish.value!=""&&date.value!=""){
      var elementNode = document.getElementById("text");
      var newText = document.createTextNode("요일: "+ date.value+"/  "+ start.value + " 시작 -   " + finish.value+" 종료");
      elementNode.appendChild(newText);
    }
      
  }

  function review() {
    var name = document.getElementById("name");
    var address = document.getElementById("location");
    var tel = document.getElementById("phone");
    var date = document.getElementById("monToSun");
    
    
    if(name.value==""){
      alert("식당 이름을 입력해주세요!")
    }
    else if(address.value==""){
      alert("상세 주소를 입력해주세요!")
    }
    else if(tel.value==""){
      alert("식당 전화번호를 입력해주세요!")
    }
    else if(document.querySelectorAll('input[name="category"]:checked').length == 0) {
      alert('음식 메뉴를 선택해주세요!')
      return false;
    }
    else if(date.value==""){
      alert("영업시간을 입력해주세요!")
    }
    else if(start.value==""){
      alert("시간을 선택해주세요!")
    }
    else{
      location.href='/result';
    }
    
  }

  function NoMultiChk(chk){
    var obj = document.getElementsByName("category");
     for(var i=0; i<obj.length; i++){
       if(obj[i] != chk){
         obj[i].checked = false;
       }
     }
  }