'use strict';

angular.module('myApp.polls', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/polls', {
    templateUrl: 'polls/polls.html',
    controller: 'PollsCtrl'
  });
}])

.controller('PollsCtrl', ['$http', function($http) {
	
	$http({
		method: 'GET',
		url: 'http://127.0.0.1:8001/quickstart/users/'
	}).then(function successCallback(response) {
		console.log(response);	    
	}, function errorCallback(response) {
		  console.log(response);
	});
	
	
}]);