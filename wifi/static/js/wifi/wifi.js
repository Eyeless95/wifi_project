$(document).ready(function () {
    var interval = setInterval(update_countdown, 1000);

    function update_countdown() {
        var current = parseInt($('#countdown_seconds').text());
        if (current <= 1) {
            clearInterval(interval);
            $('.timer_div').html('Redirecting...');
            redirect_to_thanks_page()
        }
        $('#countdown_seconds').text(current - 1);
    }

    function redirect_to_thanks_page() {
        var csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            type: 'POST',
            url: links.callback,
            data: {
                csrfmiddlewaretoken: csrfmiddlewaretoken
            },
            dataType: 'json',
            success: function (data) {
                if (data['status']) {
                    window.location.href = 'http://10.5.50.1/success_login.html'
                }
            }
        })
    }
});