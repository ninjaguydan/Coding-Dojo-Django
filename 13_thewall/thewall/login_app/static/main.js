// Form validation
// $('#post-form').submit(function(){
//     let firstName = $('#fname').val();
//     let lasttName = $('#lname').val();
//     let dob = $('#bdate').val();
//     let email = $('#email').val();
//     let password = $('#pw').val();
//     let confirm = $('#confirm').val();

//     if (firstName.length < 2) {
//         return false;
//     }
//     if (lasttName.length < 2) {
//         return false
//     }
// })
$('body').on('submit', '.comment-form', function(e){
    e.preventDefault();
    console.log("hello?");
    $.ajax({
        url: "wall/post_comment",
        method: "POST",
        data: $(this).serialize(),
        success: function(response){
            console.log(response);
            $('#whatever').html(response);
        }
    })
})

// $('.comment-form').submit(function(e){

// })