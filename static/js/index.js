$(document).ready(function() {
    $('form').submit(function (e) {
        e.preventDefault();
        var input_box_content = $('#search-query').val();
        console.log(input_box_content);
        var raw_transcript = $('#hidden-transcript').html();
        console.log(raw_transcript.search(input_box_content))
    }) 
});

// https://www.youtube.com/watch?v=wxxhuzjT9aM