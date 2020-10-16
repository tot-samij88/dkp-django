function myMap() {
    var mapOptions = {
        center: new google.maps.LatLng(58.01741, 56.28552),
        zoom: 10,
        mapTypeId: google.maps.MapTypeId.HYBRID
    }
    var map = new google.maps.Map(document.getElementById("map"), mapOptions);
}