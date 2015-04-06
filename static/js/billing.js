function searchStudent(form){
  var search_text;
  search_text = $('#'+ form + " #seach_student").val();
  var itemSelect;
  itemSelect = $ ('#student_search_filters').val();
  $.get('/billing/searchstudent', {_search: search_text, _type:itemSelect}, function(data){
      $('#stud_list ').html(data);
    });
}

var csrftoken = $.cookie('csrftoken');

var selected;
function getStudent(id){
  selected=id;
  $.get('/billing/getstudent', {student: id }, function(data){
      $('#stud_info').html(data);
      $('#student_id').val();
  });
  getBills(id);
  bindTabs();
}

function getBills(id){
  $.get('/billing/getbill', {student: id }, function(data){
      $('#bill_info' ).html(data);  
      bindCheckboxes();
      $('#history_tab').removeClass('active');
      $('#bills_tab').addClass('active');
  });
  $('#tabs').css('display', 'block')
  $('#tabbed-panel').css('display', 'block')
}

function getHistoryTransaction(id){
      $.get('/billing/get_history', {student: id }, function(data){
        $('#bill_info' ).html(data);
        $('#bills_tab').removeClass('active');
        $('#history_tab').addClass('active');
  });
}

function getItemHistory(id){
      $.get('/billing/getitemhistory', {transact_id: id,  }, function(data){
      $('#bill_info').html(data);  
     
  });
}

function delete_bill_items(student){
  var items = []
if (confirm('Are you sure you want to delete this items?')) {
  $("input[name='student_bills[]']:checked").each(function(){
     
      items.push($(this).val());
  });

    $.get('/billing/delete_bill_items', {items: items, student:student },function(data){
      
      bindCheckboxes();
      data = new String(data).trim();
      if(data == 'Fail'){
        bindCheckboxes();
        alert('Tution or Registration Fee Cannot be deleted');
      }else{
        $('#bill_info' ).html(data);
        bindCheckboxes();
        alert('Successfully Deleted');
      }

    });

      
} 

}

function deleteTransaction(id, student){

  if (confirm('Are you sure you want to delete this transaction?')) {
    $.get('/billing/delete_transaction', {transact_id: id }, function(data){
      $('#bill_info' ).html(data);

      });

      alert('Successfully Deleted');
} 
  
}

function bindCheckboxes(){
  $('#check_all_bills').on('click', function () {
    $('.bill_picker').prop('checked', this.checked);
    updateTotal();
  });
  
  $('.bill_picker').on('change', function () {
    var check = ($('.bill_picker').filter(":checked").length == $('.bill_picker').length);
    $('#check_all_bills').prop("checked", check);
    updateTotal();
  });

  $('#check_all_bill_item').on('click', function () {
    $('.bill_picker_item_name').prop('checked', this.checked);
    
  });
  
  $('.bill_picker_item_name').on('change', function () {
    var check = ($('.bill_picker_item_name').filter(":checked").length == $('.bill_picker').length);
    $('#check_all_bills').prop("checked", check);
    
  });
}
var sum =0;
var count = 0;
var sumkitab =0;
var countkitab = 0;
var discounted = 0;
var dis = 0;
var total=0;
function print(){
  var or_number = $('#old_or_number').val();
  $('.or_number').html(or_number.replace(/,/g,''))
  $('.payee_name').html($('#payee_name').html())
  $('.payee_id').html($('#payee_id').val())
  $('#transact').button('loading')
  $("input[name='student_bills[]']").each(function(){
    //var amt = $(this).data('value');
    var name = $(this).data('item');
    if( $('#Tuition').val() == name && name != undefined ){

        sum += parseFloat($(this).data('value'));
        count++;
    }else if($(this).data('item')=='Kitab'){
        
        sumkitab += parseFloat($(this).data('value'));
        countkitab ++;
    }else{
    
      if ($(this).val()){
      $('.receipt_item').append('<tr><td>'+$(this).data('item')+'</td>'
        +'<td style="text-align:right">'+$(this).data('value')+'</td></tr>')
      
      }  
    }
  });

  if (countkitab > 1) {
      $('.receipt_item').append('<tr><td>'+countkitab+' '+'Kitabs'+'</td>'
        +'<td style="text-align:right">'+addCommas(sumkitab.toFixed(2))+'</td></tr>')

  }else if(countkitab==1){ 
       $('.receipt_item').append('<tr><td>'+countkitab+' Kitab'+'</td>'
        +'<td style="text-align:right">'+addCommas(sumkitab.toFixed(2))+'</td></tr>')

  }
  
  if(count > 4 ){
      if(count > 4 && count <10){
        dis = 5
      }else{
        dis = 10
      }
      discounted = addDiscount(parseFloat(sum),dis) 
  }else{
    discounted = parseFloat(sum);
  }

  if(count >= 5 ){
     $('.receipt_item').append('<tr><td>'+count+' Months Tuition Fee with '+dis+'% </td>'
        +'<td style="text-align:right">'+addCommas(sum.toFixed(2))+'</td></tr>')
  }else if(count == 1){
     $('.receipt_item').append('<tr><td>'+count+' Month Tuition Fee </td>'
        +'<td style="text-align:right">'+addCommas(sum.toFixed(2))+'</td></tr>')
  }else   if(count > 1 && count < 5 ){
     $('.receipt_item').append('<tr><td>'+count+' Months Tuition Fee </td>'
        +'<td style="text-align:right">'+addCommas(sum.toFixed(2))+'</td></tr>')
  }
  $('.receipt_item').append('<tr class="receipt_total"><td><strong>Total</strong></td><td style="text-align:right"><strong>'+$('#all_total').val()+'</strong></td></tr>')
  count = 0;
  sum = 0 ;
  sumkitab =0;
  countkitab =0;
  discounted = 0;
  total = 0;

      
  $.ajax({

/*    type : 'POST',
    data : {items:items, tender:tender, total:total, discount:dis, studentID:studentID},
    url : url,*/
    success: function(data){
      $('#full_receipt').printArea('popup')
      $('.receipt_item').html('')
 /*      $('#bill_info' ).html(data)
      alert('Transaction complete.');*/
      bindCheckboxes();
    },
    error: function(){
     
      alert('Oops!');
      $('.receipt_item').html('')
    },
  }).always(
    $('#transact').button('reset')
  );

}

var sum =0;
var sumkitab =0;
function transact(url , studentID){
  //$("#tender").disabled = true;
  document.getElementById("tender").disabled = true;
  var total = updateTotal();
  var items = [];
  //alert($('#payee_id').val())
  var or_number = $('#or_number').val();
  $('.or_number').html(or_number)
  $('.payee_id').html($('#payee_id').val())
  $('.payee_name').html($('#payee_name').html())
  $('#transact').button('loading')
  $("input[name='student_bills[]']:checked").each(function(){
    var amt = $(this).data('value');
    var name = $(this).data('item');
    if( $('#Tuition').val() == name && name != undefined ){
        sum += parseFloat($(this).data('value'));
        items.push($(this).val())
        count++;
    }else if($(this).data('item')=='Kitab'){
        items.push($(this).val())
        sumkitab += parseFloat($(this).data('value'));
        countkitab ++;
    }else{

      if ($(this).val()){
      items.push($(this).val())
      $('.receipt_item').append('<tr><td>'+$(this).data('item')+'</td>'
        +'<td style="text-align:right">'+$(this).data('value')+'</td></tr>')
      
      }  
    }
  });

  if (countkitab > 1) {
      $('.receipt_item').append('<tr><td>'+countkitab+' '+'Kitabs'+'</td>'
        +'<td style="text-align:right">'+addCommas(sumkitab.toFixed(2))+'</td></tr>')

  }else if(countkitab==1){
       $('.receipt_item').append('<tr><td>'+countkitab+' Kitab'+'</td>'
        +'<td style="text-align:right">'+addCommas(sumkitab.toFixed(2))+'</td></tr>')

  }

  if(count > 4 ){
      if(count > 4 && count <10){
        dis = 5
      }else{
        dis = 10
      }
      discounted = addDiscount(parseFloat(sum),dis) 
  }else{
    discounted = parseFloat(sum);
  }

  if(count >= 5 ){
     $('.receipt_item').append('<tr><td>'+count+' Months Tuition Fee with '+dis+'% </td>'
        +'<td style="text-align:right">'+addCommas(discounted.toFixed(2))+'</td></tr>')
  }else if(count == 1){
     $('.receipt_item').append('<tr><td>'+count+' Month Tuition Fee </td>'
        +'<td style="text-align:right">'+addCommas(discounted.toFixed(2))+'</td></tr>')
  }else   if(count > 1 && count < 5 ){
     $('.receipt_item').append('<tr><td>'+count+' Months Tuition Fee </td>'
        +'<td style="text-align:right">'+addCommas(discounted.toFixed(2))+'</td></tr>')
  }
  $('.receipt_item').append('<tr class="receipt_total"><td><strong>Total</strong></td><td style="text-align:right"><strong>'+addCommas(total)+'</strong></td></tr>')
  sumkitab =0;
  countkitab =0;
  count = 0;
  discounted = 0;
  sum = 0;
  var now = moment().format("MMMM DD, YYYY, h:mm:ss A")
  $('.date').html(now) 
  var tender = parseFloat($("#tender").val());
  if (!tender){
    alert('No cash tendered.');
    $('.receipt_item').html('')
    $('#transact').button('reset')
    return;
  }
  if (tender < total){
    alert('Insufficient cash tendered.');
    $('.receipt_item').html('')
    $('#transact').button('reset')
    return;
  }
if(tender >= total){  
  var change = tender-total
  tender = tender-change
  $('#change').html(addCommas(change.toFixed(2)))

  $.ajax({

    type : 'POST',
    data : {items:items, tender:tender, total:total, discount:dis, studentID:studentID, or_number:or_number},
    url : url,
    success: function(data){
      
      if (confirm('Transaction complete.\nPrint receipt?')){
        $('#full_receipt').printArea('popup')
        $('.receipt_item').html('')
        $('#bill_info' ).html(data)
        alert('Transaction complete.');
        bindCheckboxes();
        dis = 0;
      } else location.reload()
      $('#tender').removeAttr('disabled');
    },
    error: function(){
      
      alert('Oops!');
      $('.receipt_item').html('')
      $('#tender').removeAttr('disabled');
    },
  }).always(
    $('#transact').button('reset')
  );
  }
}

function transact_one(url){
  document.getElementById("tender").disabled = true;
  var total = parseFloat($('#total').html());
  var items = [];
  var or_number = $('#or_number').val();
  $('.or_number').html(or_number)
  $('.payee_name').html($('#payee_name').html())
  $('#transact').button('loading')
  $("input[name='student_bills[]']:checked").each(function(){
   if($(this).data('item')=='Kitab'){
        items.push($(this).val())
        sumkitab += parseFloat($(this).data('value'));
        countkitab ++;
    }else {
        if ($(this).val()){
          items.push($(this).val())
          $('.receipt_item').append('<tr><td>'+$(this).data('item')+'</td>'
            +'<td style="text-align:right">'+$(this).data('value')+'</td></tr>')
          
          
        }
    }
  });
  if (countkitab > 1) {
      $('.receipt_item').append('<tr><td>'+countkitab+' '+'Kitabs'+'</td>'
        +'<td style="text-align:right">'+addCommas(sumkitab.toFixed(2))+'</td></tr>')

  }else if(countkitab==1){
       $('.receipt_item').append('<tr><td>'+countkitab+' Kitab'+'</td>'
        +'<td style="text-align:right">'+addCommas(sumkitab.toFixed(2))+'</td></tr>')

  }
  $('.receipt_item').append('<tr class="receipt_total"><td><strong>Total</strong></td><td style="text-align:right"><strong>'+total.toFixed(2)+'</strong></td></tr>')
  
  var now = moment().format("MMMM DD, YYYY, h:mm:ss A")
  $('.date').html(now) 
  var tender = parseFloat($("#tender").val());
  if (!tender){
    alert('No cash tendered.');
    $('.receipt_item').html('')
     $('#transact').button('reset')
    return;
  }
  if (tender < total){
    alert('Insufficient cash tendered.');
    $('.receipt_item').html('')
    $('#transact').button('reset')
    return;
  }

  sumkitab =0;
  countkitab =0;
  var change = tender-total
  tender = tender-change
  $('#change').html(change.toFixed(2))
  $.ajax({
    type : 'post',
    data : {items:items, tender:tender, total:total, peyee:$("input[name='payee']").val(),or_number:or_number},
    url : url,
    
    success: function(data){
      if (confirm('Transaction complete.\nPrint receipt?')){
        $('#full_receipt').printArea('popup')
        $('.receipt_item').html('')
        $('#bill_info' ).html(data)
      } else location.reload()
      $('#tender').removeAttr('disabled');
    },
    error: function(){
      alert('Oops!');
      $('.receipt_item').html('')
      $('#tender').removeAttr('disabled');
    },
  }).always(
    $('#transact').button('reset')
  );
}

function addCommas(nStr) {
    nStr += '';
    x = nStr.split('.');
    x1 = x[0];
    x2 = x.length > 1 ? '.' + x[1] : '';
    var rgx = /(\d+)(\d{3})/;
    while (rgx.test(x1)) {
            x1 = x1.replace(rgx, '$1' + ',' + '$2');
    }
    return x1 + x2;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function updateTotal(){
  var count = 0;
  var discounted = 0;
  var due = 0 ;
  var total = 0.0;
  var tuition_total = 0.0;
  $("input[id='bill_picker']:checked").each(function(){
    var amt = $(this).data('value');
    var discounted_amt = parseFloat(amt);
    if( $(this).data('type') == 'T' ){
        count = count + 1;
        tuition_total += discounted_amt;
    }
    total += discounted_amt;
  });
  discounted_amt = tuition_total;
  if ((count >= 5)&&(count < 10)){
    discounted_amt = addDiscount(tuition_total, 5)
  }else if(count >= 10){
    discounted_amt = addDiscount(tuition_total, 10)
  }
  due = total - tuition_total;
  due += discounted_amt
  
  /*if(count > 4 ){
      if(count > 4 && count <10){
        discounted = addDiscount($(this).data('value'), 5) 
      }else{
        discounted = addDiscount($(this).dacashta('value'), 10) 
      }
  }else{
    discounted = $(this).data('value')
  }
  due = total - $(this).data('value');
  due = due + discounted;
  alert($("input[id='bill_picker']:checked").each().val);*/
  //alert(addCommas(total.toFixed(2)));
  $('#total').html(addCommas(total.toFixed(2)));
  $('#due').html(addCommas(due.toFixed(2)));
  count = 0;
  return due.toFixed(2)
}

function addDiscount(amount,discount){
 
    return amount - ((discount/100)*amount)
}



function billSearch(form){

  var q = $('#'+form+' #item_search_field').val();
  var type = $('#item_search_filters').val();
  var student_id = $("input[name='student_id']").val();

  $.get('/billing/search_item', {query : q, query_type : type, student : student_id}, function(data){
    
    $('#bill_search_results').html(data);
    bindCheckboxes()
  });
}

function clearItemSearch(){
  $("#table_of_items").remove();
}

function billStudent(form){
  
  var type = $('#item_search_filters').val();
  $("input[name='bills[]']:checked").each(function(){
    
    $.get('/billing/bill_student', {query_type : type,'bill':parseInt($(this).val()), 'student':$("input[name='student_id']").val() } , function(data){
      $('#bill_info').html(data);
      bindCheckboxes();
      clearItemSearch();
    });
  });
}

function customBill(c_amount, c_description){
 // alert($('#'+c_amount).val()+" "+)
  $.get('/billing/custom_bill',{amount : $('#'+c_amount).val(), description : $('#'+c_description).val(), 'student':$("input[name='student_id']").val()}, function(data){
      $('#bill_info').html(data);
      bindCheckboxes();
      clearItemSearch();
  });
  $('#custom_close').click();
}


function advance_tuition(){
  var counted = $('#item_advance_tuition').val();
  var bill = $('#Tuition_id').val();
  
    
    $.get('/billing/bill_student', {query_type : 'advance_tuition','bill':bill, 'student':selected, 'count':counted } , function(data){
      $('#bill_info').html(data);
      bindCheckboxes();
      clearItemSearch();
    });
}

function branchRemittance(){
  var remittance_payee = $('#remittance_payee').val()
  var branch = $('#branch').val()
  var amount_remittance = $('#amount_remittance').val()
  var or_number = $('#or_number_rem').val();

/*   $.get('/billing/remittance_transaction', {_remittance_payee:remittance_payee, _branch:branch, _amount_remittance:amount_remittance }, function(data){
    
    $('#report_detail').html(data);
    
  });*/ 
  $.ajax({

      type : 'GET',
      data : {_or_number: or_number,_remittance_payee:remittance_payee, _branch:branch, _amount_remittance:amount_remittance},
      url : '/billing/remittance_transaction',
      success: function(data){
       // if (confirm('Transaction complete.\nPrint receipt?')){
          $('#bill_info').html(data);
          $('#remittance_receipt').printArea()
         //$('#bill_info' ).html(data)
          alert('Transaction complete.');
          
        //} else location.reload()
      },
      error: function(){
       
        alert('Error!');
        
      },
    }).always(
      $('#add_remittance').button('reset')
    );
}

function addBill(form){
  var type = $('#item_search_filters').val();
  var items = []
  $("input[name='bills[]']:checked").each(function(){
    items.push($(this).val())
    
  }); 
  var query = $('#query_copy').val()
  $.post('/billing/others/add_bill', {
      query_type : type, 
      query_copy : query,
      'items':items, 
      'payee':$("input[name='payee']").val() 
    } , function(data){
    $('#bill_info').html(data);
    bindCheckboxes();
    $("input[name='bills[]']:checked").each(function(){
      $(this).removeAttr('checked')
    });
  });
  
}

function getMonthlyDetail(month,item){
    $.get('/billing/collection_detail', {month : month, item : item}, function(data){
    
    $('#report_detail').html(data);
    
  }); 
}

$('#bill_pick input[type="checkbox"]').on('change', function(){
  if ($('#bill_pick input:checkbox:checked').length > 0)
    $('#bill_student_button').removeAttr('disabled');
  else
    $('#bill_student_button').attr('disabled', 'disabled');
});



function bindTabs(){
  $('#bills_tab').on('click', function(){
    getBills($('input[name="student_id"]').val());
  })
  $('#history_tab').on('click', function(){
    //if ($('#history_tab').class('active')){}
    getHistoryTransaction($('input[name="student_id"]').val());
  })
}

$(document).ready(function(){
bindCheckboxes();
bindTabs();

})


function getCAData(ca_id){
    $.ajax({
	data : {'ca_id' : ca_id},
	type : 'GET',
	dataType: 'JSON',
	url : '/billing/cash_advance/get/cadata',
	success: function (data, status){
	    var id = data[0].pk;
	    fields = data[0].fields;
	    console.log(data);
	    $("#ca_action").val("edit");
	    $("#ca_id").val(id);
	    $("#id_employee").val(fields.employee);
	    $("#id_amount").val(fields.amount);
	    $("#ca_modal").modal("show");
	    var pay_month = (fields.pay_month < 10)? "0"+fields.pay_month : fields.pay_month;
	    $("#ca_submit #id_payroll_month").val(fields.pay_year+"-"+pay_month);
	},
	error: function(textStatus, errorThrown){
	    alert(textStatus.error);
	}
    });
}


$("#ca_form_btn").click(function(){
    $("#ca_action").val("add");
    $("#ca_modal").modal('show');
});

$("#ca_submit_btn").click(function(){
    $("#ca_submit").submit();
});


function submitCA(){
    var payroll_month_str = $("#ca_submit #id_payroll_month").val();
    var payroll_month = $("#ca_submit #id_payroll_month").val().split("-");
    var pay_year = payroll_month[0];
    var pay_month = payroll_month[1];

    $.ajax({
	url  : '/billing/cash_advance/form/submit',
	data : {'action'    : $("#ca_action").val(),
		'ca_id'     : $("#ca_id").val(),
		'employee'  : $("#id_employee").val(),
		'pay_year'  : pay_year,
		'pay_month' : pay_month,
		'amount'    : $("#id_amount").val()},
	type : 'GET',
	dataType: 'HTML',
	success: function(data){
	    $("#ca_table_con").html(data);
	    //set the payroll month for the filter form
	    $("#id_payroll_month").val(payroll_month_str);
	    $("#ca_modal").modal('hide');
	    $("#err_msg").removeClass().html();
	    //show success message
	    $("#msg_body").html("<h3><span class='glyphicon glyphicon-check text-success'></span>&nbsp;<small>Cash Advance Succesfully Saved!</small></h3>");
	    $("#msg_modal").modal("show");
	},
	error  : function(jqXHR, textStatus, errorThrown){
	    $("#err_msg").removeClass().addClass("text-danger").html("ERROR! Please Input an appropriata data and dont leave other fields blank");
	}
    });
}


//checks the selected payroll month is already aproved
$("#ca_submit #id_payroll_month").change(function(){
    payroll_month = $(this).val().split("-");
    
    $.ajax({
        url : "/security/employee/payprofile/isallowtoadd",
        type: "GET",
        data: {"pay_year"  : payroll_month[0],
               "pay_month" : payroll_month[1]},
        success: function(data){
            if (data == "notallowed"){
                $("#ca_submit_btn").attr("disabled", "disabled").removeClass().addClass("btn btn-default");
                $("#err_msg").removeClass().addClass("text-danger").html("You selected an approved payroll month, Please select other month");
            }else{
                $("#ca_submit_btn").removeAttr("disabled").removeClass().addClass("btn btn-primary");
                $("#err_msg").removeClass().html("");
            }
        }
    });
});



//delete cash advance
function delCA(ca_id, name, amount){
    var ans = confirm("Are you sure to delete '"+name+"' Cash Advance with an amount of "+amount+"?");
    if (ans){
	$.ajax({
	    url : '/billing/cash_advance/delete/cadata',
	    data: {'ca_id' : ca_id},
	    daType: 'HTML',
	    type : 'GET',
	    success: function(data){
		$("#ca_table_con").html(data);
		$("#msg_body").html("<h3><span class='glyphicon glyphicon-check text-success'></span>&nbsp;<small>Cash Advance of '"+name+"' with an amount of Php. "+amount+" successfully deleted!</small></h3>");
		$("#msg_modal").modal("show");

	    },
	    error: function(jqXHR, textStatus, errorThrown){
		$("#msg_body").html("<h3><span class='glyphicon glyphicon-exclamation-sign text-danger'></span>&nbsp;<small>"+ jqXHR.responseText+": Failed to delete '"+name+"' cash Advance!</small></h3>");
		$("#msg_modal").modal("show");

	    }
	});
    }
    
}

