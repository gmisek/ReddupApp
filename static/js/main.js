/* MAIN JS */

/*
	UI Modes:
		1. default
		2. identify
		3. details
		4. claim
		5. solve
*/

$(document).ready(function() {
	//$('#spinner').spin();
});

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
		solve: false,
		pledge: false,
		userList: false,
		list: false
	};
	$scope.issues = [];
	$scope.activeIssue = null;
	$scope.newIssue = {};
	$scope.mapOptions = {
		center: new google.maps.LatLng(40.4406, -79.9961),
		zoom: 14,
		mapTypeId: google.maps.MapTypeId.ROADMAP
	};

	$scope.setMode = function (mode) {
		$scope.mode = {
			select: false,
			identify: false,
			details: false,
			solve: false,
			pledge: false,
			userList: false,
			list: false
		};
		$scope.mode[mode] = true;
	};

	$scope.fetchPoints = function() {
		$scope.clearMarkers();
		
		//$scope.issues = sampleIssues;
		$http({
			type: 'GET',
			url: '/issues/all/ajax/'
		}).success(function (data) {
			$scope.issues = data;
			$.each($scope.issues, function (index, issue){
				issue.marker = $scope.newMarker(issue.lat, issue.lng);
				issue.date_opened = new Date(issue.date_opened);
				issue.reported = Math.floor(Math.random() * 5);
			});
			$scope.refreshMarkers();
		});
	};

        /*
	$scope.openIssue = function() {
		$scope.loading = true;
		$http({
			url: "/issue/open/",
		    method: "POST",
		    data: {
		    	"user_id" : 1,
		    	"description" : $scope.newIssue.description,
		    	"before_img" : $scope.newIssue.image,
		    	"category_id" : $scope.newIssue.category,
		    	"reported_to_311" : false,
		    	"location_type_id" : 1,
		    	"longitude" : $scope.newIssue.longitude+'',
		    	"latitude" : $scope.newIssue.latitude+''
		    }
		}).success(function(data, status, headers, config) {
			$scope.loading = false;
    		$scope.refreshMarkers();
    		$scope.setMode('select');
    	}).error(function(data, status, headers, config) {
    		$scope.loading = false;
    	});
	};
*/
	$scope.closeMsg = function () {
		$scope.setMode('select');
	};

	$scope.cancelNewIssue = function () {
		$scope.setMode('select');
		if ($scope.newIssue.marker) $scope.newIssue.marker.setMap(null);
		$scope.newIssue = {};
	};

	$scope.newMarker = function(lat, lng) {
		return new google.maps.Marker({
			map: $scope.map,
			position: new google.maps.LatLng(parseFloat(lat), parseFloat(lng))
		});
	};

	$scope.tempMarker = function ($event) {
		$scope.activeIssue = {};
		if ($scope.mode.identify) {
			if ($event) {
				if ($scope.newIssue.marker != null || $scope.newIssue.marker != undefined) {
					$scope.newIssue.marker.setMap(null);
				}
				$scope.newIssue = {};
				$scope.newIssue.marker = new google.maps.Marker({
					map: $scope.map,
					position: $event.latLng
				});
				
				$scope.newIssue.latitude = $event.latLng.hb;
				$scope.newIssue.longitude = $event.latLng.ib;

				$scope.setMode('details');
			} else {

				if ($scope.newIssue.marker != null || $scope.newIssue.marker != undefined) {
					$scope.newIssue.marker.setMap(null);
				}
				var yourLat, yourLong;
				navigator.geolocation.getCurrentPosition(function(position) {
					yourLat = position.coords.latitude;
					yourLong = position.coords.longitude;
				});
				$scope.newIssue = {};
				$scope.newIssue.marker = new google.maps.Marker({
					map: $scope.map,
					position: new google.maps.LatLng(40.460271, -79.916954)
				});
				
				$scope.newIssue.latitude =  yourLat;
				$scope.newIssue.longitude = yourLong;

				$scope.setMode('details');
			}
		}
	};

	$scope.closeIssue = function (issue) {
		$scope.loading = true;
		$http({
			url: "/issue/" + issue.id + "/close/",
		    method: "POST",
		    data: {
		    	"issue_id" : issue.id,
		    	"after_img" : issue.afterImg,
		    	"closer_id" : issue.closer.id,
		    	"cleaner_id" : issue.cleaner.id
		    }
		}).success(function(data, status, headers, config) {
			$scope.loading = false;
    		$scope.closeHasSucceeded = true;

    		if ($scope.alertMe) {
    			$http({
					url: "/pledge/new/",
				    method: "POST",
				    data: {
				    	"user_id" : 1,
				    	"latitude" : 40.460271,
				    	"longitude" : -79.916954
				    }
				});
    		}

    		$scope.fetchPoints();
    	}).error(function(data, status, headers, config) {
    		$scope.loading = false;
    	});
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

	$scope.openDetails = function(issue) {
		$scope.cancelNewIssue();
		$scope.activeIssue = issue;
		$scope.map.panTo(new google.maps.LatLng(issue.lat, issue.lng));
	};

	$scope.claimIssue = function(issueId) {
		$scope.loading = true;
		$http({
			url: "/issue/" + issueId + "/claim/",
		    method: "POST",
		    data: {
		    	"user_id" : 1,
		    	"issue_id" : issueId
		    }
		}).success(function(data, status, headers, config) {
			$scope.loading = false;
    		$scope.setMode('userList')
    		$scope.fetchPoints();
    	}).error(function(data, status, headers, config) {
    		$scope.loading = false;
    	});
	};

	$scope.reUpIssue = function(issueId) {
		$scope.loading = true;
		$http({
			url: "/issue/" + issueId + "/reup/",
		    method: "POST",
		    data: {
		    	"user_id" : 1,
		    	"issue_id" : issueId
		    }
		}).success(function(data, status, headers, config) {
			$scope.loading = false;
    		$scope.setMode('select')
    		$scope.fetchPoints();
    	}).error(function(data, status, headers, config) {
    		$scope.loading = false;
    	});
	};

	setTimeout(function(){
		$scope.fetchPoints();
		navigator.geolocation.getCurrentPosition(function(position) {
			$scope.map.panTo(new google.maps.LatLng(position.coords.latitude,position.coords.longitude));
		});
	}, 1000);
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
		cleaner  		: { id: 3, username: "nate", deleted: false },
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
		cleaner 		: { id: 4, username: "ben", deleted: false },
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
		cleaner 		: { id: 6, username: "david", deleted: false },
		category		: { id: 1, name: "Pothole", appKey: "POTHOLE" },
		locationType	: { id: 5, name: "Street", appKey: "STREET" },
		reportedTo311	: true
	}
];
