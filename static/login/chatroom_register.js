$(document).ready(function(){

	//注册
	$("#register").click(function(){
		var name = $("#inputName").val();
		var password1 = $("#inputPassword1").val();
		var password2 = $("#inputPassword2").val();
		/*$.post("goregister",{"name":name,"password1":password1,"password2":password2},
			function(data){
				if ( 0 != data.rtn )
					alert (data.errors);
				else { 
					window.location.href = "/chatroom/registersuc"; 
					//alert (data.username);
				}

			});*/
		$.ajax({
             type: "POST",
             url: "goregister",
             data: {"name":name,"password1":password1,"password2":password2},
             dataType: "json",
             async: false,
             success: function(data){
             			if ( 0 != data.rtn ){
							alert (data.errors);

             			}else{ 
							//window.location.href = "../registersuc"; 
							//alert (data.username);
							//document.location.href = "/chatroom/registersuc";
							//window.open( "registersuc");
							var html = "";
							html += "<div>";
							html += "<p>" + data.username + "</p>";
			    			html += "<p>恭喜！您已注册成功~</p>";
			    			html += "<a href='/chatroom/login'>立即登录</a>";
			    			html += "</div>";
							$("#registersuc").html(html);
						}

                    }
                    
                    	
                    
         });
		//window.open( "registersuc" ); 
        //window.location.reload( "registersuc" );
        return false;
	});
});