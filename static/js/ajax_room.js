$(document).ready(function(){

 $('#grab').click(function(){
    var pref1;
var pref2;
var hostel;
var pref1_data;
var pref2_data;
hostel = $("#hostel").val();
        
pref1 = $("#pref1").val();
    pref2=$("#pref2").val();
 $.get('/search/', {search_hostel: hostel,search_room:pref1}, function(data){
			               pref1_data=data;
$.get('/search/', {search_hostel: hostel,search_room:pref2}, function(data){
               pref2_data=data;
 
$.get('/room/', {search_hostel: hostel,pref1:pref1,pref2:pref2,pref1_data:pref1_data,pref2_data:pref2_data}, function(data){
              				 $('#error').html(data);
					setTimeout(function() {
		           			if (str.indexOf("is alloted to you") >= 0)
  						{	 					
							location.reload(true);	
						}
					
					     }, 5000);						
           });   



});




 });
 


});
});

 
   				
               
         
            
