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
                    ajaxLoader.fadeIn(function () {
                        $(form).ajaxSubmit({
                            success: function () {
                                ajaxLoader.fadeOut(function () {
                                    $('.success-message').fadeIn();
                                });
                            },
                            error: function () {
                                ajaxLoader.fadeOut(function () {
                                    $('.error-message').fadeIn();
                                });
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
});
