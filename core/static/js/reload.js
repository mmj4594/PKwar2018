setInterval(function(){
    $.ajax({url: "/reload_match", success: function(result_html){
        $("#scoreboard").html(result_html);
    }});
}, 10000);