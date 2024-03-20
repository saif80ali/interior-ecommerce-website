function showing(){
    $(".signup-form1").addClass("hiding1")
    $(".hiding1").removeClass("signup-form1")
    $(".hiding").addClass("signup-form")
    $(".hiding").removeClass("hiding")

}
function hiding(){
    $(".signup-form").addClass("hiding")
    $(".hiding").removeClass("signup-form")

}

function showing1(){
    $(".signup-form").addClass("hiding")
    $(".hiding").removeClass("signup-form")
    $(".hiding1").addClass("signup-form1")
    $(".hiding1").removeClass("hiding1")

}
function hiding1(){
    $(".signup-form1").addClass("hiding1")
    $(".hiding1").removeClass("signup-form1")

}


function logout(){
  console.log("iihh")
  window.location.replace("Home.py?msg=def&username=None")
}




$("#show-pass1").click(function(){
if ($('#show-pass1').is(":checked")){
  $('#password1').attr('type', 'text');
}
else{
  $('#password1').attr('type', 'password');
}
})

$("#show-pass").click(function(){
if ($('#show-pass').is(":checked")){
  $('#password').attr('type', 'text');
}
else{
  $('#password').attr('type', 'password');
}
})
$(".input").click(function(){
  $(".input").removeClass("red")
  $("#nouser").addClass("hide")

})
$("#burger").click(function(){
  $("nav").toggleClass("nav-media")
  $("ul").toggleClass("ul-media")
  $("li").toggleClass("li-media")
  $(".a").toggleClass("a-media")
})