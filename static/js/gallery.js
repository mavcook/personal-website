var lastOpened = '';

// (function defer() {
//     if (window.jQuery) {
//         $(window).resize(function(){
//             $('#mediaWrap').height($('#imgView')[0].height + 'px')
//         });
		
//         $('#mediaWrap').click(function(){
//             var pdiv = $($(this).attr('data-parent'))
//             $(this).animate({height: '0px'});
//             $('html, body').animate({
//                 scrollTop: (pdiv.offset().top - 100)
//             },'slow');
//             lastOpened = '';
//         });
//     } else {
//         setTimeout(function() { defer() }, 50);
//     }
// })();


$(document).ready(function()
{

	$(window).resize(function(){
		$('#mediaWrap').height($('#imgView')[0].height + 'px')
	});
	
	$('#mediaWrap').click(function(){
		var pdiv = $($(this).attr('data-parent'))
		$(this).animate({height: '0px'});
		$('html, body').animate({scrollTop: (pdiv.offset().top - 100)});
		lastOpened = '';
	});

});


function toggleViewer(parent, imgsrc)
{
	var t = $('#mediaWrap');
	var parentDiv = $(parent);

	// close if image is visible
	t.animate({height: '0px'});

	// dont reopen same pic
	if (lastOpened === parent)
	{   
		$('html, body').animate({
			scrollTop: (parentDiv.offset().top - 100)
		});
		lastOpened = '';
		return;
	}
	lastOpened = parent;

	// else open
	var tImg = $('#imgView');
	var loadEvent = 'load', mediaType = 'pic';

	if (imgsrc.split('.').pop() === 'mp4')
	{
		tImg = $('#vidView');
		loadEvent = 'loadeddata';
		mediaType = 'video';
	}

	tImg.one(loadEvent, 
		function(){
			
			// new media src has finished loading
			t.attr('data-parent', parent);
			// put viewer below selected media
			t.css({top: parentDiv.position().top + parentDiv.height() + 'px'});
			
			var mediaHeight = tImg[0].height;
			if (mediaType === 'pic')
				$('#vidView').hide();
			else
			{
				mediaHeight = tImg.height();
				$('#imgView').hide();
			}
			tImg.show();

			$('html, body').animate({
				scrollTop: (t.offset().top - 100)
			},'slow');
			
			t.animate({height: mediaHeight + 'px'}, 'slow'); 
			
		}
	).attr('src', imgsrc);        
	
}