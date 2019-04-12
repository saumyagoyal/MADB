$(function() {
        $('#btnSignUp').click(function() {
            console.log("This is hopefully working!")
            $.ajax({
                url: '/',
                data: $('form').serialize(),
                type: 'POST',
                success: function(response) {
                    window.alert(response);
                    $("form").trigger("reset");
                },
                error: function(error) {
                    console.log(error);
                    window.location.replace = "/";
                }
            });
        });
    });