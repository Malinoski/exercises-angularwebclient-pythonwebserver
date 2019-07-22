'use strict';

angular.module('myApp.snippets', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/snippets', {
    templateUrl: 'snippets/snippets.html',
    controller: 'SnippetsCtrl'
  });
}])

.controller('SnippetsCtrl', ['$scope', '$http', function($scope, $http) {
	
	$scope.snippets = null;
	
	$http({
		method: 'GET', 
		url: 'http://127.0.0.1:8001/snippets/'
	}).then(function successCallback(response) {
		console.log(response);
		$scope.snippets = response.data;
	}, function errorCallback(response) {
		  console.log(response);
	});		
	
}]);