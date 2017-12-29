var showalert = function(title, messages, category, timeout) {
    var htmlEl = "<div class='alert alert-" + category + " alert-dismissible fade show' role='alert'>";
    htmlEl += "<button type='button' data-dismiss='modal' aria-label='Close' class='close'><span aria-hidden='true'>×</span></button>";
    htmlEl += "<h4 class='alert-heading'>" + title + "</h4>";
    htmlEl += "<p>" + messages + "</p>";
    htmlEl += "</div>";

    $("#myModal div").html(htmlEl);
    $("#myModal").modal('show');

    if(isNaN(timeout)) {
        setInterval(function(){
            $("#myModal").modal('hide');
        }, 10000);
    }else{
        setInterval(function(){
            $("#myModal").modal('hide');
        }, timeout);
    }
}