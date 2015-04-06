angular.module('app.services').service('EvaluationSvc', function($http){
    this.getEvaluation = function(params){
	return $http.post('/registration/student_evaluation/',  params);
    }
    
    this.save_grades = function(params){
	return $http.post('/registration/student_old_grade', params);
    }
});
