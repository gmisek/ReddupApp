/* MAIN JS */

/*
	UI Modes:
		1. default
		2. identify
		3. details
		4. claim
		5. solve
*/


var myApp = angular.module('steelCityReddUp', ['ui'])
.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
})
.controller('Controller', ['$scope', '$http', function ($scope, $http) {
	$scope.mode = {
		select: true,
		identify: false,
		details: false,
		claim: false,
		solve: false
	};
	$scope.markers = [];
	$scope.currentMarker = null;
	$scope.mapOptions = {
		center: new google.maps.LatLng(40.4406, -79.9961),
		zoom: 12,
		mapTypeId: google.maps.MapTypeId.ROADMAP
	};

	$scope.$watch('markers', function(){
		$scope.addAllMarkers();
	});

	$scope.setMode = function (mode) {
		$scope.mode = {
			select: false,
			identify: false,
			details: false,
			claim: false,
			solve: false
		};
		$scope.mode[mode] = true;
	};

	$scope.fetchPoints = function() {
		$('#spinner').spin();
		$.getJSON(
			"url",
			function (data) {
				$('#spinner').stop();
				// TODO: change to $scope.markers = data;
				$scope.markers = samplePoints;
			}
		);
	};

	$scope.addMarker = function(latLng) {
		$scope.markers.push(new google.maps.Marker({
			map: $scope.map,
			position: latLng
		}));
	};

	$scope.addIssue = function(event) {
		//TODO: push to server
		$http.post()
		.success();
	};

	$scope.addAllMarkers = function	() {
		$scope.clearMarkers();
		$.each($scope.markers, function(){
			$scope.addMarker
		});
	};

	$scope.clearMarkers = function () {
		$.each($scope.markers, function(marker){
			//marker.setMap(null);
		});
	};
}]);

var samplePoints = [
	{
		id 				: 1,
		description 	: "Found some graffiti on the side of an office building on Penn Ave",
		latLng 			: 'new LatLng(40.462013, -79.926331)',
		beforeImg 		: "before.jpg",
		afterImg 		: "after.jpg",
		dateOpened		: 'new Date("Sat Feb 23 2013 11:48:20 GMT-0500 (EST)")',
		dateClosed		: 'new Date("Sun Feb 24 2013 12:48:20 GMT-0500 (EST)")', 
		opener			: { id: 2, username: "jim", deleted: false },
		closer			: null,
		cleanerId		: { id: 3, username: "nate", deleted: false },
		category		: { id: 5, name: "Graffiti", appKey: "GRAFFITI" },
		locationType	: { id: 5, name: "Street", appKey: "STREET" },
		reportedTo311	: true
	},
	{
		id 				: 2,
		description 	: "Large pothole on Ellsworth Ave",
		latLng 			: 'new LatLng(40.457736, -79.928359‎)',
		beforeImg 		: "before.jpg",
		afterImg 		: "after.jpg",
		dateOpened		: 'new Date("Sat Feb 23 2013 13:45:44 GMT-0500 (EST)")',
		dateClosed		: 'new Date("Sun Feb 24 2013 09:21:20 GMT-0500 (EST)")', 
		opener			: { id: 3, username: "geoff", deleted: false },
		closer			: null,
		cleanerId		: { id: 4, username: "ben", deleted: false },
		category		: { id: 1, name: "Pothole", appKey: "POTHOLE" },
		locationType	: { id: 5, name: "Street", appKey: "STREET" },
		reportedTo311	: true
	},
	{
		id 				: 3,
		description 	: "Large pothole on Fifth Ave",
		latLng 			: 'new LatLng(40.453185, -79.918220‎)',
		beforeImg 		: "before.jpg",
		afterImg 		: "after.jpg",
		dateOpened		: 'new Date("Sat Feb 23 2013 14:45:44 GMT-0500 (EST)")',
		dateClosed		: 'new Date("Sun Feb 24 2013 10:21:20 GMT-0500 (EST)")', 
		opener			: { id: 5, username: "shawn", deleted: false },
		closer			: null,
		cleanerId		: { id: 6, username: "david", deleted: false },
		category		: { id: 1, name: "Pothole", appKey: "POTHOLE" },
		locationType	: { id: 5, name: "Street", appKey: "STREET" },
		reportedTo311	: true
	}
];
