var talentpool = angular.module('talentpool', ['ngRoute']);

talentpool.config(['$routeProvider', function($routeProvider) {
    $routeProvider
        .when('/', {
            templateUrl : 'templates/talentTable.html',
            controller  : 'talentController'
        });
}]);

talentpool.factory('talentService', function(){
    return {
        all: function() {
            return [
                {
                    firstName:'Giovanni',
                    lastName:'Trappatoni',
                    mail:'gtrappa@student.ethz.ch',
                    address: {
                        city: 'Strübelbach',
                        zip: 4902,
                        street: 'Otterweg 2c',
                    },
                    phone: '076 412 78 31',
                    birthday: '25.08.1988',
                    fieldOfStudy: 'Information Technology, Communication Technology',
                    status: 'Master',
                    knownFrom: 'Amiv Kontakt',
                    rating: 'a',
                    interests: 'Trainee, Direkteinstieg, BA-MA-Arbeit'
                },
                {
                    firstName:'Fulvio',
                    lastName:'Spaghetti',
                    mail:'fulvioaldente@student.ethz.ch',
                    address: {
                        city: 'Stans',
                        zip: 4902,
                        street: 'Stüberlüb 23',
                    },
                    phone: '078 361 34 21',
                    birthday: '14.04.1991',
                    fieldOfStudy: 'Elektrotechnik',
                    status: 'Master',
                    knownFrom: 'Amiv Kontakt',
                    rating: 'c',
                    interests: 'Praktika',
                    remarks: 'Praktikum ab März zw. BA und MA'
                },
                {
                    firstName:'Moledi',
                    lastName:'Berlusconi',
                    mail:'mammamia@gmail.ch',
                    address: {
                        city: 'Lausanne',
                        zip: 1007,
                        street: 'Avenue lala 11',
                    },
                    phone: '079 461 14 30',
                    fieldOfStudy: 'Computer and Communication Sciences',
                    status: 'Phd',
                    knownFrom: 'Forum EPFL',
                    rating: 'a',
                    interests: 'Direkteinstieg',
                    remarks: 'PhD soll 2014 beendet sein. I.A. mit Lobo L. an Alfred S. für INA weitergeleitet. Weitere Dokumente von ihm im Ordner'
                },
                {
                    firstName:'Roger',
                    lastName:'Michellein',
                    mail:'michel@gmail.com',
                    address: {
                        city: 'Rennes',
                        zip: 1020,
                        street: 'Avenue Du Bois 13',
                    },
                    phone: '079 261 94 21',
                    fieldOfStudy: 'Master in Comunication Systems, Minor in Management, Technology and Entrepreneurship',
                    status: 'Master',
                    knownFrom: 'Forum EPFL',
                    rating: 'b',
                    interests: 'Direkteinstieg',
                    remarks: 'hat sich bei Michael beworben, haben ihn empfohlen'
                }
            ];
        }
    };
});

talentpool.controller('talentController',['$scope', 'talentService',
function($scope, talentService) {
    $scope.talents = talentService.all();
    $scope.selectedTalent = $scope.talents[0];
    $scope.markAsSelected = function(talent) {
        $scope.selectedTalent = talent;
    };
}]);
