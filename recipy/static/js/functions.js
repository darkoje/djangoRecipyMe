$(document).ready(function() {

	// browser window scroll (in pixels) after which the "back to top" link is shown
  var offset = 300,
    //browser window scroll (in pixels) after which the "back to top" link opacity is reduced
    offset_opacity = 1200,
    //duration of the top scrolling animation (in ms)
    scroll_top_duration = 700,
    //grab the "back to top" link
    $back_to_top = $('.cd-top');

  // grid breakpoints from variables input from sass
  var grid_breakpoints_sm = 576,
      grid_breakpoints_md = 768,
      grid_breakpoints_lg = 1100,
      grid_breakpoints_xl = 1430,
      nav_breakpoint      = 1100;

  //hide or show the "back to top" link
  $(window).scroll(function(){
    ( $(this).scrollTop() > offset ) ? $back_to_top.addClass('cd-is-visible') : $back_to_top.removeClass('cd-is-visible cd-fade-out');
    if( $(this).scrollTop() > offset_opacity ) {
      $back_to_top.addClass('cd-fade-out');
    }
  });

  //smooth scroll to top
  $back_to_top.on('click', function(event){
    event.preventDefault();
    $('body,html').animate({
      scrollTop: 0 ,
      }, scroll_top_duration
    );
  });

  // Smooth Scroll
  $('.js-scroll[href*="#"] , .nav-link[href*="#"]').click(function(e) {
    e.preventDefault();
    if ($(this.hash).offset()) {
      var heightFromTop = parseInt($(this.hash).offset().top, 10) - 60;
      $('html,body').animate({scrollTop: heightFromTop}, 600);
    }
  });

  // Navbar Toggler
  $(".navbar-toggler").on('click', function() {
    $(this).toggleClass('active');
    $('#mainMenu').toggleClass('active');
    $('#page').toggleClass('active');
    $('.menu-overlay').toggleClass('active');
  });

  $(".menu-overlay").click(function(event) {
    $(".navbar-toggler").trigger("click");
  });

  // Search Toggler
  $(".js-search-toggle").on('click', function() {
    $(this).toggleClass('active');
    $('.search-overlay').toggleClass('active');
  });

  // Recipe List Toggler
  $(".js-recipe-list-toggle").on('click', function() {
    $(this).toggleClass('active');
    $('.recipe-list-overlay').toggleClass('active');
  });

  // close elements on outside click
  function closeActiveElement(el) {
    $(document).on('mouseup', function(e) {
      var container = el;
      if(!container.is(e.target) && container.has(e.target).length === 0) {
        container.removeClass('active');
      }
    });
  }
  closeActiveElement($('.js-search-toggle, .header-search'));


  // Filter Toggler
  $(".js-filter-toggle").on('click', function() {
    $(this).toggleClass('active');
    $('.section-filter').toggleClass('active');
  });

  // Healthmeter Toggler
  $(".js-values-toggle").on('change', function() {
    $(this).toggleClass('active');
    $('.js-show-healthmeter').toggleClass('active');
    $('.js-show-values').toggleClass('active');
  });

  // Recipe Overlay Toggler on Mobile
  if ($(window).width() < grid_breakpoints_md) {
    $(".post-box").on('click', function() {
      $(".post-box").find(".post-box-add").removeClass('active');
      $(this).find(".post-box-add").toggleClass('active');
    });
  };

});