$('#sortable').sortable(
    {revert:true}
);


var rating = $('span').attr('rating');
console.log(rating);
var result = "";
for (var i = 1; i < 6; i++) {
    if (i <= rating) {
        result = result + "&#x2605"
    } else {
        result = result  + "&#x2606";
        // result += "&#x2605";
    }
}
$('span').html(result);