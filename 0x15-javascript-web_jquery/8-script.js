// a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
const url = 'https://swapi.co/api/films/?format=json';
$.get(url, function (data) {
  const films = data.results;
  for (const film of films) {
    $('ul#list_movies').append(`<li>${film.title}</li>`);
  }
});
