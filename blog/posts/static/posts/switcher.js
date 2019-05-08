var texts = ["Now", "Everywhere", "Everytime", "Here"];
var i = 0;
setInterval(
    function(){
         document.getElementById("mySpan").innerHTML=texts[i]; 
         i += 1;
         if (i>3) {
             i = 0;
         }
        },
     1000);