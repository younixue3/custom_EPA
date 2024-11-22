from odoo import http
from odoo.http import request

class ServicesPageController(http.Controller):
    @http.route('/safety_page', type='http', auth='public', website=True)
    def safety_page(self, **kwargs):
        # Render the form page template
        return request.render('landing_EPA.safety_page_template', {})