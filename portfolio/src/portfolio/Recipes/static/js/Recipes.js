$(window).on('load', function() {
	$("body").removeClass('fade-out')
});

$("#delete-recipe-button").on('click', function(){
    return confirm('Are you sure you want to delete this recipe?')
})
