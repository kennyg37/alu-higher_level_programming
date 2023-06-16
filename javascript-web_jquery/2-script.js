$(function () {
    var realHeader = $('div#red_header');
    realHeader.on('click', function () {
        var header = $('header');
        header.css('color', '#FF0000');
    })
})