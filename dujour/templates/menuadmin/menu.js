var map = L.map('map', {
  minZoom: 20,
  maxZoom: 23,
  center: [0, 0],
  zoom: 22,
  crs: L.CRS.Simple
});

// dimensions of the image
var w = {{ object.file.width }},
    h = {{ object.file.height }},
    url = '/{{ object.file }}';

// calculate the edges of the image, in coordinate space
var southWest = map.unproject([0, h], map.getMaxZoom()-1);
var northEast = map.unproject([w, 0], map.getMaxZoom()-1);
var bounds = new L.LatLngBounds(southWest, northEast);

// add the image overlay,
// so that it covers the entire map
L.imageOverlay(url, bounds).addTo(map);

// tell leaflet that the map is exactly as big as the image
map.setMaxBounds(bounds);

// add "select area" button to map
var locationFilter = new L.LocationFilter().addTo(map);

// bind create button action
$('#but-create').click(function() {
    var bounds = locationFilter.getBounds();
    $.ajax({
        url : "{% url 'menu_admin_create_item_and_region' %}",
        type : "POST",
        dataType: "json",
        data : {
            menu_id: {{ object.id }},
            menu_item_name: $('#menu_item_name').val(),
            menu_item_price: $('#menu_item_price').val(),
            ne_lat: bounds.getNorthEast().lat,
            ne_lng: bounds.getNorthEast().lng,
            sw_lat: bounds.getSouthWest().lat,
            sw_lng: bounds.getSouthWest().lng,
            csrfmiddlewaretoken: '{{ csrf_token }}',
            },
        success : function(json) {
            if (json['status'] === 'success')
            {
                $('#menu_item_name').val('');
                locationFilter.disable();
                L.rectangle([[bounds.getNorthEast().lat, bounds.getNorthEast().lng], [bounds.getSouthWest().lat, bounds.getSouthWest().lng]], {color: "#ff7800", weight: 1}).addTo(map);
            }
            else
            {
                alert('Error saving this region');
            }
        },
        error : function(xhr,errmsg,err) {
            alert('Error: ' + xhr.status + ': ' + xhr.responseText);
        }
    });
});

// bind update button action
$('#but-update').click(function() {
    var bounds = locationFilter.getBounds();
    $.ajax({
        url : "{% url 'menu_admin_update_item_and_region' %}",
        type : "POST",
        dataType: "json",
        data : {
            region_id: $('#menu_item_region_id').val(),
            menu_item_name: $('#menu_item_name').val(),
            menu_item_price: $('#menu_item_price').val(),
            ne_lat: bounds.getNorthEast().lat,
            ne_lng: bounds.getNorthEast().lng,
            sw_lat: bounds.getSouthWest().lat,
            sw_lng: bounds.getSouthWest().lng,
            csrfmiddlewaretoken: '{{ csrf_token }}',
            },
        success : function(json) {
            if (json['status'] === 'success')
            {
                location.reload();
            }
            else
            {
                alert('Error saving this region');
            }
        },
        error : function(xhr,errmsg,err) {
            alert('Error: ' + xhr.status + ': ' + xhr.responseText);
        }
    });
});

// bind delete button action
$('#but-delete').click(function() {
    $.ajax({
        url : "{% url 'menu_admin_delete_item_and_region' %}",
        type : "POST",
        dataType: "json",
        data : {
            region_id: $('#menu_item_region_id').val(),
            csrfmiddlewaretoken: '{{ csrf_token }}',
            },
        success : function(json) {
            if (json['status'] === 'success')
            {
                location.reload();
            }
            else
            {
                alert('Error saving this region');
            }
        },
        error : function(xhr,errmsg,err) {
            alert('Error: ' + xhr.status + ': ' + xhr.responseText);
        }
    });
})

function editRegion(region_id)
{
    $.get( "{% url 'menu_admin_load_region' %}", {'menu_item_region_id': region_id}, function(data) {
        // set form fields to existing values
        $('#menu_item_region_id').val(data['data']['region']['id']);
        $('#menu_item_name').val(data['data']['menu_item']['name']);
        $('#menu_item_price').val(data['data']['menu_item']['price']);
        $('#region_ne_lat').val(data['data']['region']['ne_lat']);
        $('#region_ne_lng').val(data['data']['region']['ne_lng']);
        $('#region_sw_lat').val(data['data']['region']['sw_lat']);
        $('#region_sw_lng').val(data['data']['region']['sw_lng']);

        // set map area select to existing region
        var southWest = L.latLng(data['data']['region']['sw_lat'], data['data']['region']['sw_lng']);
        var northEast = L.latLng(data['data']['region']['ne_lat'], data['data']['region']['ne_lng']);
        var existingBounds = L.latLngBounds(southWest, northEast);
        locationFilter.setBounds(existingBounds);
        locationFilter.enable();
    });
    $('#but-create').hide();
    $('#but-options').show()
    $('#but-update').show();
    $('#but-delete').show();
}

// draw existing regions
{% for region in region_list %}
L.rectangle([[{{ region.ne_lat }}, {{ region.ne_lng }}], [{{ region.sw_lat }}, {{ region.sw_lng }}]], {color: "#ff7800", weight: 1}).addTo(map).on('click', function(e) { editRegion({{region.id}}); });
{% endfor %}