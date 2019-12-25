$(document).ready(function() {
    
        // scrollUp
	$(function(){
		$.scrollUp({
			scrollText: '<i class="fa fa-angle-up" aria-hidden="true"></i>',
			easingType: 'linear',
			scrollSpeed: 600,
			animation: 'fade'
		});
	});
    
        // slick.js
    $('.active-by-appetizer').slick({
        speed: 700,
        autoplay : true,
        arrows: true,
        dots: false,
        slidesToShow: 4,
        slidesToScroll: 1,
        prevArrow: '<button type="button" class="arrow-prev"><i class="fa fa-long-arrow-left" aria-hidden="true"></i></button>',
        nextArrow: '<button type="button" class="arrow-next"><i class="fa fa-long-arrow-right"></i></button>',
        responsive: [
            { breakpoint: 991, settings: { slidesToShow: 3 }  },
            { breakpoint: 767, settings: { slidesToShow: 1 }  },
            { breakpoint: 479, settings: { slidesToShow: 1 }  }
        ]
    });
});