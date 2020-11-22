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

    // $('#multiselect-medical-conditions').multiselect({
    // //includeSelectAllOption: true,
    // buttonClass: 'form-control',
    // buttonWidth: '100%',
    // buttonText: function(options, select) {
    //   return 'medical conditions';
    // },
    // maxHeight: 400,
    // });

    // $('#multiselect-alergens').multiselect({
    // //includeSelectAllOption: true,
    // buttonClass: 'form-control',
    // buttonWidth: '100%',
    // buttonText: function(options, select) {
    //   return 'alergens';
    // },
    // });

    $('#multiselect-course').multiselect({
    //includeSelectAllOption: true,
    buttonClass: 'form-control',
    buttonWidth: '100%',
    buttonText: function(options, select) {
      return 'course';
    },
    });

});





$(function() {

	$('#id_allergens').select2({
		width: '100%',
		placeholder: "Add / Remove",
	});

	$('#id_medical_conditions').select2({
		width: '100%',
		placeholder: "Add / Remove",
	});

	$('#id_risk_factors').select2({
		width: '100%',
		placeholder: "Add / Remove",
	});

    $('#id_meals-per-day').val("").multiselect({
    //includeSelectAllOption: true,
    buttonClass: 'form-control',
    buttonWidth: '100%',
    buttonText: function(options, select) {
      if (options.length === 0) {
          return 'meals per day';
      }
      else {
        var labels = [];
        options.each(function() {
          if ($(this).attr('label') !== undefined) {
            labels.push($(this).attr('label'));
          }
          else {
            labels.push($(this).html());
          }
        });
        return labels.join(', ') + '';
      }
    }
    });

    $('#multiselect-sex').val("").multiselect({
    //includeSelectAllOption: true,
    buttonClass: 'form-control',
    buttonWidth: '100%',
    buttonText: function(options, select) {
      if (options.length === 0) {
          return 'biological sex';
      }
      else {
        var labels = [];
        options.each(function() {
          if ($(this).attr('label') !== undefined) {
            labels.push($(this).attr('label'));
          }
          else {
            labels.push($(this).html());
          }
        });
        return labels.join(', ') + '';
      }
    }
    });

    $('#multiselect-metrics').val("").multiselect({
    //includeSelectAllOption: true,
    buttonClass: 'form-control',
    buttonWidth: '100%',

    buttonText: function(options, select) {
      if (options.length === 0) {
          return 'Select metrics';
      }
      else {
        var labels = [];
        options.each(function() {
          if ($(this).attr('label') !== undefined) {
            labels.push($(this).attr('label'));
          }
          else {
            labels.push($(this).html());
          }
        });
        return labels.join(', ') + '';
      }
    }
    });

    $('.datepicker').datepicker();

});


