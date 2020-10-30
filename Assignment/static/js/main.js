 document.getElementById("hiderBtn").addEventListener("click", function(){ 
 $("#smallNav").toggle();
 });

/* Overlay JS 
Create an overlay when the user clicks on an image and display the image on the overlay
*/

var $overlay = $('<div id="overlay"></div>'); // create a div
var $img = $("<img>"); // create an image to go on the div
var $caption = $('<p></p>'); // create a caption to go beneath picture
var $button = $('<button id="closeGallery">X</button>'); // create a button to close current image

$overlay.append($img); // add the image to the overlay

$overlay.append($caption); // add the caption to the overlay

$overlay.append($button); // add the caption to the overlay

$('#htlImgs').append($overlay);

// Add an event listener for when a user clicks an image in our gallery

$('#gallery a').click(function(event) {
    event.preventDefault(); // prevent the default action assosciated with <a> tag of following the url
    var Src = $(this).attr('href'); // get the src of the image that the user clicked on and store in Src
    console.log(Src);
    $img.attr('src', Src); // update the image we created on the overlay to have the Src of the image that the user clicked
    $overlay.show(); // display the overlay
    
    var caption = $(this).children('img').attr('alt'); 
    $caption.text(caption); // set the caption we created earlier  to have the text of the alt tag of the img clicked
    
});

$button.click(function(){
    $overlay.hide();
    
    
})

$overlay.click(function(){
    $overlay.hide();
    
    
})

