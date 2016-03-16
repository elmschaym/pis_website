angular.module('app.controllers').controller('EventsCtrl', function($log, $scope,EventsSvc){
	$scope.news_result = {};

	$scope.getNews = function(){
			EventsSvc.getNewsSvc().success(function(data,status){
				
				$scope.news_result=data;
				$log.log(data);
				//$('#news_scroll').scrollTop($('#news_scroll')[0].scrollHeight);
				/*var objDiv = document.getElementById("news_scroll");
				objDiv.scrollTop = objDiv.scrollHeight;*/
				//$("#news_scroll").scrollTop($("#news_scroll")[0].scrollHeight);
			})
			.error(function(data, status){
			$log.log(data);
		    })

	}

	$scope.getEvents = function(){
			EventsSvc.getEventsSvc().success(function(data,status){
				
				$scope.events_result=data;
				$log.log(data);
				//$('#news_scroll').scrollTop($('#news_scroll')[0].scrollHeight);
				/*var objDiv = document.getElementById("news_scroll");
				objDiv.scrollTop = objDiv.scrollHeight;*/
				//$("#news_scroll").scrollTop($("#news_scroll")[0].scrollHeight);
			})
			.error(function(data, status){
			$log.log(data);
		    })

	}


	$scope.newsViewMore = function(){
			EventsSvc.newsViewMore().success(function(data,status){
				//alert(data);
				//$('#table_news').append();
				//$("#news_scroll").scrollTop($("#news_scroll")[0].scrollHeight);
				
				$scope.news_result=data;
				$log.log(data);
				//$('#news_scroll').scrollTop($('#news_scroll')[0].scrollHeight);
				var objDiv = document.getElementById("news_scroll");
				objDiv.scrollTop = objDiv.scrollHeight;
				//$('#news_scroll').scrollIntoView(false);

			})
			.error(function(data, status){
			$log.log(data);
		    })
	}

	$scope.newsViewMoreEvents = function(){
				EventsSvc.newsViewMoreEvents().success(function(data,status){
					//alert(data);
					//$('#table_news').append();
					//$("#news_scroll").scrollTop($("#news_scroll")[0].scrollHeight);
					
					$scope.events_result=data;
					$log.log(data);
					//$('#news_scroll').scrollTop($('#news_scroll')[0].scrollHeight);
					var objDiv = document.getElementById("news_scroll2");
					objDiv.scrollTop = objDiv.scrollHeight;
					//$('#news_scroll').scrollIntoView(false);

				})
				.error(function(data, status){
				$log.log(data);
			    })
		}

	$scope.view_news = function(id){
		EventsSvc.view_newsSvc(id).success(function(data,status){

			$('#result_news').html(data);
		})
		.error(function(data, status){
			$log.log(data);
		    })
	}

});
 
/*angular.module('app.controllers').controller('EvaluationCtrl', function($scope, $log, $modal, EvaluationSvc){
    $scope.level_types = [{'val': 1, 'text': 'Nursery' },
			  {'val': 2, 'text': 'Kinder' },
			  {'val': 3, 'text': 'Elementary(Old)' },
			  {'val': 4, 'text': 'HighSchool(Old)' },
			  {'val': 5, 'text': 'Elementary(New)' },
			  {'val': 6, 'text': 'HighSchool(New)' }];

    $scope.evaluation_params = {};
    $scope.evaluation = {};
    $scope.grades = [];


    $scope.getEvaluation = function(){
	$scope.evaluation_params['csrfmiddlewaretoken'] = $('[name="csrfmiddlewaretoken"]').val();
	$log.log($scope.evaluation_params);

	EvaluationSvc.getEvaluation($scope.evaluation_params)
	    .success(function(data, status){
		$scope.evaluation = data;
		$log.log(data);
	    })
	    .error(function(data, status){
		$log.log(data);
	    })
    }

    $scope.items = [1, 2, 3];
    //modal for grade entry
    $scope.openTransferreGradeEntryModal = function(year_level, student_id){
	
	var modalInstance = $modal.open({
	    templateUrl: '/static/angular-app/templates/evaluation/transferre_grade_form.html',
	    controller: 'TranferreModalInstanceCtrl',
	    size: 'lg',
	    resolve: {
		items: function () {
		    return {'year_level': year_level, 'student_id': student_id};
		}
	    }
	});

	modalInstance.result.then(function (selectedItem) {
	    $scope.selected = selectedItem;
	}, function () {
	    $log.info('Modal dismissed at: ' + new Date());
	});
    }

});



angular.module('app.controllers').controller('TranferreModalInstanceCtrl', function($scope, $modalInstance, $log, items, EvaluationSvc){

    $scope.grade = {};
    $scope.year_grades = {};
    $scope.year_levels = ['Nursery', 'Kinder Junior', 'Kinder Senior',
			  'Grade 1', 'Grade 2', 'Grade 3', 'Grade 4', 
			  'Grade 5', 'Grade 6', 'Grade 7', 'Grade 8',
			  '1st Year Junior', '2nd Year Junior', '1st Year Senior',
			  '2nd Year Senior'];
    $scope.year_level_desc = $scope.year_levels[items.year_level-1];
    $log.log(items.year_level);
    $scope.grades_entered = [];
    $log.log(items.student_id);
    
    $scope.add_subject = function(){
	var new_grade = $scope.grade;
	$scope.grade = {};
	$scope.grades_entered.push(new_grade);
    }

    $scope.save = function(){
	$scope.year_grades['student_id'] = items.student_id;
	$scope.year_grades['year_level'] = items.year_level;
	$scope.year_grades['grades'] = $scope.grades_entered;
	//$modalInstance.close('sas');
	EvaluationSvc.save_grades($scope.year_grades)
	    .success(function(data, status){
		
	    })
	    .error(function(data, status){
		
	    })
    }

    $scope.cancel = function(){
	$modalInstance.dismiss('cancel');
    }


});
*/