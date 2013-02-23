/* MAIN JS */

/*
	UI Modes:
		1. default
		2. identify
		3. details
		4. claim
		5. solve
*/

angular.module('steelCityReddUp', ['ui'])

/*
	Maps
*/
function Controller($scope) {
	$scope.mode = 'default';
	$scope.markers = [];

	$scope.mapOptions = {
		center: new google.maps.LatLng(40.4406, -79.9961),
		zoom: 12,
		mapTypeId: google.maps.MapTypeId.ROADMAP
	}

	$scope.fetchPoints = function() {
		$scope.clearMarkers();
		$('#spinner').spin();
		$.getJSON(
			"url",
			function (data) {
				$('#spinner').stop();
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
}

var samplePoint = {
	id 				: 1,
	description 	: "Found some graffiti on the side of an 
					   office building on Penn Ave",
	latLng 			: new LatLng(40.462013, 79.926331),
	beforeImg 		: "before.jpg",
	afterImg 		: "afterImg",
	dateOpened		: new Date("Sat Feb 23 2013 11:48:20 GMT-0500 (EST)"),
	dateClosed		: new Date("Sun Feb 24 2013 12:48:20 GMT-0500 (EST)"), 
	opener			: { id: 2, username: "jim", deleted: false },
	closer			: null,
	cleanerId		: { id: 3, username: "nate", deleted: false },
	category		: { id: 5, name: "Graffiti", appKey: "GRAFFITI" },
	locationType	: { id: 5, name: "Street", appKey: "STREET" }
	reportedTo311	: true,
};
