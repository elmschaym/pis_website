function newVoucher(){
  voucher_id = moment().format("YY")+moment().format("MM")+moment().format("DD")+moment().format("m")+moment().format("ss");
  date_now = moment().format("YYYY-MM-DD")
 // var or_number = $('#or_number').val();
  var claimant = $('#claimant').val();
  var purpose = $('#purpose').val();
  var dept = $('#department').val();
  var expense_type = $('#expense_type').val();
  var amount = $('#amount').val();
  var date_created = $('#date_created').val();
  if(date_created == ''){
       date_now;
  }else{
    date_now=date_created;
  }

  $.ajax({

    type : 'GET',
    data : {_date_now: date_now,_voucher_id:voucher_id, _claimant:claimant, _purpose: purpose,_dept:dept,_expense_type: expense_type, _amount:amount},
    url : '/finance/save_voucher',
    success: function(data){
     // if (confirm('Transaction complete.\nPrint receipt?')){
        $('#view_voucher').html(data);
        $('#voucher_print').printArea()
       //$('#bill_info' ).html(data)
        alert('Transaction complete.');
        
      //} else location.reload()
    },
    error: function(){
     
      alert('Oops!');
      $('.receipt_item').html('')
    },
  }).always(
    $('#save_button').button('reset')
  );
}

function getVoucher(voucher_id){
  $.get('/finance/get_voucher',{_voucher_id:voucher_id,},function(data){
      $('#get_voucher_result').html(data);
    });
  
}

function deleteVoucher(voucher_id){
  if (confirm('Are you sure you want to delete this items?')) {
   $.get('/finance/delete_voucher',{_voucher_id:voucher_id,},function(data){
      $('#index').html(data);
      $('#get_voucher_result').html('<br/><br/><br/><h2 align="center"><b> No Item Selected </b></h2>');

    });
  }
  
}

function addChange(voucher_id){

  var change = $('#ad_change').val();
  $.get('/finance/save_add_change',{_voucher_id:voucher_id, _change:change},function(data){
      $('#get_voucher_result').html(data);
      $('#view_voucher').html(data);
    });
  
}

/*function addAccount(voucher_id){

  var account_title = $('#account_title').val();
  var expense_type = $('#expense_type').val();
  $.get('/finance/save_add_account',{_account_title:account_title, _expense_type:expense_type},function(data){
      $('#account_title_add').html(data);
      alert(account_title+ ' Successfully Added');
    });
  
}*/

function addAccount(voucher_id){
 
  var account_title = $('#account_title').val();
  var expense_type = $('#expense_type').val();
  $.ajax({

    type : 'GET',
    data : {_account_title:account_title, _expense_type:expense_type},
    url : '/finance/save_add_account',
    success: function(data){
        $('#account_title_add').html(data);
        alert(account_title+ ' Successfully Added');       
      
    },
    error: function(){
     
      alert('Cannot be Addeded!');
      
    },
  })
}

/*function deleteAccountTitle(acc_title_id){

    $.ajax({
      alert(acc_title_id)
    type : 'GET',
    data : {account_id:acc_title_id},
    url : '/finance/delete_account_title',
    success: function(data){
    
    },
    error: function(){
     
      alert('Cannot be Deleted!');
    },
  })  
}
*/

function deleteAccountTitle(acc_title_id){
   if (confirm('Are you sure you want to delete this Account title?')) {

  $.ajax({

    type : 'GET',
    data : {account_id:acc_title_id},
    url : '/finance/delete_account_title',
    success: function(data){
        $('#account_title_add').html(data);
        alert('Successfully Deleted.');
        
      
    },
    error: function(){
     
      alert('Cannot be Deleted!');
      
    },
  })
}
}


function editAccountTitle(acc_title_id){

  var account_title = $('#'+acc_title_id+'_title').val();
  var expense_type = $('#'+acc_title_id+'_expense_type').val();
  

  $.get('/finance/save_edit_account',{account_id:acc_title_id,_account_title:account_title, _expense_type:expense_type},function(data){
      $('#account_title_add').html(data);
      alert(' Successfully Edited');
    });
  
}

function editVoucher(voucher_id){
  var claimant = $('#claimant').val();
  var purpose = $('#purpose').val();
  var dept = $('#department').val();
  var expense_type = $('#expense_type').val();
  var amount = $('#amount').val();
  $.get('/finance/save_edit_voucher',{_voucher_id:voucher_id, _claimant:claimant, _purpose: purpose,_dept:dept,_expense_type: expense_type, _amount:amount},function(data){
      $('#get_voucher_result').html(data);
      $('#view_voucher').html(data);
    });
  
}

//$('#check_all_bills').on('click', function ()
$('#acc_type').on('click',function() {
  
    if ($('#acc_type').val()!=""){
        $.get('/finance/check_account_title',{_account_type:$('#acc_type').val() },function(data){
            $('#acc_title_list').html(data);
            $('#amount').removeAttr('disabled');
            $('#department').removeAttr('disabled');
        });
    }
});

$('#acc_type').blur(function() {
    if ($('#acc_type').val()!=""){
        $.get('/finance/check_account_title',{_account_type:$('#acc_type').val() },function(data){
            $('#acc_title_list').html(data);
            $('#amount').removeAttr('disabled');
            $('#department').removeAttr('disabled'); 
        });
    }

});


/*function department(d){
  var dept;
  if(d == 'IT')
    dept = 'Information Technology';
  else if( d == 'R')
    dept = 'Registrat'
  else if(d == 'F')
    dept = 'Finace'
  else if (d == 'P')
    dept = 'Personnel'
  else if (d == 'O')
    dept = 'Other/Miscellaneous'
  else if( d == 'BT')
    dept = 'Board of Trustees'
  else if(d == 'EC')
    dept = 'Executive Committee'
  else if (d == 'U')
    dept = 'Utility'
  else if (d == 'O')
    dept = 'Other'
  return dept
}

*/