$(function(){

    var ajaxLoader = setUpAjaxLoader();
    setUpFormToBeAjaxEnabled();

    function setUpAjaxLoader() {
        var ajaxLoader = $('<img src="/static/images/ajax-loader.gif" class="ajax-loader"/>');
        ajaxLoader.hide();
        ajaxLoader.appendTo($('#confirmation'));
        return ajaxLoader;
    }

    function setUpFormToBeAjaxEnabled() {
        $('form').validate({
            submitHandler: function (form) {
                $('input[type=submit]').fadeOut(function () {
                    ajaxLoader.fadeIn(function() {
                        $(form).ajaxSubmit({
                            success: function(json) {
                                if(json.success)
                                    hideAjaxLoaderAndShow('.success-message');
                                else
                                    hideAjaxLoaderAndShow('.error-message');
                            },
                            error: function() {
                                hideAjaxLoaderAndShow('.error-message');
                            }
                        });
                    });
                });
            },
            errorElement: "span",
            errorPlacement: function (error, element) {
                $(element).prev().append(error);
            },
            errorClass: "error-message"
        });
    }

    function hideAjaxLoaderAndShow(selector) {
        ajaxLoader.fadeOut(function () {
            $(selector).fadeIn();
        });
    }
    
});
