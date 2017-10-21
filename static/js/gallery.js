var lastOpened = '';
var vidView;
var imgView;
var mediaWrap;
var htmlBody;



$(document).ready(function()
{
	vidView = $('#vidView');
	imgView = $('#imgView');
	mediaWrap = $('#mediaWrap');
	htmlBody = $('html, body');

	$(window).resize(function(){
		mediaWrap.height(imgView[0].height + 'px')
	});
	
	mediaWrap.click(function(){
		var pdiv = $($(this).attr('data-parent'))
		$(this).animate({height: '0px'});
		htmlBody.animate({scrollTop: (pdiv.offset().top - 100)});
		lastOpened = '';
	});

});




function toggleViewer(parent, imgsrc)
{
	var t = mediaWrap;
	var parentDiv = $(parent);

	var scroller = function(){
		htmlBody.animate({
			scrollTop: (parentDiv.offset().top - 100)
		});
	};
	

	// close if image is visible
	t.animate({height: '0px'});

	// dont reopen same pic
	if (lastOpened === parent)
	{   
		scroller();
		lastOpened = '';
		return;
	}
	lastOpened = parent;

	// else open
	var tView = imgView;
	var loadEvent = 'load', mediaType = 'pic';

	if (imgsrc.split('.').pop() === 'mp4')
	{
		tView = vidView;
		loadEvent = 'loadeddata';
		mediaType = 'video';
	}

	tView.one(loadEvent, 
		function(){
			
			// new media src has finished loading
			t.attr('data-parent', parent);
			// put viewer below selected media
			t.css({top: parentDiv.position().top + parentDiv.height() + 'px'});
			
			var mediaHeight = tView[0].height;
			if (mediaType === 'pic')
				vidView.hide();
			else
			{
				mediaHeight = tView.height();
				imgView.hide();
			}
			tView.show();

			scroller();

			t.animate({height: mediaHeight + 'px'}); 
			
		}
	).attr('src', imgsrc);        
	
}