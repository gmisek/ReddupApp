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
	$scope.issues = [];
	$scope.currentMarker = null;
	$scope.newIssue = {};
	$scope.mapOptions = {
		center: new google.maps.LatLng(40.4406, -79.9961),
		zoom: 12,
		mapTypeId: google.maps.MapTypeId.ROADMAP
	};

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
		//$('#spinner').spin();
		$scope.clearMarkers();
		$scope.issues = sampleIssues;
		$.each($scope.issues, function (index, issue){
			issue.marker = $scope.newMarker(issue.lat, issue.lng);
		});
		$scope.refreshMarkers();
		//$('#spinner').stop();

		// $.getJSON(
		// 	"url",
		// 	function (data) {
		// 		$('#spinner').stop();
		// 		// TODO: change to $scope.issues = data;
		// 	}
		// );
	};

	$scope.addIssue = function() {
		//TODO: push to server
		console.log($scope.newIssue);
		$http({
			url: "/issue/open/",
		    method: "POST",
		    data: {
		    	"opener_id" : 1,
		    	"description" : $scope.newIssue.description,
		    	"before_img" : $scope.newIssue.image,
		    	"category_id" : $scope.newIssue.category,
		    	"reported_to_311" : false,
		    	"location_type_id" : 1,
		    	"longitude" : $scope.newIssue.longitude+'',
		    	"latitude" : $scope.newIssue.latitude+''
		    }
		}).success(function(data, status, headers, config) {
    		$scope.refreshMarkers();
    		$scope.setMode('select');
    	}).error(function(data, status, headers, config) {
    		//
    	});
	};

	$scope.cancelNewIssue = function () {
		$scope.setMode('select');
		$scope.newIssue = {};
		$scope.clearMarkers();
		$scope.refreshMarkers();
	};

	$scope.newMarker = function(lat, lng) {
		return new google.maps.Marker({
			map: $scope.map,
			position: new google.maps.LatLng(parseFloat(lat), parseFloat(lng))
		});
	};

	$scope.tempMarker = function ($event) {
		new google.maps.Marker({
			map: $scope.map,
			position: $event.latLng
		});
		
		$scope.newIssue.latitude = $event.latLng.hb;
		$scope.newIssue.longitude = $event.latLng.ib;

		$scope.setMode('details');
	};

	$scope.removeMarker = function (index) {
		$scope.issues.splice(index, 1)
	};

	$scope.clearMarkers = function () {
		$.each($scope.issues, function(index, issue){
			issue.marker.setMap(null);
		});
	};

	$scope.refreshMarkers = function () {
		$.each($scope.issues, function(index, issue){
			issue.marker.setMap($scope.map);
		});
	};

	setTimeout(function(){ $scope.fetchPoints(); }, 1000);
}]);

var sampleIssues = [
	{
		id 				: 1,
		description 	: "Found some graffiti on the side of an office building on Penn Ave",
		lat 			: '40.462013',
		lng 			: '-79.926331',
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
		lat 			: '40.457736',
		lng 			: '-79.928359‎',
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
		lat 			: '40.453185', 
		lng 			: '-79.918220‎',
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
