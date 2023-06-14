import xlrd
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ImportCustomerWizard(models.Model):
    _name = "import.customer.wizard"
    file = fields.Binary(string="File", required=True)
    file_name = fields.Char(string="File Path", required=True)
    ic_ids = fields.One2many('import.customer','ic_id')

    # def import_customer(self):
    #     try:
    #         wb = openpyxl.load_workbook(filename=BytesIO(base64.b64decode(self.file)), read_only=True )
    #     ws = wb.active
    #     for record in ws.iter_rows(min_row=2, max_row=None, min_col=None,
    #                                max_col=None, values_only=True):
    #         # search if the customer exist else create
    #         search = self.env['res.partner'].search([
    #             ('name', '=', record[1]), ('customer_rank', '=', True)])
    #         if not search:
    #             self.env['res.partner'].create({
    #                 'ref': record[0],
    #                 'name': record[1],
    #                 'street': record[2],
    #                 'state_id': self.env['res.country.state'].search([
    #                     ('name', '=', record[3])]).id,
    #                 'country_id': self.env['res.country'].search([
    #                     ('code', '=', record[4])]).id,
    #                 'zip': record[5],
    #                 'phone': record[6],
    #                 'email': record[7],
    #                 'customer_rank': True
    #             })
    #             except:raise UserError(_('Please insert a valid file'))

    def _create_journal_entry(self, record):
        # code = int(record[0])
        # account_id = self.env['account.account'].search([('code', '=', code)], limit=1)
        # if not account_id:
        #     raise UserError(_("There is no account with code %s.") % code)
        # partner_id = self.env['res.partner'].search([('name', '=', record[2])], limit=1)
        # if not partner_id:
        #     partner_id = self.env['res.partner'].create({
        #         'name': record[1],
        #         'customer': True,
        #     })Loaded
        print('record [0]')
        print(record[0])
        print('record [1]')
        print(record[1])
        line_ids = {
            'desc': record[0],
            'price': record[1],
        }
        return line_ids

    def import_journal_entry(self):
        try:
            book = xlrd.open_workbook(filename=self.file_name)
            # book = xlrd.open_workbook(filename=BytesIO(base64.b64decode(self.file)), read_only=True)
        except FileNotFoundError:
            raise UserError('No such file or directory found. \n%s.' % self.file_name)
        except xlrd.biffh.XLRDError:
            raise UserError('Only excel files are supported.')
        for sheet in book.sheets():
            try:
                line_vals = []
                if sheet.name == 'Sheet1':
                    for row in range(sheet.nrows):
                        if row >= 1:
                            row_values = sheet.row_values(row)
                            vals = self._create_journal_entry(row_values)
                            line_vals.append((0, 0, vals))
                if line_vals:
                    for re in line_vals:
                        print(re)
                    # date = self.date
                    # ref = self.jv_ref
                    # self.env['account.move'].create({
                    #     # 'date': date,
                    #     # 'ref': ref,
                    #     # 'journal_id': self.jv_journal_id.id,
                    #     'ic_ids': line_vals
                    # })
            except IndexError:
                pass

class ImportCustomerWizard(models.Model):
    _name = "import.customer"

    desc = fields.Char()
    price = fields.Float()
    ic_id = fields.Many2one('import.customer.wizard')
    # file = fields.Binary(string="File", required=True)
