$(function(){
    $('form').validate({

        submitHandler: function(form) {
            $('input[type=submit]').fadeOut(function(){
                $(form).ajaxSubmit({
                   success: function(){
                       $('.success-message').fadeIn();
                   },
                    error : function(){
                        $('.error-message').fadeIn();
                    }
                });
            });
        },

        errorElement: "span",
        errorPlacement: function(error, element) {
            $(element).prev().append(error);
        },

        errorClass: "error-message"
        
    });
});
