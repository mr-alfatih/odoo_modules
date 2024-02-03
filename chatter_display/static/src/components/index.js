odoo.define('chatter_display.ChatterDisplay', function (require) {
    "use strict";

    console.log('Chatterbox loaded');

    // var core = require('web.core');
    var Widget = require('web.Widget');
    var SystrayMenu = require('web.SystrayMenu');

    var FormController = require('web.FormController');
    var FormView = require('web.FormView');
    var core = require('web.core');
    var _t = core._t;

        FormView.include({
        render_buttons: function ($node) {
            this._super.apply(this, arguments);
            console.log("Entered value -------------------------------------");
            if (this.$buttons) {
                var customButton = $(QWeb.render('chatter_display.ChatterDisplay'));
                customButton.on('click', this.proxy('on_custom_button_click'));
                this.$buttons.append(customButton);
            }
        },

        on_custom_button_click: function () {
            // Perform actions when the custom button is clicked
            var value = prompt(_t("Enter a value:"));
            if (value !== null) {
                // Store the value somewhere or perform additional actions
                console.log("Entered value:", value);
            }
        },
    });

//    var YourWidget = Widget.extend({
//        template: 'YourTemplate',
//
//        start: function () {
//            this._super.apply(this, arguments);
//
//            // Set a cookie
//            this.setCookie('yourCookieName', 'cookieValue', 7); // 7 days expiration
//
//            // Get the value of a cookie
//            var cookieValue = this.getCookie('yourCookieName');
//            console.log('Cookie Value:', cookieValue);
//        },
//
//
//    });

//    FormView.include({
//        init: function (viewInfo, params) {
//            this._super.apply(this, arguments);
//
//            // Trigger your custom function when the form view is initialized
//            this.triggerCustomFunction();
//        },
//
//        start: function () {
//            return this._super.apply(this, arguments).then(this.proxy('onStart'));
//        },
//
//        onStart: function () {
//            // Trigger your custom function when the form view is started
//            this.triggerCustomFunction();
//        },
//
//        // Custom function that you want to trigger
//        triggerCustomFunction: function () {
//            console.log("Form view is opened. Your custom function is triggered!");
//
//            // Your custom logic goes here
//        },
//    });

    //TODO: Implement localstorage
    // var chatterDisplay = localStorage.getItem('chatter_display');

    // if(chatterDisplay){
    //     localStorage.setItem("chatter_display", "0");
    // }

    // var toggleDisplay = function(){

    //     if(localStorage.getItem('chatter_display') != "0"){
    //         console.log('chatter_display exists');
    //         localStorage.setItem("chatter_display", "0");
    //         $('.o_FormRenderer_chatterContainer').css("display","none");
    //     }else{
    //         console.log('chatter_display is not found');
    //         localStorage.setItem("chatter_display", "1");
    //         $('.o_FormRenderer_chatterContainer').css("display","block");
    //     }

    // }



    var TopButton = Widget.extend({
        template:'chatter_display.ToggleChatterBox',
        events: {
            "click": "on_click"
        },

        setCookie: function (name, value, days) {
            var expires = "";
            if (days) {
                var date = new Date();
                date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
                expires = "; expires=" + date.toUTCString();
            }
            document.cookie = name + "=" + value + expires + "; path=/";
        },

        getCookie: function (name) {
            var nameEQ = name + "=";
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i];
                while (cookie.charAt(0) === ' ') {
                    cookie = cookie.substring(1, cookie.length);
                }
                if (cookie.indexOf(nameEQ) === 0) {
                    return cookie.substring(nameEQ.length, cookie.length);
                }
            }
            return null;
        },
        on_click: function (event) {
            //do action

            var cookieValue = this.getCookie('yourCookieName');
            if(cookieValue){
                console.log('Get The Cookie Value And Show:', cookieValue);
                $('.o_FormRenderer_chatterContainer').css("display","block");
                $('.o_form_sheet').css("max-width","inherit");
            }else{
                console.log('Get The Cookie Value And Hide:', cookieValue);
                $('.o_FormRenderer_chatterContainer').css("display","none");
                $('.o_form_sheet').css("max-width","100%");
            }

            //$('.o_FormRenderer_chatterContainer').css("display","none");
            //$('.o_FormRenderer_chatterContainer').toggle('fast', 'linear');
            //toggleDisplay();

            // Get the current value from localStorage and convert it to a boolean
            let currentValue = localStorage.getItem('chatter_display') === 'true';

            // Toggle the value
            currentValue = !currentValue;

            // Update the value in localStorage
            localStorage.setItem('chatter_display', currentValue.toString());
            this.setCookie('yourCookieName', currentValue, 7);

            // Example usage: logging the toggled value
            console.log('Toggled value:', currentValue);
            console.log('yourCookieName value:', cookieValue);

//            if(cookieValue){
            if(currentValue){

                $('.o_FormRenderer_chatterContainer').css("display","block");
                $('.o_form_sheet').css("max-width","inherit");


            }else{
                $('.o_FormRenderer_chatterContainer').css("display","none");
                $('.o_form_sheet').css("max-width","100%");
            }
        }
    });

    TopButton.prototype.sequence = -1;

    console.log(TopButton)


    SystrayMenu.Items.push(TopButton);

    // FormController.include({
    //     init: function () {
    //         this._super.apply(this, arguments);
    //         this.on_load();
    //     },

    //     on_load: function () {
    //         console.log('Chatter Sigmund test')
    //     },
    // });



});