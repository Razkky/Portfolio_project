$('document').ready(function () {
    const api_key = "c3c63420556c1043a8d6eac9948f427c";
    const base_url = "https://api.themoviedb.org/3";
    const img_path = "https://image.tmdb.org/t/p/w500/"
    const movies_url = base_url + '/movie/popular?api_key=' + api_key; 
    const section = document.getElementsByClassName('section_two')[0]

    // get list of movies from TDMB
    function getMovies(url) {
        $.ajax({
            type: "GET",
            url: url,
            success: function(data) {
                showMovies(data.results)
            }
        })
    }

    // Display all movies to the user
    function showMovies(results) {
        section.innerHTML = "";
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
    //Search for a movie
    $('.btn_container button[type="submit"]').click(function() {
        console.log('clicked')
        const search = $('.btn_container input[type="text"]').val();
        if (search){
            const url = base_url + '/search/movie?api_key=' + api_key + "&query=" + search
            $.ajax({
                type: "GET",
                url: url,
                success: function(response){
                    showMovies(response.results)
                }
            })
            console.log(url)
        } else {
            console.log("Nothing")
        }
    })
    //get link to video
    async function videoLink(videoUrl){
        const response = await fetch(videoUrl);
        const data = await response.json()
        return data.results[0].key
    } 
    const btn1 = document.getElementById('btn1')
    btn1.addEventListener('click', function() {
        window.location.href = '/login'
        console.log('click')})

    
    getMovies(movies_url);
})
