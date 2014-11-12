 $(document).ready(function(){

var ajax_call = function() {
  //your jQuery ajax code
var room=[];
var roll_no;
 //roll_no=$("#id").text();
    var hostel;
    hostel = $("#hostel").val();
   
     $.get('/available/', {search_hostel: hostel}, function(data){
		//var hello = JSON.parse(data); // this will convert your json string to a javascript object
var json=$.parseJSON(data);
//$('#error').html(json.length);
//
for (x in json){
$("#"+String(json[x].room_no)).html(String(json[x].room_no)+" Sorry!,Its Gone!");
$("#"+String(json[x].room_no)).css('color', 'red');

}
/*$.json.each(function(index, element) {
    $('#error').html(element.room_no);

});*/
				
    							
//$('#error').html(json['room_no']);
			/*for(var i = 0, size = json.length; i < size ; i++){
   					var item = json[i];
   					for (var key in item) {
    							$('#error').html(item)
    // Use `key` and `value`
									}	
				}        
			/*for(var i=1;i<total_room;i++)
				{
				if(room[i]!=1)
					{
					$('<option>').val(i).text('Available').appendTo('#available');				
					}

			
				}	*/	


           });
};

var interval = 4000; // where X is your every X minutes

setInterval(ajax_call, interval);

});
