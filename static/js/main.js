/* MAIN JS */

angular.module('steelCityReddUp', ['ui'])


/*
	Maps
*/
function MapController($scope) {
	$scope.markers = [];

	$scope.mapOptions = {
		center: new google.maps.LatLng(40.4406, -79.9961),
		zoom: 12,
		mapTypeId: google.maps.MapTypeId.ROADMAP
	}

	$scope.fetchPoints = function() {
		$scope.clearMarkers();
		$.getJSON(
			"url",
			function (data) {
				$.each(data.items, function(item){

				});
			}
		);
	}

	$scope.addMarker = function($event) {
		$scope.markers.push(new google.maps.Marker({
			map: $scope.map,
			position: $event.latLng
		}));
	}

	$scope.clearMarkers = function () {
		$.each($scope.markers, function(marker){
			marker.setMap(null);
		});
	}

	$scope.openInfoWindow = function(marker) {

	}
}