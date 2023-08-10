$(document).ready(function() {
    $('#search').on('input', function() {
        const searchValue = $(this).val().toLowerCase();
        $.ajax({
            url: '/search/',
            data: {search: searchValue},
            success: function(data) {
                $('#id_fooditem').html(data);
            }
        });
    });
});