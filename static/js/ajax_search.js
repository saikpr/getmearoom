$(document).ready(function(){

 $('#search').click(function(){
    var hostel;
var room;
    hostel = $("#hostel").val();
    room=$("#search_room").val();
     $.get('/search/', {search_hostel: hostel,search_room:room}, function(data){
		          
		$('#search_result').html(data);
               
           });
});
});
