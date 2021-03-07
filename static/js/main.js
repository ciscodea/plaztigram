// Show Comments
$(function() {
    // Always show last 3 comments:
    $(".comment-box").each(function(index) {
        $(this).children(".user-comment-box").slice(-3).show();
    });

    $(".see-more").click(function(e) { // click event for load more
        e.preventDefault();
        var link = $(this);
        $(this).siblings(".user-comment-box:hidden").show(1, function() {
            if ($(this).is(':visible')) {
                link.text('Show less comments');
                $(this).addClass('showing-more')
            }
        });

        if ($('div').hasClass('showing-more')) {
            link.text('Show all comments');
            $('.showing-more').hide(1);
            $('div').removeClass("showing-more");
        }
    });
});
