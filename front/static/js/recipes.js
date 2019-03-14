$.views.settings.delimiters("<%", "%>");
var elements = document.querySelectorAll(".ingredient");
for (i = 0; i < elements.length; i++) {
    elements[i].onclick = function(event) {
        var filters = "";
        var checkboxes = document.querySelectorAll(".ingredient:checked");

        for (j = 0; j < checkboxes.length; j++) {
            filters += checkboxes[j].getAttribute("value");
            if (j !== checkboxes.length-1) {
                filters += ",";
            }
        }
        $.get( "/recipes/?ingredients=" + filters, function( data ) {
            var tmpl = $.templates("#recipeTemplate");
            $("#recipesContainer").html(tmpl.render(data));
        });
    }
}