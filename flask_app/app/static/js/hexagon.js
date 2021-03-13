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
    // map.setCenter(position);
}
