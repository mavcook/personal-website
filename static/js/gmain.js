
//Stickynavbar
var navBar = $("#navBarDiv");
var	headerHeight = $("#headerDiv").height();
var isNavStuck = false;
var header = document.getElementById('headerDiv');
//Only bind on non-project-view pages (nav is fixed on project view)
if (document.title.indexOf('Project-View') == -1){
	$(window).scroll(function()
	{
		
		if ( $(document).scrollTop() > headerHeight && isNavStuck == false)
		{
			navBar.addClass("navBarDiv-scrolled");
			if (header)
				header.style.display = "none"; //optional
			var newMarg = document.getElementById('navBarDiv').clientHeight;
			$('#content').css('marginTop', newMarg + 'px');
			isNavStuck = true;
			
		}
		else if ($(document).scrollTop() <= headerHeight && isNavStuck == true)
		{
			navBar.removeClass("navBarDiv-scrolled");
			if (header)
				header.style.display = "block"; //optional
			$('#content').css('marginTop', '0');
			isNavStuck = false;
		}
		
		//Parallax effect
		if($(document).scrollTop() <= headerHeight)
		{
			$('#cycler').css('margin-top' , $(window).scrollTop() * -.1);
			$('.logo').css('margin-top', $(window).scrollTop() * -.3);
		}
		
	});	
}


//update navbar stick when window is resized
$(window).resize(function () 
{  
    headerHeight = $("#headerDiv").height();
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
	  document.cookie = "hImg=" + currentImage + ';path=/';

	  localStorage.setItem("active", $('#cycler .active'));
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
		$(this).addClass("popAndDrop").one(
			'animationend webkitAnimationEnd oAnimationEnd', function()
		{
			$(this).removeClass("popAndDrop");
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
		$("#navBarDiv").animate({'height': navHeight +'em', 'opacity':'1'}, 'slow');
	else
		$("#navBarDiv").animate({'height': navHeight * numNavLinks -.2 + 'em', 'opacity':'.95'}, 'slow');
	// -.2 because nav links dont actually have set height -- just aproximating here
	mobileMenuOpen = !mobileMenuOpen;
	event.stopPropagation(); //because of window click listener line 126
});


//Prevent expanded mobile nav height from carrying over on resize
function resetToDeskNav()
{
	if (window.innerWidth >= 400)
	{
		document.getElementById("navBarDiv").style.height = "2.4em";
		document.getElementById("navBarDiv").style.opacity = "1";
		mobileMenuOpen = false;
	}
};
// Remove open mobile menu when it loses focus
$(window).click(function(){
	if (mobileMenuOpen)
	{
		$("#navBarDiv").animate({'height': navHeight +'em', 'opacity':'1'}, 'slow');
		mobileMenuOpen = false;
	}
});





function replaceImgSrc(obj, oldSize, newSize)
{
	var oldSrc = obj.attr('src');
	var newSrc = oldSrc.replace(oldSize, newSize);
	obj.attr('src', newSrc);
}

// Header/Navbar media query breakpoints
var hnMed = 400, hnLarge = 800, pfLarge = 1000;

//booleans to prevent extra work for updating content on media query match
var hnMedQActive = false, hnLargeQActive = false, pfLargeQActive = false;
//change image src for larger screen sizes
function replaceMobileImages()
{
	width = window.innerWidth;
	
	
	//Header images
	if (width >= hnMed && width < hnLarge && hnMedQActive == false)
	{
		//update bools
		hnMedQActive = true;
		
		var headerImages = $('#cycler img');
		
		headerImages.each(function(){replaceImgSrc($(this), '_small', '_med');});
	}
	else if (width >= hnLarge && hnLargeQActive == false)
	{
		//update bools
		hnLargeQActive = true; 
		
		var headerImages = $('#cycler img');
		
		if (hnMedQActive == false)
			headerImages.each(function(){replaceImgSrc($(this), '_small', '_large');});
		else headerImages.each(function(){replaceImgSrc($(this), '_med', '_large');});
		
		hnMedQActive = true; //update this because it doesn't need to swap images when sizing down
	}
	
	
	
	//Portfolio images
	if (document.title == 'Portfolio | Maverick Cook' && width >= pfLarge && pfLargeQActive == false)
	{
		//update bools
		pfLargeQActive = true;
		var projectThumbs = $('.thumb img');

		projectThumbs.each(function(){replaceImgSrc($(this), '_med', '_large');});
	}
	

}

window.onresize = function(){replaceMobileImages(); resetToDeskNav();};

window.onload = function(){replaceMobileImages();};