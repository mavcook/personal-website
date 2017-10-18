$('.expander').click(function(){
	toggleExpand($(this));
});

// Effects: hides or shows .collapase elements under a parent .collapseParent
function toggleExpand(el)
{
	var target = el.closest(".collapseParent").find('.collapse');
	var targetImgs = target.find("img");

	target.slideToggle("slow");
	targetImgs.slideToggle("slow");
	// switch chevron
	el.children(".expander-open").toggle();
	el.children(".expander-closed").toggle();

	// :( add padding to a closed section
	var par = el.parent().parent().parent();
	if (el.parent().hasClass('titleAndBar') && par.hasClass('section'))
		par.toggleClass('section-closed-padding');
}

