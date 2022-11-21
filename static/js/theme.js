
$('document').ready(function() {
  $('#doctorSlideshow').owlCarousel({
    nav: true,
    dots: false,
    navText: ["<span class='mai-arrow-back'></span>", "<span class='mai-arrow-forward'></span>"],
    responsive: {
      0: {
        items: 1
      },
      576: {
        items: 2
      },
      992: {
        items: 3
      }
    }
  });
});

$('document').ready(function() {
  $("a[data-role='smoothscroll']").click(function(e) {
    e.preventDefault();
    
    var position = $($(this).attr("href")).offset().top - nav_height;

    $("body, html").animate({
        scrollTop: position
    }, 1000 );
    return false;
  });
});

$('document').ready(function() {
  // Back to top
  var backTop = $(".back-to-top");

  $(window).scroll(function() {
    if($(document).scrollTop() > 400) {
      backTop.css('visibility', 'visible');
    }
    else if($(document).scrollTop() < 400) {
      backTop.css('visibility', 'hidden');
    }
  });

  backTop.click(function() {
    $('html').animate({
      scrollTop: 0
    }, 1000);
    return false;
  });
});


$('document').ready(function() {
  // Tooltips
  $('[data-toggle="tooltip"]').tooltip();

  // Popovers
  $('[data-toggle="popover"]').popover();

  // Page scroll animate
  new WOW().init();
});

$('#fileup').change(function(){
  //here we take the file extension and set an array of valid extensions
      var res=$('#fileup').val();
      var arr = res.split("\\");
      var filename=arr.slice(-1)[0];
      filextension=filename.split(".");
      filext="."+filextension.slice(-1)[0];
      valid=[".jpg",".png",".jpeg",".bmp"];
  //if file is not valid we show the error icon, the red alert, and hide the submit button
      if (valid.indexOf(filext.toLowerCase())==-1){
          $( ".imgupload" ).hide("slow");
          $( ".imgupload.ok" ).hide("slow");
          $( ".imgupload.stop" ).show("slow");
        
          $('#namefile').css({"color":"red","font-weight":700});
          $('#namefile').html("File "+filename+" is not  pic!");
          
          $( "#submitbtn" ).hide();
          $( "#fakebtn" ).show();
      }else{
          //if file is valid we show the green alert and show the valid submit
          $( ".imgupload" ).hide("slow");
          $( ".imgupload.stop" ).hide("slow");
          $( ".imgupload.ok" ).show("slow");
        
          $('#namefile').css({"color":"green","font-weight":700});
          $('#namefile').html(filename);
        
          $( "#submitbtn" ).show();
          $( "#fakebtn" ).hide();
      }
  });