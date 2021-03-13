//ur mum gone
function drawHexagon(map,position,radius){
    var coordinates = [];
    for(var angle= -90;angle < 270; angle+=60) {
       coordinates.push(google.maps.geometry.spherical.computeOffset(position, radius, angle));
    }

    console.log(coordinates);

    // Construct the polygon.
    var polygon = new google.maps.Polygon({
        paths: coordinates,
        strokeColor: '#FF0000',
        strokeOpacity: 0.8,
        strokeWeight: 2,
        fillColor: '#FF0000',
        fillOpacity: 0.35
    });
    polygon.setMap(map);
}

function drawHexagon1(map,position,radius){
    let br = radius / Math.sqrt(3)
    for (var i = 0; i < 3; i++) {
        position = google.maps.geometry.spherical.computeOffset(position, radius, 0);
        for (var j = 1; j <= 6; j++) {
            for (var k = 1; k <= i+1; k++) {
                drawHexagon(gmap, position, br);
                position = google.maps.geometry.spherical.computeOffset(position, radius, -60+(-60*j));
            }
        }
    }
}
