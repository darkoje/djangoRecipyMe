$(function() {

  /* Swiper
	**************************************************************/
	var swiper= Swiper;
	var init = false;

	/* Which media query
	**************************************************************/
	function swiperMode() {
	  let mobile = window.matchMedia('(min-width: 0px) and (max-width: 768px)');
	  let desktop = window.matchMedia('(min-width: 769px)');

	  // Enable (for mobile)
	  if(mobile.matches) {
	    if (!init) {
	      init = true;
	      swiper = new Swiper('#swiper-posts', {
	        effect: 'slide',
	        loop: false,
	        slidesPerView: 'auto',
	        spaceBetween: 0,
	        });
	      }
	    }

	    // Disable (for desktop)
	    else if(desktop.matches) {
	      swiper.destroy();
	      init = false;
	    }
	  }

	  /* On Load
	  **************************************************************/
	  window.addEventListener('load', function() {
	    swiperMode();
	  });

	  /* On Resize
	  **************************************************************/
	  window.addEventListener('resize', function() {
	    swiperMode();
	  });

});

$(function() {

    $('#multiselect-medical-conditions').multiselect({
    //includeSelectAllOption: true,
    buttonClass: 'form-control',
    buttonWidth: '100%',
    buttonText: function(options, select) {
      return 'medical conditions';
    },
    maxHeight: 400,
    });

    $('#multiselect-alergens').multiselect({
    //includeSelectAllOption: true,
    buttonClass: 'form-control',
    buttonWidth: '100%',
    buttonText: function(options, select) {
      return 'alergens';
    },
    });

    $('#multiselect-course').multiselect({
    //includeSelectAllOption: true,
    buttonClass: 'form-control',
    buttonWidth: '100%',
    buttonText: function(options, select) {
      return 'course';
    },
    });

});