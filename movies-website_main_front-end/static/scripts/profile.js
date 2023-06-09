$('document').ready(function() {
    console.log("readys")
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