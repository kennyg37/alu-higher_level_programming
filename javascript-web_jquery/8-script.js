$(function() {
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        method: 'GET',
        success: function(response) {
            var movies = response.results;
            var movieList = $('ul#list_movies');
            $.each(movies, function(index, movie) {
                var listItem = $('<li>').text(movie.title);
                movieList.append(listItem);
            });
        },
    });
});