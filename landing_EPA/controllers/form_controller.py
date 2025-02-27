from odoo import http
from odoo.http import request
import base64
from odoo.exceptions import ValidationError

class FormPageController(http.Controller):

    @http.route('/form_page', type='http', auth='public', website=True)
    def form_page(self, **kwargs):
        error = kwargs.get('error')
        return request.render('landing_EPA.form_page_template', {'error': error})
    
    @http.route('/form/submit', type='http', auth='public', website=True, methods=['POST'], csrf=True)
    def submit_form(self, **post):
        # Ambil data dari form
        lead_title = post.get('lead_title', '')
        name = post.get('name', '')
        company_name = post.get('company_name', '')
        email = post.get('email', '')
        phone = post.get('phone', '')
        description = post.get('description', '')
        attachment_file = request.httprequest.files.get('attachment')

        # Validasi field wajib
        if not (lead_title and name and email):
            error = "Lead Title, Name, and Email are required."
            return request.redirect(f"/form_page?error={error}")

        try:
            # Dapatkan team_id dari Sales Team yang valid
            team = request.env['crm.team'].sudo().search([], limit=1)
            if not team:
                raise ValidationError("No Sales Team found. Please create one in Settings.")

            lead_values = {
                'name': lead_title,
                'contact_name': name,
                'email_from': email,
                'phone': phone,
                'description': description,
                'partner_name': company_name,
                'team_id': team.id,
                'type': 'lead'  # Field wajib
            }

            # Buat lead dengan sudo()
            lead = request.env['crm.lead'].sudo().create(lead_values)

            # Proses attachment
            if attachment_file:
                attachment_data = attachment_file.read()
                attachment_base64 = base64.b64encode(attachment_data).decode('utf-8')
                attachment = request.env['ir.attachment'].sudo().create({
                    'name': attachment_file.filename,
                    'type': 'binary',
                    'datas': attachment_base64,
                    'res_model': 'crm.lead',
                    'res_id': lead.id,
                    'mimetype': attachment_file.mimetype,
                })
                lead.message_post(body="Attachment added", attachment_ids=[attachment.id])

            return request.redirect('/form_page')

        except Exception as e:
            error = f"Error: {str(e)}"
            return request.redirect(f"/form_page?error={error}")