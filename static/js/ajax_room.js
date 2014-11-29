$(document).ready(function(){

 $("#available").change(function() {
        var room_get = $(this).val();
    var pref1;

var hostel;
var pref1_data;

hostel = $("#hostel").val();
        
//pref1 = $("#pref1").val();
    
 $.get('/search/', {search_hostel: hostel,search_room:room_get}, function(data){
			               pref1_data=data;

 
$.get('/room/', {search_hostel: hostel,pref1:room_get,pref1_data:pref1_data}, function(data){
              				$('#error_room').show();
              				 $('#error').html(data);
					
		           			if (data.indexOf("is alloted to you") >= 0)
  						{	 					
							location.reload(true);	
						}
					
					    				
           });   








 });
 


});
});

 
   				
               
         
            
