var b1 = document.getElementsByClassName("b1");

      function handleClick(event) {
        console.log(event.target);
        // console.log(this);
        // 콘솔창을 보면 둘다 동일한 값이 나온다

        console.log(event.target.classList);

        if (event.target.classList[1] === "clicked") {
          event.target.classList.remove("clicked");
        } else {
          for (var i = 0; i < b1.length; i++) {
            b1[i].classList.remove("clicked");
          }

          event.target.classList.add("clicked");
        }
      }

      function init() {
        for (var i = 0; i < b1.length; i++) {
          b1[i].addEventListener("click", handleClick);
        }
      }

      init();



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
        var review = document.getElementById("review");
        var year = document.getElementById("year");
        var month = document.getElementById("month");
        var date = document.getElementById("date");
        var name = document.getElementById("restaurant_name");
        if(name.value==""){
          alert("식당 이름을 입력해주세요!")
        }
        else if(year.value==""){
          alert("날짜를 입력해주세요!")
        }
        else if(month.value==""){
          alert("날짜를 입력해주세요!")
        }
        else if(date.value==""){
          alert("날짜를 입력해주세요!")
        }
        else if(review.value==""){
          alert("리뷰를 작성해주세요!")
        }
        else{
          location.href="view_review.html"
        }
      }

      function setThumbnail(event) {
        var reader = new FileReader();
    
        reader.onload = function(event) {
          var img = document.createElement("img");
          img.setAttribute("src", event.target.result);
          document.querySelector("div#image_container").appendChild(img);
          
          img.style.width = "170px"; 
          img.style.height = "170px";
          img.style.position="absolute";
          img.style.top = "30%"; 
          img.style.left = "1.5%"; 
          img.style.borderRadius="100%";
        };
    
        reader.readAsDataURL(event.target.files[0]);
      }

