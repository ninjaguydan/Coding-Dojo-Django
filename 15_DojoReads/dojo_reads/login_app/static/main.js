$('#sortable').sortable(
    {revert:true}
);


//Display Star Rating
function displayRating(num){
    var result = "";
    for (var i = 1; i < 6; i++) {
        if (i <= num) {
            result = result + "&#x2605"
        } else {
            result = result  + "&#x2606";
            // result += "&#x2605";
        }
    }
    return result
}

// for (let x = 1; x < 6; X++) {
//     $(".n"+x).html(displayRating(x))
// }

$('.n1').html(displayRating(1));
$('.n2').html(displayRating(2));
$('.n3').html(displayRating(3));
$('.n4').html(displayRating(4));
$('.n5').html(displayRating(5));