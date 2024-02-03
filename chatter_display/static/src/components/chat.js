odoo.define('chatter_display.chat', function (require) {
    "use strict";

    var core = require('web.core');
    var FormView = require('web.FormView');

    FormView.include({
        init: function (parent, dataset, view_id, options) {
            this._super.apply(this, arguments);
            this.on('view_loaded', this, this.onViewLoaded);
        },

        onViewLoaded: function () {
            // Your custom code to be executed when the form view is opened
            console.log('Form view is being opened.');

            // You can access the current record using `this.datarecord`
            if (this.datarecord) {
                console.log('Current record ID:', this.datarecord.id);
            }
        },
    });
});
