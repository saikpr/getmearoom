$(document).ready(function(){

 $('#accept').click(function(){
    var roll_no;
	var room_no;
	var room_data;
	var hostel;
hostel=$("#hostel").val();
    roll_no=$("#id").text();
	  $.get('/get_room/',function(data){
               room_no=data;
           
		 $.get('/search/', {search_hostel: hostel,search_room:room_no}, function(data){
			               room_data=data;

     				$.get('/accept_page/', {roll:roll_no,data_room:room_data}, function(data){
               				
						if(data==='1'){
							location.reload(true);							
								}           						
						else{
							$('#notify_error').html(data);
							$('#error_msg').show();
							$('#error_msg').delay(4000).fadeOut();
							location.reload(true);	
						}						
						});


				});

});
});

$('#reject').click(function(){
    var roll_no;
    roll_no=$("#id").text();
	
     $.get('/reject_page/', {roll:roll_no}, function(data){
               $('#search_result').html(data);
           });
});


});
