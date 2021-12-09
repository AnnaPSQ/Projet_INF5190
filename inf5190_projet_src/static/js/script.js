function get_installations() {
        
    var formData = new FormData(document.getElementById("formulaire"));
    var arrondissement = formData.get("arrondissement");
    fetch('/api/installations?arrondissement='+arrondissement)
    .then(function (response) {
        return response.text();
    }).then(function (text) {
        //console.log(json);
        var json = JSON.parse(text);
        //document.getElementById("name").innerHTML = json;
        if (json[0].length == 0) {
            document.getElementById("tableau").innerHTML = "Le nom saisi est invalide.";
        }
        else {
            var output = "<table class='table-sm table-bordered table-active'> ";
            output += "<tr><th>" + "id" + "</th>" + "<th>" + "installation" + "</th>"
                + "<th>" + "type" + "</th>" + "<th>" + "nom" +
                "</th>" + "<th>" + "nom_arrondissement" + "</th></tr>";
    
            for (var k = 0; k < json.length; k++) {
                for (var j = 0; j < json[k].length; j++) {
                    var obj = json[k][j];
                    //document.getElementById("test1").innerHTML = json[k][j]['nom'];
            
                    output += "<tr><td>" + obj["id"] + "</td>" + "<td>" + obj["installation"] 
                        + "</td>" + "<td>" + obj["type"] + "</td>" + "<td>" + obj["nom"]
                        + "</td>" + "<td>" + obj["nom_arrondissement"] + "</td></tr>";
                }   
            }
            output += "</table>";
            document.getElementById("tableau").innerHTML = output;
        }
    });
}