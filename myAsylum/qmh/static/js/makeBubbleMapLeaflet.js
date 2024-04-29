function makeBubbleMapLeaflet(obj) { //code adapted from https://d3-graph-gallery.com/graph/bubblemap_leaflet_basic.html
    /*obj should be an object with the following parameters:
        csv: the path to a .csv file
        places: the name of places in the file
        total: column corresponding the total for each place
        color: column of colors assigned to each location
        div: name of div to put map in
    the csv should also include columns for Longitude and Latitude
    
    For some reason, Leaflet only draws multiple maps if you use a  string for the div, 
    even though normally it would require the use of document.getElementById. 
    I don't really know why this is
    Using leaflet also requires the following in the html file:
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin=""/>
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
*/

    markerList = []; //I don't know why, but this needs to be here or the addMarkers function won't work
    d3.csv(obj.csv, function(err, rows) { //parse the data
        function unpack(rows, key) { //returns arrays based on column keys
            return rows.map(function(row) {return row[key];}); 
        }
        let size = [],
            places = unpack(rows, obj.places),
            total = unpack(rows, obj.total),
            lonList = unpack(rows, "Longitude"),
            latList = unpack(rows, "Latitude"),
            color = unpack(rows, obj.colors);
        
        for (let i = 0; i < places.length; i++) {
            size[i] = 2.5 * Math.sqrt(total[i]); //size of markers in pixels
        }

        let map = L //innitialize an empty map
            .map(obj.div, {
                maxBounds: [[-90, -260],[90, 260]], //prevents panning past these values
                maxBoundsViscosity: 1,  
            })
            .setView([39.9526,-75.1652], 2); //center on Philadelphia
        
        L.tileLayer(
            'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a>',
            maxZoom: 10,
            }).addTo(map);

        for (var i = 0; i < places.length; i++) { //add circular markers w/ popups for each location
            circle = L.circleMarker([latList[i], lonList[i]], { 
                color: color[i],
                fillColor: color[i],
                fillOpacity: 0.5,
                radius: (size[i]),
                alt: places[i] + ": " + total[i] + " patients",
            })
            .bindPopup(places[i] + ": " + total[i] + " patients", {autoClose: false})
            .addTo(map)
            markerList.push(circle)
            }
        
            let addText = false;
            window.addEventListener('keyup', function(e) {
                let key = e.key;
                if (key == 't') {
                    addText = !addText;
                    addMarkers(markerList, addText)
                }
            })
    })
}

function addMarkers(markerList, addText) { //open or close all the popups for map markers
    if (addText) {
        for (let i = 0; i < markerList.length; i++) {
            markerList[i].openPopup();
        }
        }
        else {
            for (let i = 0; i < markerList.length; i++) {
                markerList[i].closePopup();
            }
        }
}