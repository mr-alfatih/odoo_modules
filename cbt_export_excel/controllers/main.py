# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import content_disposition, request
import io
import xlsxwriter


class InvoiceExcelReportController(http.Controller):
    @http.route([
        # '/invoicing/excel_report/<model("invoice.reports"):report_id>',
        '/invoicing/excel_report/<model("sale.order"):report_id>',
    ], type='http', auth="user", csrf=False)
    def get_sale_excel_report(self, report_id=None, **args):
        response = request.make_response(
            None,
            headers=[
                ('Content-Type', 'application/vnd.ms-excel'),
                ('Content-Disposition', content_disposition('Invoice_report' + '.xlsx'))
            ]
        )
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        # create some style to set up the font type, the font size, the border, and the aligment
        title_style = workbook.add_format({'font_name': 'Times', 'font_size': 14, 'bold': True, 'align': 'center'})
        header_style = workbook.add_format({'font_name': 'Cambria', 'bold': True, 'left': 1, 'bottom':1, 'right':1, 'top':1, 'align': 'center'})
        text_style = workbook.add_format({'font_name': 'Times', 'left': 1, 'bottom':1, 'right':1, 'top':1, 'align': 'left'})
        number_style = workbook.add_format({'font_name': 'Times', 'left': 1, 'bottom':1, 'right':1, 'top':1, 'align': 'right'})
        # get data for the report.
        report_lines = report_id.get_report_lines()
        # prepare excel sheet styles and formats
        # sheet = workbook.add_worksheet("invoices")
        sheet = workbook.add_worksheet("Quotation")
        # sheet.write(1, 0, 'No.', header_style)
        # sheet.write(0, 0, 'No.', header_style)
        # sheet.write(1, 1, 'Description', header_style)
        # sheet.write(0, 1, 'Description', header_style)
        sheet.write(0, 0, 'Description', header_style)
        sheet.write(0, 1, 'QTY', header_style)
        sheet.write(0, 2, 'UNIT PRICE', header_style)
        sheet.write(0, 3, 'TOTAL PRICE', header_style)
        sheet.write(0, 4, 'ESTIMATION COST', header_style)
        # sheet.write(1, 1, 'Invoice Reference', header_style)
        # sheet.write(1, 2, 'Customer', header_style)

        # row = 2
        row = 1
        # number = 1
        number = 0
        # write the report lines to the excel document
        for line in report_lines:
            print('line------------>', line)
            sheet.set_row(row, 20)
            if line['d_type'] == 'line_section':
                sheet.merge_range(f'A{row+1}:E{row+1}', ' ', title_style)
                # sheet.merge_range(row, 0, line['description'], text_style)
            # sheet.write(row, 0, number, text_style)
            # sheet.write(row, 1, line['description'], text_style)
            sheet.write(row, 0, line['description'], text_style)
            sheet.write(row, 1, line['qty'], text_style)
            sheet.write(row, 2, line['unit_price'], text_style)
            sheet.write(row, 3, line['total_price'], text_style)
            sheet.write(row, 4, line['estimation_cost'], text_style)
            # sheet.write(row, 1, line['move_id'], text_style)
            # sheet.write(row, 2, line['partner_id'], text_style)
            row += 1
            number += 1
        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()
        return response

# class SaleExcelReportController(http.Controller):
#     @http.route([
#         '/sale/excel_report/<model("ng.sale.wizard"):wizard>',
#     ], type='http', auth="user", csrf=False)
#     def get_sale_excel_report(self,wizard=None,**args):
#         # the wizard parameter is the primary key that odoo sent
#         # with the get_excel_report method in the ng.sale.wizard model
#         # contains salesperson, start date, and end date
#
#         # create a response with a header in the form of an excel file
#         # so the browser will immediately download it
#         # The Content-Disposition header is the file name fill as needed
#
#         response = request.make_response(
#                     None,
#                     headers=[
#                         ('Content-Type', 'application/vnd.ms-excel'),
#                         ('Content-Disposition', content_disposition('Sales Report in Excel Format' + '.xlsx'))
#                     ]
#                 )
#
#         # create workbook object from xlsxwriter library
#         output = io.BytesIO()
#         workbook = xlsxwriter.Workbook(output, {'in_memory': True})
#
#         # create some style to set up the font type, the font size, the border, and the aligment
#         title_style = workbook.add_format({'font_name': 'Times', 'font_size': 14, 'bold': True, 'align': 'center'})
#         header_style = workbook.add_format({'font_name': 'Times', 'bold': True, 'left': 1, 'bottom':1, 'right':1, 'top':1, 'align': 'center'})
#         text_style = workbook.add_format({'font_name': 'Times', 'left': 1, 'bottom':1, 'right':1, 'top':1, 'align': 'left'})
#         number_style = workbook.add_format({'font_name': 'Times', 'left': 1, 'bottom':1, 'right':1, 'top':1, 'align': 'right'})
#
#         # loop all selected user/salesperson
#         for user in wizard.user_id:
#             # create worksheet/tab per salesperson
#             sheet = workbook.add_worksheet(user.name)
#             # set the orientation to landscape
#             sheet.set_landscape()
#             # set up the paper size, 9 means A4
#             sheet.set_paper(9)
#             # set up the margin in inch
#             sheet.set_margins(0.5,0.5,0.5,0.5)
#
#             # set up the column width
#             sheet.set_column('A:A', 5)
#             sheet.set_column('B:E', 15)
#
#             # the report title
#             # merge the A1 to E1 cell and apply the style font size : 14, font weight : bold
#             sheet.merge_range('A1:E1', 'Sales Report in Excel Format', title_style)
#
#             # table title
#             sheet.write(1, 0, 'No.', header_style)
#             sheet.write(1, 1, 'Document', header_style)
#             sheet.write(1, 2, 'Date', header_style)
#             sheet.write(1, 3, 'Customer', header_style)
#             sheet.write(1, 4, 'Total', header_style)
#
#             row = 2
#             number = 1
#
#             # search the sales order
#             # orders = request.env['sale.order'].search([('user_id','=',user.id), ('date_order','>=', wizard.start_date), ('date_order','<=', wizard.end_date)])
#             # print('kw---->', kw)
#             print('wizard---->', wizard)
#             print('wizard id---->', wizard.sale_id.id)
#             orders = request.env['sale.order'].sudo().search([('id','=',wizard.sale_id.id)])
#             print(orders)
#             # for order in orders:
#             for order in orders.order_line:
#                 # the report content
#                 sheet.write(row, 0, number, text_style)
#                 sheet.write(row, 1, order.name, text_style)
#                 # sheet.write(row, 2, str(order.date_order), text_style)
#                 sheet.write(row, 2, str(order.product_uom_qty), text_style)
#                 # sheet.write(row, 3, order.partner_id.name, text_style)
#                 sheet.write(row, 3, order.price_unit, text_style)
#                 # sheet.write(row, 4, order.amount_total, number_style)
#                 sheet.write(row, 4, order.price_subtotal, number_style)
#
#                 row += 1
#                 number += 1
#
#             # create a formula to sum the total sales
#             sheet.merge_range('A' + str(row+1) + ':D' + str(row+1), 'Total', text_style)
#             sheet.write_formula(row, 4, '=SUM(E3:E' + str(row) + ')', number_style)
#
#         # return the excel file as a response, so the browser can download it
#         workbook.close()
#         output.seek(0)
#         response.stream.write(output.read())
#         output.close()
#
#         return response
#
