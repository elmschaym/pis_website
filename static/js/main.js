jQuery(document).ready(function($){
	
	// browser window scroll (in pixels) after which the "back to top" link is shown
	var offset = 300,
	//browser window scroll (in pixels) after which the "back to top" link opacity is reduced
	offset_opacity = 1200,
	//duration of the top scrolling animation (in ms)
	scroll_top_duration = 700,
	//grab the "back to top" link
	$back_to_top = $('.cd-top');

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

    $('#carousel').flexslider({
        speed: 100,            
        animation: "slide",
        controlNav: false,
        animationLoop: false,
        slideshow: false,
        itemWidth: 210,
        itemMargin: 5,
        asNavFor: '#slider'
      });

      $('#slider').flexslider({
      	speed: 100,
        animation: "slide",
        controlNav: false,
        animationLoop: true,
        slideshow: true,
        sync: "#carousel",
        start: function(slider){
          $('body').removeClass('loading');
        }
      });

    $("#dropdown").hover(function(){
        $(".dropdown-menu").fadeIn("slow");
    });

    $("#dropdown").mouseleave(function(){
        $(".dropdown-menu").hide();
    });

	window.onresize=function() {

	    if ($("body").outerWidth() < 1200) {

	    	$("#imgHeader").hide();
	    	$("#slider").hide();
		    $("#carousel").hide();

		    $("#indexTables").css("margin-top", "-115px");
			$("#loginTemplate").css("margin-top","90px");
			$("#loginBase").css("margin-top", "90px");
		    $("#realMonitoring").css("margin-top", "90px");
		    $("#contactInfo").css("margin-top", "90px");
			$("#contactUs").css("margin-top", "90px"); 
			$("#aboutUs").css("margin-top", "60px");

	      	$(window).scroll(function(){
				( $(this).scrollTop() > offset ) ? $back_to_top.addClass('cd-is-visible') : $back_to_top.removeClass('cd-is-visible cd-fade-out');
				
				$("#imgHeader").hide();
		    	$("#slider").hide();
		    	$("#carousel").hide();

		    	$("#indexTables").css("margin-top", "-115px");
				$("#loginTemplate").css("margin-top","90px");
				$("#loginBase").css("margin-top", "90px");
			    $("#realMonitoring").css("margin-top", "90px");
			    $("#contactInfo").css("margin-top", "90px");
				$("#contactUs").css("margin-top", "90px"); 
				$("#aboutUs").css("margin-top", "60px");

				if( $(this).scrollTop() > offset_opacity ) {
					$back_to_top.addClass('cd-fade-out');
				}
				if ($(this).scrollTop()) {
					$("#imgHeader").hide();
		    		$("#slider").hide();
		    		$("#carousel").hide();
					
					$("#indexTables").css("margin-top", "-115px");
					$("#loginTemplate").css("margin-top","110px");
					$("#loginBase").css("margin-top", "100px");
					$("#realMonitoring").css("margin-top", "90px");
					$("#contactInfo").css("margin-top", "10px");
					$("#contactUs").css("margin-top", "90px");
					$("#aboutUs").css("margin-top", "50px");
				}
			});

	    } else {
	      	
	      	$("#imgHeader").show();
		   	$("#slider").show();
		    $("#carousel").show();

	    	$("#indexTemplate").css("margin-top", "233px");
	    	$("#indexTables").css("margin-top", "10px");
			$("#loginTemplate").css("margin-top","280px");
			$("#loginBase").css("margin-top", "280px");
			$("#realMonitoring").css("margin-top", "280px");
			$("#contactInfo").css("margin-top", "260px");
			$("#contactUs").css("margin-top", "275px");
			$("#aboutUs").css("margin-top", "240px");


	    	$(window).scroll(function(){
				( $(this).scrollTop() > offset ) ? $back_to_top.addClass('cd-is-visible') : $back_to_top.removeClass('cd-is-visible cd-fade-out');
			
				$("#imgHeader").show();
				$("#slider").show();
		    	$("#carousel").show();
				
				$("#indexTemplate").css("margin-top", "233px");
				$("#indexTables").css("margin-top", "10px");
				$("#loginTemplate").css("margin-top","280px");
				$("#loginBase").css("margin-top", "280px");
				$("#realMonitoring").css("margin-top", "280px");
				$("#contactInfo").css("margin-top", "260px");
				$("#contactUs").css("margin-top", "275px"); 
				$("#aboutUs").css("margin-top", "240px");

				if( $(this).scrollTop() > offset_opacity ) {
					$back_to_top.addClass('cd-fade-out');
				}
				if ($(this).scrollTop()) {

					$("#imgHeader").hide();

					$("#indexTemplate").css("margin-top", "60px"); 
					$("#loginTemplate").css("margin-top","110px");
					$("#loginBase").css("margin-top", "110px");
					$("#realMonitoring").css("margin-top", "85px");
					$("#contactInfo").css("margin-top", "60px");
					$("#contactUs").css("margin-top", "75px");
					$("#aboutUs").css("margin-top", "60px");
				}
			});
	    }
  	};


    if ($("body").outerWidth() < 1200) {
    	
    	$("#imgHeader").hide();
	   	$("#slider").hide();
		$("#carousel").hide();

	    $("#indexTables").css("margin-top", "70px");
		$("#loginTemplate").css("margin-top","90px");
		$("#loginBase").css("margin-top", "90px");
	    $("#realMonitoring").css("margin-top", "90px");
	    $("#contactInfo").css("margin-top", "90px");
		$("#contactUs").css("margin-top", "90px"); 
		$("#aboutUs").css("margin-top", "60px");

	    $(window).scroll(function(){
			( $(this).scrollTop() > offset ) ? $back_to_top.addClass('cd-is-visible') : $back_to_top.removeClass('cd-is-visible cd-fade-out');
			
			if( $(this).scrollTop() > offset_opacity ) {
				$back_to_top.addClass('cd-fade-out');
			}
			if ($(this).scrollTop()) {
				$("#imgHeader").hide();
	    		$("#slider").hide();
		    	$("#carousel").hide();
				
				$("#indexTables").css("margin-top", "70px");
				$("#loginTemplate").css("margin-top","110px");
				$("#loginBase").css("margin-top", "90px");
				$("#realMonitoring").css("margin-top", "90px");
				$("#contactInfo").css("margin-top", "90px");
				$("#contactUs").css("margin-top", "90px");
				$("#aboutUs").css("margin-top", "60px");
			}
		});

    } else {

    	$("#imgHeader").show();
	    $("#slider").show();
		$("#carousel").show();

    	$("#indexTemplate").css("margin-top", "234px");
		$("#loginTemplate").css("margin-top","280px");
		$("#loginBase").css("margin-top", "280px");
		$("#realMonitoring").css("margin-top", "280px");
		$("#contactInfo").css("margin-top", "260px");
		$("#contactUs").css("margin-top", "275px");
		$("#aboutUs").css("margin-top", "240px");


    	$(window).scroll(function(){
			( $(this).scrollTop() > offset ) ? $back_to_top.addClass('cd-is-visible') : $back_to_top.removeClass('cd-is-visible cd-fade-out');
		
			$("#imgHeader").show();
			$("#slider").show();
		    $("#carousel").show();

			$("#indexTemplate").css("margin-top", "234px");
			$("#loginTemplate").css("margin-top","280px");
			$("#loginBase").css("margin-top", "280px");
			$("#realMonitoring").css("margin-top", "280px");
			$("#contactInfo").css("margin-top", "260px");
			$("#contactUs").css("margin-top", "275px"); 
			$("#aboutUs").css("margin-top", "240px");

			if( $(this).scrollTop() > offset_opacity ) {
				$back_to_top.addClass('cd-fade-out');
			}
			if ($(this).scrollTop()) {

				$("#imgHeader").hide();
				
				$("#indexTemplate").css("margin-top", "55px"); 
				$("#loginTemplate").css("margin-top","110px");
				$("#loginBase").css("margin-top", "110px");
				$("#realMonitoring").css("margin-top", "85px");
				$("#contactInfo").css("margin-top", "60px");
				$("#contactUs").css("margin-top", "75px");
				$("#aboutUs").css("margin-top", "60px");
			}
		});
    }
});


/*$(function() {
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
});*/