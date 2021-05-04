$('.container').on('submit', '#registration', function(e){
    e.preventDefault();
    $.ajax({
        url: "/register",
        method: "POST",
        data: $(this).serialize(),
        success: function(){
            if ($('.pw').val() !== $('.confirm').val()) {
                $('#confirm-pw-input p').show(100);
            } else {
                $('#confirm-pw-input p').hide(100);
            }
        }
    })
})