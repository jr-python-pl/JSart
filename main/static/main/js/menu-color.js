// Change Color Navbar Elements on Scroll

$(window).scroll(function () {
    if ($(this).scrollTop() > 350) {
        $('.icon-bar').addClass('opaque');
        $('.navbar-brand img').attr('src', '/static/main/img/logo-light.png');
        $('.navbar-brand img').addClass('small');
    } else {
        $('.icon-bar').removeClass('opaque');
        $('.navbar-brand img').attr('src', '/static/main/img/logo.png');
        $('.navbar-brand img').removeClass('small');
    }
});



$(function () {
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('#topbar, .cart-label').fadeOut('slow');
            $('.logo img')
                .attr('src', '/static/main/img/logo.png');
        }
        if ($(this).scrollTop() < 100) {
            $('#logo, #topbar, .cart-label').fadeIn('fast');
            $('.logo img')
                .attr('src', '/static/main/img/logo-light.png');
        }
    });
});
