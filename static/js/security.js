
//global variables
var valid_employee = true;



//function definitions

function viewEmpProfile(username){
    request = {username: username};
    $.get('/security/employee_profile', request, 
	  function(data){
	      $("#profile").html(data);
	  });
}

function validateEmployee(){
    request = {firstname: $('#id_firstname').val(),
               lastname: $('#id_lastname').val()};
    alert(request.firstname +' '+ request.lastname);
    $.get('/security/is_employee_name_exist', request, function(response){
	response = new String(response).trim();
	alert(response);
	if(response == 'has_duplicate'){
	    valid_employee = false;
	}else{
	    valid_employee = true;
	}
    });
    return valid_employee;
}

$('#gen_emp_id_btn').click(function(){
    $.ajax({
	url : '/security/generate_employee_id',
	dataType : 'html',
	success : function(data){
	    $("#id_username").val(data);
	}
    });
});

$("#id_username").keydown(function(e){
    return allNumbers(e);
});

function ad_employee(user_id, status){
    $.ajax({
	url  : "/security/employee/ad/status",
	data : {user_id : user_id, status: status},
	success: function(data){
	    if (data==1){
		$("#"+user_id).html("<input type='checkbox' checked='checked' onclick='ad_employee("+user_id+", 0)'>&nbsp;True");
	    }else{
		$("#"+user_id).html("<input type='checkbox'  onclick='ad_employee("+user_id+", 1)'>&nbsp;False");
	    }
	}
    });
}


//checker if allowed to add payroll values to employee for a certain payroll month
$("#id_payroll_month").change(function(){
    payroll_month = $(this).val().split("-");
    $.ajax({
        url : "/security/employee/payprofile/isallowtoadd",
        type: "GET",
        data: {"pay_year"  : payroll_month[0],
               "pay_month" : payroll_month[1]},
        success: function(data){
            if (data == "notallowed"){
                $("#id_submit").attr("disabled", "disabled").removeClass().addClass("btn btn-default");
                $("#id_msg").html("<p class='alert alert-warning'>Adding is disabled for approved payroll month. Please select other month</p>");
            }else{
                $("#id_submit").removeAttr("disabled").removeClass().addClass("btn btn-primary");
                $("#id_msg").html("");
            }
        }
    });
});


$("#csi_submit").click(function(){
    $("#csi_submit").removeClass().addClass("btn btn-default").attr("disabled", "disabled").html("<i class='fa fa-spinner fa-pulse'></i>&nbsp;Saving..");
    setTimeout(function(){submitCSI();}, 3000);
});


function submitCSI(){
    $.ajax({
	url : '/security/update/csi',
	type: 'GET',
	dataType: 'JSON',
	data: {'employee_id' : $("#employee_id").val(),
	       'description' : $("#csi_desc").val(),
	       'amount'      : $("#csi_amount").val()},
	success: function(data){
	    csi = data[0].fields;
	    $("#csi_desc").val(csi.description);
	    $("#csi_amount").val(csi.amount);
	    disable_csi_fields();
	    $("#csi_submit").removeClass().addClass("btn btn-primary").removeAttr("disabled").html("Save");
	},
	error: function(jqXHR, textStatus, errorThrown){
	    alert(jqXHR.statusText+": Please fill in description and amount and supply appropriate input before you save!");
	    $("#csi_submit").removeClass().addClass("btn btn-primary").removeAttr("disabled").html("Save");
	}
    });
}


function disable_csi_fields(){
    $("#csi_desc").attr("readonly", "readonly");
    $("#csi_amount").attr("readonly", "readonly");

}

function enable_fields(){
    $("#csi_desc").removeAttr("readonly");
    $("#csi_amount").removeAttr("readonly");

}


$("#csi_clear").click(function(){
    $.ajax({
	url  : "/security/employee/clear/csi",
	data : {"employee_id": $("#employee_id").val()},
	type : "GET",
	dataType: "JSON",
	success : function(data){
	    var fields = data[0].fields;
	    alert("Custom Salary Increase for with description "+ fields.description +" and amount "+ fields.amount + " successfully deleted!");
	    $("#csi_desc").val('');
	    $("#csi_amount").val('');
	},
	error: function(jqXHR, textStatus, errorThrown){
	    alert(jqXHR.statusText+": Clearing custom salary increase failed!");
	}
    });
});


