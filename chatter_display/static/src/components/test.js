odoo.define('your_module.your_js_file', function (require) {
    "use strict";

    var core = require('web.core');
    var Widget = require('web.Widget');

    var YourWidget = Widget.extend({
        template: 'YourTemplate',

        start: function () {
            this._super.apply(this, arguments);

            // Set a cookie
            this.setCookie('yourCookieName', 'cookieValue', 7); // 7 days expiration

            // Get the value of a cookie
            var cookieValue = this.getCookie('yourCookieName');
            console.log('Cookie Value:', cookieValue);
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
    });

    return YourWidget;
});
