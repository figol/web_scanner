openerp.web_scanner = function (instance) {
    var module = instance.web_scanner;
    instance.web.client_actions.add('web.scanner.action', 'instance.web_scanner.action');
    instance.web_scanner.action = instance.web.Widget.extend({
        template: 'web_scanner',
 	    start: function () {
            var self = this;
            /* input focus for scanning */
            $("#web_sale_order").focus();

            /* scanner trigger */
            $("#web_sale_order").keypress(function(e){
                if((e.keyCode || e.which) != 13){
                    return true;
                }
                var order = $(this).val();
                if(!order){
                    alert('empty input');
                    return false;
                }
                instance.web.blockUI();
                new instance.web.Model("sale.order").call("get_order_detail", [order]).then(function(res) {
                    instance.web.unblockUI();
                    if(res.state){
                        self.fn_list_order_lines(res, order);
                    }else{
                        self.fn_show_errors(res);
                    }
                });
            });
        },
        fn_show_errors: function(res){
            this.dialog_view = new module.ScannerErrorDialogWidget(self, {msg: res.msg});
            this.dialog_view.renderElement();
            var _dialog = new instance.web.Dialog(self,{
                title: 'Scanner Error', autoOpen:true, width:700, resizable:false, modal:true,
                buttons:{
                    "Close": function () {
                        _dialog.destroy();
                        $('#web_sale_order').val('').focus();
                    }
                }
            }, this.dialog_view.$el);
            _dialog.open();
	        // focus first form button
            $('.oe_form_button:first').focus().addClass('oe_highlight');
        },
        fn_list_order_lines: function(res, order){
            this.dialog_view = new module.ScannerLinesWidget(self, {res: res});
            this.dialog_view.renderElement();
            var _dialog = new instance.web.Dialog(self,{
                title: 'Order: '+order, autoOpen:true, width:700, resizable:false, modal:true,
                buttons:{
                    "Close": function () {
                        _dialog.destroy();
                        $('#web_sale_order').val('').focus();
                    }
                }
            }, this.dialog_view.$el);
            _dialog.open();
	        // focus first form button
            $('.oe_form_button:first').focus().addClass('oe_highlight');
        },
    });

    module.ScannerLinesWidget = instance.web.Widget.extend({
        template: 'ScannerLinesWidget',
        init: function(parent, options){
            this.res = options.res;
        }
    });
    module.ScannerErrorDialogWidget = instance.web.Widget.extend({
        template: 'ScannerErrorDialogWidget',
        init: function(parent, options){
            this.msg = options.msg;
        }
    });
};

