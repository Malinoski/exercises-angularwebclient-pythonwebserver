'use strict';

angular.module('myApp.polls', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/polls', {
    templateUrl: 'polls/polls.html',
    controller: 'PollsCtrl'
  });
}])

.controller('PollsCtrl', ['$scope', '$http', function($scope, $http) {
	
	$scope.polls = null;
	
	$http({
		method: 'GET',
		url: 'http://127.0.0.1:8001/polls/questions/'
	}).then(function successCallback(response) {
		console.log(response);
		$scope.polls = response.data.results;
	}, function errorCallback(response) {
		  console.log(response);
	});	
	
}]);