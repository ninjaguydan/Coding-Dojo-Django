// Form validation
$('#post-form').submit(function(){
    let firstName = $('#fname').val();
    let lasttName = $('#lname').val();
    let dob = $('#bdate').val();
    let email = $('#email').val();
    let password = $('#pw').val();
    let confirm = $('#confirm').val();

    if (firstName.length < 2) {
        return false;
    }
    if (lasttName.length < 2) {
        return false
    }
})