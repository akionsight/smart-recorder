$(document).ready(function() {
    $('#search-query').on('keypress', function (e) {
        if (e.which == 32) {
            console.log('space detected, aborting space');
            return false
        }
    })
})