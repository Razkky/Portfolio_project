$('document').ready(function() {
    let actors_names = []
    let genre_names = []
    let actor_div = $('#actors_name')
    let genre_div = $('#genres_name')
    //add individual actor to list of actors
    $('button').click(function(event) {
        event.preventDefault()
    })
    $('.actors').click(function(event) {
        event.preventDefault();
        let actor = $('#actors')
        actors_names.push(actor.val())
        let button = $("<button>").text(actor.val())
        actor_div.append(button)
        actor.val('')
    })

    //add individual genres to list of genres
    $('.genres').click(function(event) {
        event.preventDefault();
        let genre = $('#genres')
        genre_names.push(genre.val())
        let button = $('<button>').text(genre.val())
        genre_div.append(button)
        genre.val('')
    })
    // submit user details to backend database
    $('#submit').click(function(event) {
        event.preventDefault();
        const data = JSON.parse(localStorage.getItem('Data'))
        $.ajax({
            type: "POST",
            data: JSON.stringify(data),
            url: "http://localhost:5001/api/users",
            contentType: "application/json",
            success: function (response){
                async function sendActorRequests(response) {
                    for (let element of actors_names) {
                        const actor_obj = {
                        "name": element,
                        "user_id": response.id
                        };

                        try {
                        await $.ajax({
                            type: "POST",
                            data: JSON.stringify(actor_obj),
                            url: `http://localhost:5001/api/actor/${response.id}`,
                            contentType: "application/json"
                        });

                        console.log("creating actor");
                        console.log(element);
                        console.log("created actor");
                        } catch (error) {
                        console.log("encountered error");
                        console.log(error);
                        }
                    }
                    }

                (async function() {
                try {
                    await sendActorRequests(response);

                    for (let element of genre_names) {
                        const genre_obj = {
                            "name": element,
                            "user_id": response.id
                        };

                        try {
                            await $.ajax({
                            type: "POST",
                            data: JSON.stringify(genre_obj),
                            url: `http://localhost:5001/api/genre/${response.id}`,
                            contentType: "application/json"
                            });

                            console.log(element);
                            console.log("created genre");
                        } catch (error) {
                            console.log(error);
                        }
                        }
                    window.location.href = "/login"
                } catch (error) {
                    console.log(error);
                }
                })();

            }
                })
            })
        })