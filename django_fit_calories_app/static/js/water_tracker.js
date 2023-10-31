//Использование POST запроса в AJAX и Django
function getCookie(name){
    var cookieValue = null;
    if(document.cookie && document.cookie != '' ){
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++){
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name wewant?
            if ( cookie.substring(0, name.length + 1 ) == (name + '=') ){
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method){
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings){
        if (!csrfSafeMethod(settings.type) && !this.crossDomain){
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

//////////////////////////////////////////////////////////////////////////////////

//Добавить стакан
$(function() {
    $('#water-tracker-plus').click(function(event) {
        const new_water = parseInt($('#water-tracker-actual').html()) + 1
        console.log(new_water)
        event.preventDefault();
        $.ajax({
            url: '',
            type: 'POST',
            data: $(this).serialize(),
            success: function(response) {
                $('#water-tracker-actual').html(new_water)
                }
        });
    });
});

//Убавить стакан
$(function() {
    $('#water-tracker-minus').click(function(event) {
        let new_water = parseInt($('#water-tracker-actual').html()) - 1
        if (new_water < 0) {
            new_water = 0
        }
        console.log(new_water)
        event.preventDefault();
        $.ajax({
            url: '',
            type: 'POST',
            data: $(this).serialize(),
            success: function(response) {
                $('#water-tracker-actual').html(new_water)
                }
        });
    });
});


// $(function() {
//     setInterval(function() {
//         $.ajax({
//             url: '',
//             type: 'POST',
//             data: $(this).serialize(),
//             success: function(response) {
//                 $('#water-tracker-actual').html(response.water);
//             }
//         });
//     }, 2000);
// });
