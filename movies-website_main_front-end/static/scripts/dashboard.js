$('document').ready(function() {
    const section = document.getElementsByClassName('section_two')[0]
    const api_key = "c3c63420556c1043a8d6eac9948f427c";
    const base_url = `https://api.themoviedb.org/3`;
    const img_path = "https://image.tmdb.org/t/p/w500/"
    const logout = $('#btn2')
    const user_tag = $('#btn1')
    let user = JSON.parse(localStorage.getItem('User'))
    const username = user.username
    console.log(username)
    user_tag.html(username)
    const actors = []
    const genres = []
    user.actors.forEach(element => {
        actors.push(element.name)
    });
    user.genres.forEach(genre => {
        genres.push(genre.name)
    })
    console.log(actors)
    actors.forEach(actor => {
        const acotr_url = `${base_url}/search/person?api_key=${api_key}&query=${actor}`
        fetch(acotr_url).then((response) => response.json()).then((data) => {
            console.log(data)
            console.log(data.results[0])
            const actorId = data.results[0].id
            const acotr_movie = `${base_url}/discover/movie?api_key=${api_key}&with_cast=${actorId}`
            $.ajax({
                type: "GET",
                url: acotr_movie,
                success: function(response) {
                    showMovies(response.results)
                },
                error: function(jqXHR, textStatus, errorThrown){
                    console.log(errorThrown)
                }
            })
        })
    })
    genres.forEach(item => {
        const genre_url = `${base_url}/genre/movie/list?api_key=${api_key}`
        fetch(genre_url).then((response) => response.json()).then((data) => {
            const genres = data.genres
            const genre = genres.find(genre => genre.name === item)
            const genreId = genre.id
            const genre_movie = `${base_url}/discover/movie?api_key=${api_key}&with_genres=${genreId}`
            $.ajax({
                type: "GET",
                url: genre_movie,
                success: function(response) {
                    showMovies(response.results)
                },
                error: function(jqXHR, textStatus, errorThrown){
                    console.log(errorThrown)
                }
            })
        })
    })
    function showMovies(results) {
        results.forEach(element => {
            const {poster_path, title, overview, vote_average, id, release_date} = element;
            const vido_url = base_url + "/movie/" + id + "/videos?api_key=" + api_key
            let watch_video = ""
            videoLink(vido_url).then(key => {
                watch_video = key
                const youtube_link = "https://www.youtube.com/watch?v=" + watch_video
                const movieD = document.createElement('div');
                movieD.classList.add('movie')
                movieD.innerHTML = `
                    <img src="${img_path + poster_path}" class="movie_img"/>
                    <div class="movie_div">
                        <h1>${title}</h1>
                        <h1>${vote_average}%</h1>
                    </div>
                    <h3>Release Date: ${release_date}</h3>
                    <button class="movie_button"><a href=${youtube_link}>Watch</a></button>
                    <p class="ova_d">${overview}</p>
                `
                section.appendChild(movieD);
            });

        });
    }
    async function videoLink(videoUrl){
        const response = await fetch(videoUrl);
        const data = await response.json()
        return data.results[0].key
    } 
    $(logout).click(function(event) {
        event.preventDefault();
        localStorage.removeItem('token')
        window.location.href = '/'
    })

    $('.btn_container button[type="submit"]').click(function(event) {
        event.preventDefault();
        const search = $('.btn_container input[type="text"]').val();
        console.log(search)
        if (search){
            const url = base_url + '/search/movie?api_key=' + api_key + "&query=" + search
            $.ajax({
                type: "GET",
                url: url,
                success: function(response){
                    section.innerHTML = ""
                    showMovies(response.results)
                },
                error: function(jqXHR, textStatus, errorThrown){
                    console.log(errorThrown)
                }
            })
        } else {
            console.log("Nothing")
        }
    })
})