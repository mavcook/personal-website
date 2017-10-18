var nav = document.getElementById('navBarDiv');
var lArrow = document.getElementById('leftArrow');
var rArrow = document.getElementById('rightArrow');
var btn = document.getElementById('btn');

function hFadeOut(e) 
{
	//add
	nav.classList.add('fadeOut');
	lArrow.classList.add('fadeOut');
	rArrow.classList.add('fadeOut');
	btn.classList.add('fadeOut');
	
	//remove
	nav.classList.remove('fadeIn');
	lArrow.classList.remove('fadeIn');
	rArrow.classList.remove('fadeIn');
	btn.classList.remove('fadeIn');
}
function hFadeIn(e)
{
	//add
	nav.classList.remove('fadeOut');
	lArrow.classList.remove('fadeOut');
	rArrow.classList.remove('fadeOut');
	btn.classList.remove('fadeOut');
	
	//remove
	nav.classList.add('fadeIn');
	lArrow.classList.add('fadeIn');
	rArrow.classList.add('fadeIn');
	btn.classList.add('fadeIn');
}



carousel = (function(){
  var box = document.querySelector('.mCarousel');
  var next = document.getElementById('rightArrow');
  var prev = document.getElementById('leftArrow');
  var cElements = box.querySelectorAll('.cElement');
  var counter = 0;
  var numElements = cElements.length;
  var currentElement = cElements[0];

  function navigate(direction) {
    currentElement.classList.remove('current');
	if (currentElement.children[0].tagName == 'VIDEO')
	{
		//pause video and fadeback when changing element
		currentElement.children[0].pause();
		hFadeIn();
		
		currentElement.children[0].removeEventListener('play',hFadeOut,false);
		currentElement.children[0].removeEventListener('ended',hFadeIn,false);
		currentElement.children[0].removeEventListener('pause',hFadeIn,false);
	}
		 
    counter = counter + direction;
    if (direction === -1 && 
        counter < 0) { 
      counter = numElements - 1; 
    }
    if (direction === 1 && 
        !cElements[counter]) { 
      counter = 0;
    }
    currentElement = cElements[counter];
    currentElement.classList.add('current');
	if (currentElement.children[0].tagName == 'VIDEO')
	{
		currentElement.children[0].addEventListener('play',hFadeOut,false);
		currentElement.children[0].addEventListener('ended',hFadeIn,false);
		currentElement.children[0].addEventListener('pause',hFadeIn,false);
	}
  }
  next.addEventListener('click', function(e) {
    navigate(1);
  });
  prev.addEventListener('click', function(e) {
    navigate(-1);
  });
  navigate(0);
})();


