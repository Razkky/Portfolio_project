$('document').ready(function() {
    let actors_names = []
    let genre_names = []
    let actor_div = $('#actors_name')
    let genre_div = $('#genres_name')
    //add individual actor to list of actors
    $('.actors').click(function(event) {
        event.preventDefault();
        let actor = $('#actors')
        console.log(actor.val())
        actors_names.push(actor.val())
        let button = $("<button>").text(actor.val())
        actor_div.append(button)
        actor.val('')
    })

    //add individual genres to list of genres
    $('.genres').click(function(event) {
        event.preventDefault();
        let genre = $('#genres')
        console.log(genre.val())
        genre_names.push(genre.val())
        let button = $('<button>').text(genre.val())
        genre_div.append(button)
        genre.val('')
    })
    // submit user details to backend database
    $('#submit').click(function(event) {
        event.preventDefault();
        const data = JSON.parse(localStorage.getItem('Data'))
        console.log(data)
        const actors = $('#actors').val()
        const genres = $('#genres').val()
        console.log(actors)
        console.log(genres)
        $.ajax({
            type: "POST",
            data: JSON.stringify(data),
            url: "http://localhost:5001/api/users",
            contentType: "application/json",
            success: function (response){
                console.log(response)
                console.log("created User")
                const actor_obj = {
                    "name": actors,
                    "user_id": response.id
                }
                const genre_obj = {
                    "name": genres,
                    "user_id": response.id
                }
                console.log(response.id)
                $.ajax({
                    type: "POST",
                    data: JSON.stringify(actor_obj),
                    url: `http://localhost:5001/api/actor/${response.id}`,
                    contentType: "application/json",
                    success: function(response2) {
                        console.log("creating actor")
                        console.log(response2)
                        console.log("created actor")
                    },
                    error: function(error) {
                        console.log(error)
                    }

                })
                
                $.ajax({
                    type: "POST",
                    data: JSON.stringify(genre_obj),
                    url: `http://localhost:5001/api/genre/${response.id}`,
                    contentType: "application/json",
                    success: function(response2) {
                        console.log(response2)

                    }

                })
                window.location.href = '/login'
            }
        })
    })
})