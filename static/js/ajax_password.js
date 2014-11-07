$(document).ready(function(){

 $('#recover').click(function(){
    var roll_no;
    roll_no=$("#roll").val();
	$('#progress').show();
     $.get('/pass_recovery/', {roll_number:roll_no}, function(data){
               $('#message').html(data);
		$('#progress').hide();
           });
});



});
