import xlwt
from xlsxwriter.workbook import Workbook
from io import BytesIO, StringIO
import base64
from odoo import api, fields, models


class ExeclGen(models.Model):
    _name = 'execle.gen.'

    def generate_excel_report(self):
        filename = 'filename.xlsx'
        workbook = xlwt.Workbook(encoding="UTF-8")
        worksheet = workbook.add_sheet('Sheet 1')
        style = xlwt.easyxf('font: bold True, name Arial;')
        worksheet.write_merge(0, 1, 0, 3, 'your data that you want to show into excelsheet', style)
        fp = StringIO()
        workbook.save(fp)
        record_id = self.env['wizard.excel.report'].create({'excel_file': base64.encodestring(fp.getvalue()),
                                                            'file_name': filename}, )
        fp.close()
        return {'view_mode': 'form',
                'res_id': record_id,
                'res_model': 'wizard.excel.report',
                'view_type': 'form',
                'type': 'ir.actions.act_window',
                'context': context,
                'target': 'new',
                }


class wizard_excel_report(models.Model):
    _name = "wizard.excel.report"
    excel_file = fields.Binary('excel file')
    file_name = fields.Char('Excel File', size=64)
