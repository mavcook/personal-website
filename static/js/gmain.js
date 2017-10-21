
//Stickynavbar
var navBar = $('#navBarDiv');
var headerDiv = $('#headerDiv');
var	headerHeight = headerDiv.height();
var isNavStuck = false;
var header = document.getElementById('headerDiv');
var contentDiv = $('#content');
var logoClass = $('.logo');
var cyclerDiv = $('#cycler');

//Only bind on non-project-view pages (nav is fixed on project view)
if (document.title.indexOf('Project-View') === -1){
	$(window).scroll(function()
	{
		
		var st = $(document).scrollTop();

		if ( st > headerHeight && isNavStuck === false)
		{
			navBar.attr('class', 'navBarDiv-scrolled');
			if (header)
				header.style.display = 'none'; //optional
			var newMarg = navBar[0].clientHeight;
			contentDiv.css('marginTop', newMarg + 'px');
			isNavStuck = true;
			
		}
		else if (st <= headerHeight && isNavStuck === true)
		{
			navBar.attr('class', '');
			if (header)
				header.style.display = 'block'; //optional
			contentDiv.css('marginTop', '0');
			isNavStuck = false;
		}
		
		//Parallax effect
		if(st <= headerHeight)
		{
			cyclerDiv.css('margin-top', $(window).scrollTop() * -.1);
			logoClass.css('margin-top', $(window).scrollTop() * -.3);
		}
		
	});	
}


//update navbar stick when window is resized
$(window).resize(function () 
{  
    headerHeight = headerDiv.height();
});





//Thanks to http://www.simonbattersby.com/blog/simple-jquery-image-crossfade/
function cycleImages(){
	var $active = $('#cycler .active');
	var $next = ($active.next().length > 0) ? $active.next() : $('#cycler img:first');
	$next.css('z-index',2);//move the next image up the pile
	$active.fadeOut(1500,function(){//fade out the top image
		$active.css('z-index',1).show().removeClass('active');//reset the z-index and unhide the image
		$next.css('z-index',3).addClass('active');//make the next image the top one
		// Store current image
		currentImage = $next.attr('id');
		document.cookie = 'hImg=' + currentImage + ';path=/';

		localStorage.setItem('active', $('#cycler .active'));
	});
}
//Effects: scales logo and changes background picture
function swapHeaderImg()
{
	$(document).ready(function(){cycleImages();});
}






$('#logoImg').click(
	function() 
	{
		$(this).addClass('popAndDrop').one(
			'animationend webkitAnimationEnd oAnimationEnd', function()
		{
			$(this).removeClass('popAndDrop');
		});
		swapHeaderImg();
	}
);
	
	
	
	
var mobileMenuOpen = false;
var navHeight = 2.4; //em | first media query after mobile
var numNavLinks = $('nav').children().length;
// Hamburger menu
$('#sel').click(function() 
{
	if (mobileMenuOpen)
		navBar.animate({'height': navHeight +'em', 'opacity':'1'}, 'slow');
	else
		navBar.animate({'height': navHeight * numNavLinks -.2 + 'em', 'opacity':'.95'}, 'slow');
	// -.2 because nav links dont actually have set height -- just aproximating here
	mobileMenuOpen = !mobileMenuOpen;
	event.stopPropagation(); //because of window click listener line 126
});


//Prevent expanded mobile nav height from carrying over on resize
function resetToDeskNav()
{
	if (window.innerWidth >= 400)
	{
		navBar[0].style.height = '2.4em';
		navBar[0].style.opacity = '1';
		mobileMenuOpen = false;
	}
};
// Remove open mobile menu when it loses focus
$(window).click(function(){
	if (mobileMenuOpen)
	{
		navBar.animate({'height': navHeight +'em', 'opacity':'1'}, 'slow');
		mobileMenuOpen = false;
	}
});




window.onresize = function(){resetToDeskNav();};