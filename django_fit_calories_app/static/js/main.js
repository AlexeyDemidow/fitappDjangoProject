$(document).ready(function () {
    $('select').selectize({
        maxItems: 1,
        placeholder: 'Нажмите чтобы выбрать продукт ...',
    });
})


//$(document).ready(function() {
//    $('#number-plus').click(function(){
//        $.ajax({
//            url: 'user_calc/',
//            type: 'GET',
//            data: {
//
//            },
//            success: function(data){
//                $('#water_count').html(data);
//                },
//            error: function(){
//                alert('Error!');
//                }
//            });
//        });
//    });