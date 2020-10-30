$(document).ready(function() {
    $('form').submit(function (e) {
        e.preventDefault();
        places_where_the_word_is_present = window.places_where_the_word_is_present
        transcript = $('#raw-transcript').text();
        var split_words_raw = transcript.split(' ');
        var split_words = split_words_raw.split(',');

        


    }) 
});

// https://www.youtube.com/watch?v=wxxhuzjT9aM