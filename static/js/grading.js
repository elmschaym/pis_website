function getStudents(){
    var data = {'subject_id' : $('#subject_id').val(),
		'period'     : $('#period').val(),
		'section_id' : $('#section_id').val()}

    $.get("/grading/get_students", data, function(rs){
	$("#student_table").html(rs);
    });
}


function setSubjectandgetStuds(subject_id){
    $('#subject_id').val(subject_id)
    getStudents();
}

function setGradPeriodandgetStuds(period){
    $('#period').val(period)
    getStudents();
}

