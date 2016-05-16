$(document).ready(function() {
    activateShowcase();
});

function activateShowcase() {
    $items = $('.showcase li');
    if ($items.length > 0) {
        $items.removeClass('active');
        activateShowcaseItem($items[0]);
    }

    // Initialize hover functionality
    $items.hover(function(){
        $this = $(this);
        if (!($this.hasClass('active'))) {
            activateShowcaseItem($this[0]);
        }
    });

    // Initialize autorun functionality
    window.setInterval(function(){
        toNextShowcaseItem();
    }, 30000);


}

function activateShowcaseItem(item) {
    // Clean the previous link
    $('.sc-img').children().remove();
    $('.showcase li').removeClass('active');
    // Add new image to placeholder
    $(item).addClass('active');
    var url = $(item).data('url');
    var imageUrl = $(item).data('img');
    $anchor = $('<a href="'+ url +'"></a>');
    $image = $('<img src="'+ imageUrl +'" />');
    $anchor.append($image);
    $('.sc-img').append($anchor);
}

function toNextShowcaseItem() {
    var currentIndex, totalItems, nextIndex, nextItem;

    currentIndex = $('.sc-content li.active').data('index');
    totalItems = $('.sc-content li').length;
    if (currentIndex === totalItems) {
        nextIndex = 1;
    } else {
        nextIndex = currentIndex + 1;
    }
    nextItem = $('.sc-content li[data-index='+ nextIndex +']');
    activateShowcaseItem(nextItem);
}
