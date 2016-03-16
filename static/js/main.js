jQuery(document).ready(function($){
	
	// browser window scroll (in pixels) after which the "back to top" link is shown
	var offset = 300,
	
	//browser window scroll (in pixels) after which the "back to top" link opacity is reduced
	offset_opacity = 1200,
		
	//duration of the top scrolling animation (in ms)
	scroll_top_duration = 700,
		
	//grab the "back to top" link
	$back_to_top = $('.cd-top');

	$("#header").show();
	$("#loginTemplate").css("margin-top","280px");
	$("#indexTemplate").css("margin-top", "234px");
	$("#contactInfo").css("margin-top", "260px");
	$("#contactUs").css("margin-top", "275px");
	$("#realMonitoring").css("margin-top", "275px");
	$("#aboutUs").css("margin-top", "240px");
	$(".carousel-caption").show();

	//hide or show the "back to top" link
	$(window).scroll(function(){
		( $(this).scrollTop() > offset ) ? $back_to_top.addClass('cd-is-visible') : $back_to_top.removeClass('cd-is-visible cd-fade-out');
		
		$("#header").show();
		$("#indexTemplate").css("margin-top", "234px");
		$("#loginTemplate").css("margin-top","280px");
		$("#contactInfo").css("margin-top", "260px");
		$("#contactUs").css("margin-top", "275px"); 
		$("#realMonitoring").css("margin-top", "275px");
		$("#aboutUs").css("margin-top", "240px");
		$(".carousel-caption").show();

		if( $(this).scrollTop() > offset_opacity ) {
			$back_to_top.addClass('cd-fade-out');
		}
		if ($(this).scrollTop()) {
			$("#header").hide();
			$("#indexTemplate").css("margin-top", "60px"); 
			$("#loginTemplate").css("margin-top","110px");
			$("#contactInfo").css("margin-top", "60px");
			$("#contactUs").css("margin-top", "75px");
			$("#realMonitoring").css("margin-top", "85px");
			$("#aboutUs").css("margin-top", "50px");
			$(".carousel-caption").hide();
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

	$("#dropdown").hover(function(){
        $(".dropdown-menu").fadeIn("slow");
    });

    $("#dropdown").mouseleave(function(){
        $(".dropdown-menu").hide();
    });

});


$(function() {
$('a[href*=#]:not([href=#])').click(function() {
  if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
    var target = $(this.hash);

    target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
    if (target.length) {
      $('html,body').animate({
        scrollTop: target.offset().top
      }, 1000);
      return false;
    }
  }
});
});