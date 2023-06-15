$('document').ready(function() {
    console.log("Loaded")
    const currentUrl = window.location.href;
    // Extract the token from the URL
    const token = currentUrl.split('/').pop();
    console.log(token);
    //On clicking submit botton sends request to the backend
    $('input[type="button"]').click(function(event) {
        event.preventDefault()
        const password = $('#password').val()
        const password1 = $('#password1').val()
        console.log(password === password1)
        console.log(password)
        console.log(password1)
        const data = {
            "password": password
        }
        const url1 = `http://localhost:5001/api/user/reset_password/${token}`
        console.log(url1)
        $.ajax({
            type: "POST",
            url: `http://localhost:5001/api/user/reset_password/${token}`,
            contentType: "application/json",
            data: JSON.stringify(data),
            success: function(response) {
                console.log("sent")
                console.log(response)
                window.location.href = '/login'
            },
            error: function(error) {
                console.log(error)
            }
        })
    })
})