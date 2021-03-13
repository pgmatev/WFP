//ur mum gone
function drawHexagon(map, position, radius, fire_coef){
    var coordinates = [];
    for(var angle= -90;angle < 270; angle+=60) {
       coordinates.push(google.maps.geometry.spherical.computeOffset(position, radius, angle));
    }

    console.log(coordinates);

    let color = '#00FF00'
    if(fire_coef > 0.5 && fire_coef < 0.75){
        color = '#FFFF00'
    }
    if(fire_coef >= 0.75){
        color = '#FF0000'
    }
    console.log(color);
    // Construct the polygon.
    var polygon = new google.maps.Polygon({
        paths: coordinates,
        strokeColor: color,
        strokeOpacity: 0.8,
        strokeWeight: 2,
        fillColor: color,
        fillOpacity: 0.35
    });
    polygon.setMap(map);
}

async function drawOuterHexagon(map, position, radius){
    let danger = 0;
    function postInfo(latLng) {
        return $.ajax({
            type: "POST",
            url: 'info',
            contentType: "application/json; charset=UTF-8",
            dataType: 'json',
            data: JSON.stringify({'latitude': latLng.lat(), 'longitude': latLng.lng()}),
            success: function (data) {
                console.log(data);
                fire_coef = data.fire_coef;
                if(fire_coef > 0.5){
                    danger++;
                }
            },
        });
    }
    let br = radius / Math.sqrt(3);
    var i = 0;

    while (true) {
        position = google.maps.geometry.spherical.computeOffset(position, radius, 0);
        for (var j = 1; j <= 6; j++) {
            for (var k = 1; k <= i+1; k++) {
                await postInfo(position);
                drawHexagon(gmap, position, br, fire_coef);
                position = google.maps.geometry.spherical.computeOffset(position, radius, -60+(-60*j));
            }
        }
        i++;
        if(danger === 0){
            break;
        }
        danger = 0;
    }
}
