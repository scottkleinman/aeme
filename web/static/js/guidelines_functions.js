function loadContent(href) {
    $("#loading").show();
    var fetch_url = site_url+"/get-markdown";
    $.ajax({
        url: fetch_url,
        type: 'POST',
        contentType: "application/x-www-form-urlencoded; charset=UTF-8",
        data: href,
        cache: false,
        dataType: "text",
        complete: function(response) {
            $(window).scrollTop(0);
            $("article").html(response.responseText);
                $('pre code').each(function(i, block) {
                    hljs.highlightBlock(block);
                });
                $('code').each(function(i, block) {
                    hljs.highlightBlock(block);
                });
            $("#loading").hide();
        }
    });
}

// Perform on document.ready()
$(function () {
    // Handle links on the content article
    $('article').on('click', 'a', function(e){
        e.preventDefault();
        if ($(this).prop("target")) {
            window.open($(this).attr("href"),'_blank');
        }
        else {
            // Clear search parameters from the browser address bar
            window.history.pushState(null, null, window.location.pathname);
            loadContent($(this).attr("href"));
        }
    });
    // Handle links in the navigation menu
    $('.nav-list li a').click(function(e){
        e.preventDefault();
        // Clear search parameters from the browser address bar
        window.history.pushState(null, null, window.location.pathname);
        href = $(this).attr("href");
        // Menu item is a dropdown heading
        if ($(this).hasClass("folder")) {
            $(this).parent().siblings().find('ul').slideUp();
            $(this).next().slideToggle();            
        }
        // If there is a link, load the content by ajax
        if (href != "#") {
            loadContent(href);
        }
    });

    // Handle search form button
    $('#searchbtn').click(function(){
        $('#searchform').submit();
    });

    // Bootstrap Table Class
    $('table').addClass('table');

    // Responsive menu spinner
    $('#menu-spinner-button').click(function () {
        $('#sub-nav-collapse').slideToggle();
    });

    // Catch browser resize
    $(window).resize(function () {
        // Remove transition inline style on large screens
        if ($(window).width() >= 768)
            $('#sub-nav-collapse').removeAttr('style');
    });
});

//Fix GitHub Ribbon overlapping Scrollbar
var t = $('#github-ribbon');
var a = $('article');
if (t[0] && a[0] && a[0].scrollHeight > $('.right-column').height()) t[0].style.right = '16px';

//Toggle Code Block Visibility
function toggleCodeBlocks() {
    var t = localStorage.getItem("toggleCodeStats")
    t = (t + 1) % 3;
    localStorage.setItem("toggleCodeStats", t);
    var a = $('.content-page article');
    var c = a.children().filter('pre');
    var d = $('.right-column');
    if (d.hasClass('float-view')) {
        d.removeClass('float-view');
        $('#toggleCodeBlockBtn')[0].innerHTML = "Hide Code Blocks";
    } else {
        if (c.hasClass('hidden')) {
            d.addClass('float-view');
            c.removeClass('hidden');
            $('#toggleCodeBlockBtn')[0].innerHTML = "Show Code Blocks Inline";
        } else {
            c.addClass('hidden');
            $('#toggleCodeBlockBtn')[0].innerHTML = "Show Code Blocks";
        }
    }
}

if (localStorage.getItem("toggleCodeStats") >= 0) {
    var t = localStorage.getItem("toggleCodeStats");
    if (t == 1) {
        toggleCodeBlocks();
        localStorage.setItem("toggleCodeStats", 1);
    }
    if (t == 2) {
        toggleCodeBlocks();
        toggleCodeBlocks();
        localStorage.setItem("toggleCodeStats", 2);
    }
} else {
    localStorage.setItem("toggleCodeStats", 0);
}
