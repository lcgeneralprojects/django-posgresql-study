function dummy() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementsByTagName("main").innerHTML = this.responseText;
        }
    };
    xhttp.open("POST", "home", true);
    xhttp.send();
}