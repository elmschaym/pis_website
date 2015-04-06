$('#gen_stud_id_btn').click(function(){
    $.ajax({
	url : '/registration/generate_student_id',
	
	dataType : 'html',
	success : function(data){
	    $("#id_studentid").val(data);
	}
    });
});

$("#id_studentid").keydown(function(e){
    return allNumbers(e);
});


$("#all_student_grade_checkbox").click(function(){
    $(".studentgrade_check_box").prop('checked', this.checked);
});


$(".studentgrade_check_box").change(function(){
    var checkall = ($(".studentgrade_check_box").filter(":checked").length == $(".studentgrade_check_box").length);
    $("#all_student_grade_checkbox").prop("checked", checkall);
});


function showStudentEvaluation(student_id){
    var data = {student_id : student_id,
	       level_type  : $("#level_type").val()}
    $.get("/registration/student_evaluation/", data, function(rs){
	$("#evaluation").html(rs);
    });
}


function setGEEntryVal(subject_id, year_level){
    var title = $("#s"+subject_id).html();
    var q1 = $("#q1"+subject_id).html();
    var q2 = $("#q2"+subject_id).html();
    var q3 = $("#q3"+subject_id).html();
    var q4 = $("#q4"+subject_id).html();

    $("#subject_title").text(title);
    $("#subject_id").val(subject_id);
    $("#student_id").val(student_id);
    $("#slevel").val(year_level);
    $("#q1_grade").val(q1);
    $("#q2_grade").val(q2);
    $("#q3_grade").val(q3);
    $("#q4_grade").val(q4);
    
}


function addUpdateGrade(){
    
    var data = {subject_id : $("#subject_id").val(),
		student_id : $("#student_idnumber").val(),
		slevel     : $("#slevel").val(),
		curriculum : $("#curriculum_selected").val(),
		q1         : $("#q1_grade").val(),
		q2         : $("#q2_grade").val(),
		q3         : $("#q3_grade").val(),
		q4         : $("#q4_grade").val()}

    $.get("/registration/add_update_studentgrades", data, function(rs){
	rs = new String(rs).trim();
	if (rs=="failed"){
	    alert("Subject Grade Update Function Currently experiencing error!")
	}else{
	    $("#yr"+data.slevel).html(rs);
	    $("#evaluation_grade_entry_form").modal('hide');
	}
    });

}

function printForm137(stud_id){
    var data = {student_id : stud_id,
		level_type  : $("#level_type").val()}

    $.get("/registration/form137_print", data, function(rs){
	rs = new String(rs).trim();
	var mywindow = window.open("", "my div", "height=600,width=900");
	mywindow.document.write(rs);
	mywindow.print();
	mywindow.close();
    })
}


