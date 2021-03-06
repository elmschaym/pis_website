function getSchedules(section_id){
    var url = '/scheduling/get_schedules';
    $('#section_id').val(section_id);
    $.get(url, {id:section_id}, function(data){
	$("#sched_panel_id").html(data);
    });
}

function removeSched(sched_id){
    var conf = confirm("Are you sure to delete this schedule?");

    if (conf){
	$.ajax({
	    data : {'sched_id':sched_id},
	    url : '/scheduling/remove_get_sched',
	    type : 'GET',
	    success : function(data){
		$("#sched_panel_id").html(data);
	    },
	    error : function(data){
		alert('Cannot delete schedule. Technical Error Occur');
	    }	
	});
    }
}

function addGetSchedules(){
    $('#id_alert').removeClass();
    var inputs = {'section_id': $('#section_id').val(),
		  'subject': $('#id_subject').val(),
		  'teacher': $('#id_teacher').val(),
		  'time_start': $('#id_time_start').val(),
		  'time_end': $('#id_time_end').val(),
		  'day': $('#id_day').val()
		 }
    $.ajax({
	data: inputs,
	type: 'GET',
	url: '/scheduling/set_get_schedules',
	success: function(data){
	    rs_data = new String(data).trim();

	    if(rs_data == 'conflict1'){
		$('#id_alert').addClass('alert alert-danger');
		$('#id_alert').html('Conflict!. Schedule currenly taken');
	    }else if(rs_data == 'conflict2'){
		$('#id_alert').addClass('alert alert-danger');
		$('#id_alert').html('Conflict schedule for teacher. Teacher already had schedule in this time and date');
	    }else{
		$('#sched_panel_id').html(data);
		$('.close').click();
	    }

	},
	error: function(data){
	    alert(data);
	}
    });
}

$().ready(function(){
    $('#all_year').click();   
});

$('#all_year').click(function(){
    $('.year_level_class').prop('checked', this.checked);
});

function getSubjects(section_id){
    $.get('/scheduling/subject_for_section', {'section_id':section_id}, 
	  function(data){
	    $('#subject_field').html(data);
	  }
	 );
}


function viewSubjectInfo(subject_id){
    $.ajax({
	data : {'subject_id': subject_id},
	url : '/scheduling/get_subject_info',
	type : 'GET',
	success: function(data){
	    $('#subject_info_id').html(data);
	}
    });
}

function checkSectionAction(){
    /*
      before redirecting or taking an action
      this function checks whether the action is edit or delete
     */
    if ($('action').val()=='del'){
	return false;
    }else{
	return true;
    }
}


$('.year_level_class').click(function(){
    $('#all_year').prop('checked', this.checked)
});

function print_list(){
  $('#list_student_print').printArea();
}

function print_list_guidelines(){
  $('#guidelines_print').printArea();
}


$('#add_sched').click(function(){
    $('#id_alert').removeClass().html('');
});



function changeOffering(id, offering_status){
    var data = {id: id,
	       offering_status: offering_status}

    $.get("/scheduling/change_offering", data, function(rs){
	rs = new String(rs).trim();
	if (rs=="done"){
	    if (offering_status==1){//lock
		var html = "<input type='checkbox'  onchange='changeOffering("+id+", 0)'> No";
		$("#"+id).html(html);
	    }else{
		var html = "<input type='checkbox'  onchange='changeOffering("+id+", 1)' checked> Yes";
		$("#"+id).html(html);
	    }
	}
    });
}

function isSubjectbeDeleted(subject_id){
    $.get("/scheduling/is_subject_be_deleted", {'subject_id': subject_id}, function(rs){
	rs = new String(rs).trim();
	if (rs=="ok"){
	    window.location = "/scheduling/delete_subject/"+subject_id+"/";
	}else{
	    alert("This subject contains student grades, So delete action for this subject is restricted");
	}
    })
}



function changeCurriculum(subject_id){
    var data = {subject_id : subject_id,
	       curriculum  : $("#curriculum"+subject_id).val()}
    $.get("/scheduling/change_curriculum/", data, function(rs){
	
    });
}
