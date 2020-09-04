// // Make the DIV element draggable:
// dragElement(document.getElementById("mydiv"));
//
// function dragElement(elmnt) {
//   var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
//   if (document.getElementById(elmnt.id + "header")) {
//     // if present, the header is where you move the DIV from:
//     document.getElementById(elmnt.id + "header").onmousedown = dragMouseDown;
//   } else {
//     // otherwise, move the DIV from anywhere inside the DIV:
//     elmnt.onmousedown = dragMouseDown;
//   }
//
//   function dragMouseDown(e) {
//     e = e || window.event;
//     e.preventDefault();
//     // get the mouse cursor position at startup:
//     pos3 = e.clientX;
//     pos4 = e.clientY;
//     document.onmouseup = closeDragElement;
//     // call a function whenever the cursor moves:
//     document.onmousemove = elementDrag;
//   }
//
//   function elementDrag(e) {
//     e = e || window.event;
//     e.preventDefault();
//     // calculate the new cursor position:
//     pos1 = pos3 - e.clientX;
//     pos2 = pos4 - e.clientY;
//     pos3 = e.clientX;
//     pos4 = e.clientY;
//     // set the element's new position:
//     elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
//     elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
//   }
//
//   function closeDragElement() {
//     // stop moving when mouse button is released:
//     document.onmouseup = null;
//     document.onmousemove = null;
//   }
// }

         $(".nav__link--hide").toggle();

         $(document).ready(function(){
           $(".profile").click(function(){
             $(this).parent().find(".nav__link--hide").toggle(200);

             $(this).toggleClass(".nav__link--pressed");
           });
         });

//   $(".hover-icon").toggle();
// //   $(".story-text").toggle();
//   $(document).ready(function(){
//     $(".stitle").click(function(){
//       $(this).parent().parent().find(".story-text").toggle(200);
//     });
//   });



//  $(function() {
//   $('.story').hover(function() {
//     $(this).find('.hover-icon').toggle(200);
//   }, function() {
//     $(this).find('.hover-icon').toggle(200);
//   });
// });

  $(document).ready(function(){
    $(".fa-user-plus").click(function(){
      $(this).parent().find(".uuid-input");
        var copyText = $(this).parent().find(".uuid-input").get(0);
        copyText.select();
        copyText.setSelectionRange(0, 99999);
         document.execCommand("copy");
          alert("Share link has been copied to you clipboard: " + copyText.value);

    });
  });
             console.log("sasd");
  $(".event-hide").toggle();
  $(".description").toggle();
  $('.comments').toggle();
  $('.event--completed').toggle();
//   $('.top-bar__button').toggle();


  $(document).ready(function(){
    $(".event-title").click(function(){
    $(this).parent().parent().find(".event-hide").toggle();
    // if ($(this).parent().hasClass('event--completed')) {
    //       $(this).parent().toggleClass('event-complete');

    // };



    });
  });

  $(document).ready(function(){
    $(".show_description").click(function(){
      if ( $(this).parent(".col").find(".description").is(':hidden')){
        $(this).parent(".col").find(".description").show(); }
      else {
        $(this).parent(".col").find(".description").hide();
      }
    });
  });

  $(document).ready(function(){
    $(".showall").click(function(){
        $(this).toggleClass('unpressed pressed');
        if ($(this).hasClass('unpressed')) {
          $(".event-hide").hide();
        }
        else if ($(this).hasClass('pressed')) {
          $(".event-hide").show();

        }


    });
  });

  $(document).ready(function(){
    $(".completed-events-box").click(function(){
        $(this).parents(".events-container").find(".event--completed").toggle();
    });
  });






  $(document).ready(function(){
    $(".open-comments").click(function(){
        $(this).parent().find('.comments').toggle();

      });
    });
  function myFunction() {
    /* Get the text field */
    var copyText = document.getElementById("myInput");

    /* Select the text field */
    copyText.select();
    copyText.setSelectionRange(0, 99999); /*For mobile devices*/

    /* Copy the text inside the text field */
    document.execCommand("copy");

    /* Alert the copied text */
    alert("Copied the text: " + copyText.value);
  };

  $.ajaxSetup({
       beforeSend: function(xhr, settings) {
           function getCookie(name) {
               var cookieValue = null;
               if (document.cookie && document.cookie != '') {
                   var cookies = document.cookie.split(';');
                   for (var i = 0; i < cookies.length; i++) {
                       var cookie = jQuery.trim(cookies[i]);
                       // Does this cookie string begin with the name we want?
                       if (cookie.substring(0, name.length + 1) == (name + '=')) {
                           cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                           break;
                       }
                   }
               }
               return cookieValue;
           }
           if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
               // Only send the token to relative URLs i.e. locally.
               xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
           }
       }
  });




      $(".fa-circle").click(function (e) {
        $(this).toggleClass('fa-circle fa-check-circle');
         e.preventDefault();
          var pk = $(this).data("pk");
          console.log("sasd");
          $.ajax({
            type: "POST",
            url: $(this).attr("data-href"),
              data: {
                csrfmiddlewaretoken: '{{ csrf_token }}',
                  'pk': pk},
              dataType: "json",
              success: function(response) {

              }
          });
      });

      $(".fa-check-circle").click(function (e) {
        $(this).toggleClass('fa-circle fa-check-circle');
         e.preventDefault();
          var pk = $(this).data("pk");

          $.ajax({
            type: "POST",
            url: $(this).attr("data-href"),
              data: {
                csrfmiddlewaretoken: '{{ csrf_token }}',
                  'pk': pk},
              dataType: "json",
              success: function(response) {

              }
          });
      });


        $(".fa-circle, .fa-check-circle").click(function(){
            var comple = $(this).parents(".events-container").find('.fa-check-circle').length;

            $(this).parents(".storyline-content").find('.completed-events-box__count').html(comple);
            if (comple==0) {
              $(this).parents(".events-container").find('.completed-events-box').addClass('nocompleted');

            }
            else {
              $(this).parents(".events-container").find('.completed-events-box').removeClass('nocompleted');
            }
});


//         $(".compl").click(function(){
//             var comple = $(this).parents(".container-events").find('.fa-check-circle').length;
//             console.log(comple);
//             $(this).parents(".storyline-content").find('.output').html(comple);

// });

$( ".events-container" ).each( function( index, element ){
    var comple = $(this).find('.fa-check-circle').length;
    $(this).find('.completed-events-box__count').html(comple);
    if (comple==0) {
      $(this).find('.completed-events-box').addClass('nocompleted');
    }
});

// function myFunction() {
//   /* Get the text field */
//   var copyText = document.getElementById("myInput");

//   /* Select the text field */
//   copyText.select();
//   copyText.setSelectionRange(0, 99999); /*For mobile devices*/

//   /* Copy the text inside the text field */
//   document.execCommand("copy");

//   /* Alert the copied text */
//   alert("Copied the text: " + copyText.value);
// }

