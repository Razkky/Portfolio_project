$('document').ready(function() {
    $('input[type="button"]').click(function(event) {
        const name = $('input#name').val()
        const email = $('input#email').val()
        const username = $('input#username').val()
        const password = $('input#password').val()
        const password1 = $('input#password1').val()
        const error = $('#error')
        if (password === password1) {
            data =  {
                "name": name,
                "username": username,
                "email": email,
                "password": password
            };
                
            localStorage.setItem("Data", JSON.stringify(data))
            window.location.href = '/profile'
        } else {
            console.log("unmatced password")
            error.text('unmatched password')
        }
    })
    $('#login').click(function(event) {
        event.preventDefault();
        window.location.href = '/login'
    })
})