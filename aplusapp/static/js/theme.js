
"use strict";




// Prealoder
 function prealoader () {
   if ($('#loader').length) {
     $('#loader').fadeOut(); // will first fade out the loading animation
     $('#loader-wrapper').delay(350).fadeOut('slow'); // will fade out the white DIV that covers the website.
     $('body').delay(350).css({'overflow':'visible'});
  };
 }


// placeholder remove
function removePlaceholder () {
  if ($("input,textarea").length) {
    $("input,textarea").each(
            function(){
                $(this).data('holder',$(this).attr('placeholder'));
                $(this).on('focusin', function() {
                    $(this).attr('placeholder','');
                });
                $(this).on('focusout', function() {
                    $(this).attr('placeholder',$(this).data('holder'));
                });
                
        });
  }
}


// Theme-banner slider 
function BannerSlider () {
  if ($("#main-banner-slider").length) {
    $("#main-banner-slider").revolution({
      sliderType:"standard",
      sliderLayout:"auto",
      loops:false,
      delay:7000,
      navigation: {
          arrows: {
                    style: "hermes",
                    enable: true,
                    hide_onmobile: false,
                    hide_onleave: false,
                    tmp: '<div class="tp-arr-allwrapper"> <div class="tp-arr-imgholder"></div>  <div class="tp-arr-titleholder">{{title}}</div> </div>',
                    left: {
                        h_align: "left",
                        v_align: "center",
                        h_offset: 0,
                        v_offset: 60
                    },
                    right: {
                        h_align: "right",
                        v_align: "center",
                        h_offset: 0,
                        v_offset: 60
                    }
                },
         bullets: {
                  enable: true,
                  hide_onmobile: false,
                  style: "uranus",
                  hide_onleave: false,
                  direction: "horizontal",
                  h_align: "center",
                  v_align: "bottom",
                  h_offset: -15,
                  v_offset: 30,
                  space: 10,
                  tmp: '<span class="tp-bullet-inner"></span>'
              }

      },
      responsiveLevels:[2220,1183,975,751],
                gridwidth:[1170,970,770,350],
                gridheight:[950,950,900,700],
                shadow:0,
                spinner:"off",
                autoHeight:"off",
                disableProgressBar:"on",
                hideThumbsOnMobile:"off",
                hideSliderAtLimit:0,
                hideCaptionAtLimit:0,
                hideAllCaptionAtLilmit:0,
                debugMode:false,
                fallbacks: {
                  simplifyAll:"off",
                  disableFocusListener:false,
                }   
    }); 
  };
}


// Time Picker
function timeSelect () {
  if ($(".timepicker").length) {
    $(".timepicker").timepicker();
  }
}


// WOW animation 
function wowAnimation () {
  if($('.wow').length) {
    var wow = new WOW(
    {
      boxClass:     'wow',      // animated element css class (default is wow)
      animateClass: 'animated', // animation css class (default is animated)
      offset:       50,          // distance to the element when triggering the animation (default is 0)
      mobile:       true,       // trigger animations on mobile devices (default is true)
      live:         true,       // act on asynchronously loaded content (default is true)
      callback:     function(box) {
        // the callback is fired every time an animation is started
        // the argument that is passed in is the DOM node being animated
      },
      scrollContainer: null // optional scroll container selector, otherwise use window
    }
  );
  wow.init();
  }
}



// Theme Slider
function themeSlider () {
  if($('.theme-slider').length) {
    $('.theme-slider').owlCarousel({
        loop:true,
        nav:false,
        navText:false,
        dots:true,
        autoplay:true,
        autoplayTimeout:3500,
        autoplaySpeed:1000,
        lazyLoad:true,
        responsive:{
            0:{
                items:1
            },
            651:{
                items:2
            },
            992:{
                items:3
            }
        }
    })
  }
}



// Google Map 
function googlMap () {
  if($("#google-map").length) {
    var settingsItemsMap = {
          zoom: 12,
          center: new google.maps.LatLng(40.925372, -74.276544),
          zoomControlOptions: {
            style: google.maps.ZoomControlStyle.LARGE
          },
          scrollwheel: false,
          mapTypeId: google.maps.MapTypeId.ROADMAP
      };
      var map = new google.maps.Map(document.getElementById('google-map'), settingsItemsMap );
      var image = 'images/logo/map.png';
      var myMarker = new google.maps.Marker({
          position: new google.maps.LatLng(40.925372, -74.276544),
          draggable: true,
          icon: image
      });

      map.setCenter(myMarker.position);
      myMarker.setMap(map);
      // Google map 
  };
}

// Counter function
function CounterNumberChanger () {
  var timer = $('.timer');
  if(timer.length) {
    timer.appear(function () {
      timer.countTo();
    })
  }
}

// Scroll to top
function scrollToTop () {
  if ($('.scroll-top').length) {

    //Check to see if the window is top if not then display button
    $(window).on('scroll', function (){
      if ($(this).scrollTop() > 200) {
        $('.scroll-top').fadeIn();
      } else {
        $('.scroll-top').fadeOut();
      }
    });
    
    //Click event to scroll to top
    $('.scroll-top').on('click', function() {
      $('html, body').animate({scrollTop : 0},1500);
      return false;
    });
  }
}



//Contact Form Validation
function contactFormValidation () {
  if($('.form-validation').length){
    $('.form-validation').validate({ // initialize the plugin
      rules: {
        name: {
          required: true
        },
        email: {
          required: true,
          email: true
        },
        sub: {
          required: true
        },
        message: {
          required: true
        }
      },
      submitHandler: function(form) {
                $(form).ajaxSubmit({
                    success: function() {
                        $('.form-validation :input').attr('disabled', 'disabled');
                        $('.form-validation').fadeTo( "slow", 1, function() {
                            $(this).find(':input').attr('disabled', 'disabled');
                            $(this).find('label').css('cursor','default');
                            $('#alert_success').fadeIn();
                        });
                    },
                    error: function() {
                        $('.form-validation').fadeTo( "slow", 1, function() {
                            $('#alert_error').fadeIn();
                        });
                    }
                });
            }
        });
  }
}

// Close suddess Alret
function closeSuccessAlert () {
  if($('.closeAlert').length) {
    $(".closeAlert").on('click', function(){
      $(".alert_wrapper").fadeOut();
    });
    $(".closeAlert").on('click', function(){
      $(".alert_wrapper").fadeOut();
    })
  }
}


// Sticky header
function stickyHeader () {
  if ($('.main-menu-wrapper').length) {
    var sticky = $('.main-menu-wrapper'),
        scroll = $(window).scrollTop();

    if (scroll >= 190) sticky.addClass('fixed');
    else sticky.removeClass('fixed');
    
  };
}


// toggle menu for mobile
function mobileDropdown () {
  if($('.main-menu-wrapper').length) {
    $('.main-menu-wrapper nav ul li.dropdown-holder').append(function () {
      return '<i class="fa fa-angle-down" aria-hidden="true"></i>';
    });
    $('.main-menu-wrapper nav ul li.dropdown-holder .fa').on('click', function () {
      $(this).parent('li').children('ul').slideToggle();
    }); 
  }
}




// Accordion panel
function themeAccrodion () {
  if ($('.theme-accordion > .panel').length) {
    $('.theme-accordion > .panel').on('show.bs.collapse', function (e) {
          var heading = $(this).find('.panel-heading');
          heading.addClass("active-panel");
          
    });
    
    $('.theme-accordion > .panel').on('hidden.bs.collapse', function (e) {
        var heading = $(this).find('.panel-heading');
          heading.removeClass("active-panel");
          //setProgressBar(heading.get(0).id);
    });

  };
}

// DOM ready function
jQuery(document).on('ready', function() {
	(function ($) {
	   removePlaceholder ();
     BannerSlider ();
     timeSelect ();
     wowAnimation ();
     themeSlider ();
     CounterNumberChanger ();
     googlMap ();
     scrollToTop ();
     contactFormValidation ();
     closeSuccessAlert ();
     mobileDropdown ();
     themeAccrodion ();
  })(jQuery);
});


// Window load function
jQuery(window).on('load', function () {
   (function ($) {
		  prealoader ()
  })(jQuery);
 });


// Window scroll function
jQuery(window).on('scroll', function () {
  (function ($) {
    stickyHeader ();
  })(jQuery);
});
