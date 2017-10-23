$(document).ready(function(){
  var $myForm = $('.my-ajax-form');
  $myForm.submit(function(e){
    e.preventDefault();
    var $formData = $myForm.serialize();
    var $thisUrl = $myForm.attr('data-url') || window.location.href;
    $.ajax({
      method: 'POST',
      url: $thisUrl,
      data: $formData,
      success: handleSuccess,
      error: handleError,
    });
    function handleSuccess(data){
      console.log(data.message);
      $myForm[0].reset()
    }
    function handleError(ThrowError){
      console.log(ThrowError);
    }
  })
})
