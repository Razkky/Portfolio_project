$('document').ready(function() {
    console.log('loaded')
    const notice = $('#notice')
    $('input[type="button"]').click(function(event) {
        event.preventDefault();
        const email = $('input#email').val();
        const data = {
            "email": email
        };
        $.ajax({
            type: "POST",
            data: JSON.stringify(data),
            url: 'http://localhost:5001/api/user/reset_password',
            contentType: "application/json",
            success: function(response) {
                console.log(response)
                notice.text("A Reset Password Mail has been sent to your mail")
            },
            error: function(jqXHR, textStatus, errorThrown){
                console.log(errorThrown)
            }
        })
    })
})