$('document').ready(function () {
    console.log('Login page')
    $('input[type="button"]').click(function (event) {
        event.preventDefault();
        const email = $('input#email').val();
        const password = $('input#password').val();
        console.log(email);
        console.log(password);
        data =  {
            "email": email,
            "password": password
        };
        console.log(data)
            
        $.ajax({
            type: "POST",
            data: JSON.stringify(data),
            url: "http://localhost:5001/api/login",
            contentType: "application/json",
            success: function (response){
                console.log(response)
                localStorage.setItem('token', response.token);
                console.log("storing token")
                let token = localStorage.getItem('token')
                console.log(token)
                $.ajax({
                    type: "GET",
                    headers: {
                        "Authorization": token
                    },
                    url: 'http://localhost:5001/api/user/' + email,
                    success: function(response2){
                        console.log('fetching user')
                        console.log(response2)
                        window.location.href = '/'
                        
                    }
                })

            }

        })

    })
    $('.login_box a').click(function(event) {
        event.preventDefault();
        window.location.href = "/sign_up"
    })
})