$(document).ready(function () {
    $('form').submit(function (e) {
        e.preventDefault();
        var search_query = $('#search-query').val();
        var searched = search_query
        var text = document.getElementById("transcript");
        var instance = new Mark(text);
        instance.unmark();
        instance.mark(searched, {
            "accurary": "excatly",
            "synonyms": {
                "one": "1",
                "two": "2",
                "three": "3",
                "four": "4",
                "five": "5",
                "six": "6",
                "seven": "7",
                "eight": "8",
                "nine": "9",
                "ten": "10"
            },
            "done": function (count) {
                $("#instances-found")
                console.log(count);
            },
            "noMatch": function (not_found) {
                console.log('nothing of that sort found');
                console.log(not_found);
            }
        });
    });
});
// https://www.youtube.com/watch?v=wxxhuzjT9aM