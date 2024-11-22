from odoo import http
from odoo.http import request

class LandingPageController(http.Controller):

    @http.route('/landing_page', type='http', auth='public', website=True)
    def landing_page(self, **kwargs):
        testimonials = request.env['wb.proyek'].search([], limit=3, order='create_date desc')
        
        testimonial_data = []
        for testimonial in testimonials:
            testimonial_data.append({
                'id': testimonial.id,  # Sertakan ID proyek
                'testi': testimonial.testi,
                'name_testi': testimonial.name_testi,
                'client': testimonial.client,
            })

        return request.render('landing_EPA.landing_page_template', {
            'testimonials': testimonial_data,
        })
