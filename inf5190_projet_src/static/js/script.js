// Copyright 2017 Jacques Berger
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Lancée par l'action du bouton recherche de la recherche par nom d'arrondissement (home.html)
function get_installations() {
        
    var formData = new FormData(document.getElementById("formulaire"));
    var arrondissement = formData.get("arrondissement");
    fetch('/api/installations?arrondissement='+arrondissement)
    .then(function (response) {
        return response.text();
    }).then(function (text) {
        var json = JSON.parse(text);
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

// Lancée suite à la sélection du nom d'une installation (home.html)
function get_installation(nom) {
    fetch('/api/installation?nom='+nom)
    .then(function (response) {
        return response.text();
    }).then(function (text) {
        var json = JSON.parse(text);
        var output = "<table class='table-sm table-bordered table-active'> ";
        output += "<tr><th>" + "id" + "</th>" + "<th>" + "type" + "</th>"
                 + "<th>" + "nom" + "</th>" + "<th>" + "nom_arrondissement" + "</th></tr>";

        for (var k = 0; k < json.length; k++) {
            for (var j = 0; j < json[k].length; j++) {
                var obj = json[0][j];
        
                output += "<tr><td>" + obj["id"] + "</td>" + 
                          "<td>" + obj["type"] + "</td>"
                          + "<td>" + obj["nom"] + "</td>" + "<td>" 
                          + obj["nom_arrondissement"] + "</td></tr>";
            }   
        }
        output += "</table>";
        document.getElementById("tableau_nom").innerHTML = output;
    });
}