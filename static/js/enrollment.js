function bindSubjects(){
    $('#check_all_subjects').click(function(){
	$('.subject_class').prop('checked', this.checked);
    });
}

function getStudents(){
    var inputs = {'search_option' : $('#search_option').val(),
		  'search_text' : $('#search_text').val()
		 };
    $.ajax({
	type : 'GET',
	data : inputs,
	url  : '/enrollment/get_students',
	success : function(data){
	    $("#student_list").html(data);
	},
	error   : function(data){
	    alert('Error!');
	}
    });
}

function getStudentInfo(studentID){
    $.ajax({
	data : {'studentID' : studentID},
	type : 'GET',
	url  : '/enrollment/get_student_info',
	success : function(data){
	    $("#main_container").html(data);
	    bindSubjects();
	    $("#check_all_subjects").click();
	    $("#close").click();
	},
	error : function(data){
	    alert('Error:\n' + data);
	}
    });
}


function getSchedule(){
    $.ajax({
	type : 'GET',
	data : {'id' : $("#section").val()},
	url  : '/enrollment/get_schedule',
	success : function(data){
	    $("#schedule").html(data);
	},
	error : function(){
	    alert('Invalid Section Selected')
	}
    });
}


function enterGrade(){
    inputs = {'stud_id': $('#stud_id').val(),
		'grade'  : $('#grade_id').val()
	     }
    if (inputs.stud_id == '' || inputs.grade==''){
	alert('Please Select a student and Enter a Valid Grade');
    }else{

	$.ajax({
	    data : inputs,
	    type : 'GET',
	    url  : '/enrollment/enter_grade',
	    success: function(data){
		$('#id-grade-con').html(data);
	    },
	    error : function(data){
		alert('Error Occur. Please input a valid grade');
	    }

	});
    }
}
