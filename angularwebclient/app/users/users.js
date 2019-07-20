'use strict';

angular.module('myApp.users', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/users', {
    templateUrl: 'users/users.html',
    controller: 'UsersCtrl'
  });
}])

.controller('UsersCtrl', ['$scope', '$http', function($scope, $http) {
	
	$scope.users = null;
	
	$http({
		method: 'GET',
		url: 'http://127.0.0.1:8001/quickstart/users/'
	}).then(function successCallback(response) {
		console.log(response);
		$scope.users = response.data.results;
	}, function errorCallback(response) {
		  console.log(response);
	});	
	
}]);