$('document').ready(function () {
    console.log('Login page')
    $('input[type="button"]').click(function (event) {
        event.preventDefault();
        const email = $('input#email').val();
        const password = $('input#password').val();
        const error1 = $('#error')
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
                console.log("responding")
                console.log(response)
                localStorage.setItem('token', response.token);
                let token = localStorage.getItem('token')
                $.ajax({
                    type: "GET",
                    headers: {
                        "Authorization": token
                    },
                    url: 'http://localhost:5001/api/user/' + email,
                    success: function(response2){
                        console.log("success")
                        localStorage.setItem("User", JSON.stringify(response2))
                        window.location.href = '/dashboard'
                        
                    },
                    error: function(jqXHR, textStatus, errorThrown){
                        console.log("invalid token")
                        console.log(errorThrown)
                        if (jqXHR.status == 401){
                            error1.text('Incorrect Password')
                            console.log(errorThrown)
                        } else {
                            error1.text('Incorrect Email')
                            console.log(errorThrown)
                        }
                    }
            })

            },
            error: function(jqXHR, textStatus, errorThrown){
                if (jqXHR.status == 401){
                    error1.text('Incorrect Password')
                    console.log(errorThrown)
                } else {
                    error1.text('Incorrect Email')
                    console.log(errorThrown)
                }
            }
        })
        
    })
    $('#signup').click(function(event) {
        event.preventDefault();
        window.location.href = "/sign_up"
    })
})