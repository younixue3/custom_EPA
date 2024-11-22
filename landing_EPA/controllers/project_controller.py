from odoo import http
from odoo.http import request

class ProjectPageController(http.Controller):
    # Route untuk halaman utama proyek tanpa ID
    @http.route('/project_page', type='http', auth='public', website=True)
    def project_page(self, page=1, **kwargs):
        # Mengonversi page ke integer
        page = int(page)

        # Tentukan jumlah proyek per halaman
        limit = 8
        offset = (page - 1) * limit

        # Ambil total jumlah proyek
        total_projects = request.env['wb.proyek'].sudo().search_count([])

        # Hitung total halaman
        total_pages = (total_projects + limit - 1) // limit  # Pembulatan ke atas

        # Ambil proyek berdasarkan halaman yang diminta
        projects = request.env['wb.proyek'].sudo().search([], order='create_date desc', limit=limit, offset=offset)

        # Render template dengan data proyek dan informasi pagination
        return request.render('landing_EPA.project_page_template', {
            'projects': projects,
            'current_page': page,
            'total_pages': total_pages,
        })



    @http.route('/project_page/<int:project_id>', type='http', auth='public', website=True)
    def project_detail_page(self, project_id):
        # Mencari proyek berdasarkan ID
        project = request.env['wb.proyek'].sudo().browse(project_id)

        # Cek apakah proyek ada
        if not project.exists():
            return request.redirect('/404')

        # Mengambil URL gambar utama dari ir.attachment
        main_image_url = ''
        if project.main_image:
            # Mengambil attachment gambar utama
            attachment = request.env['ir.attachment'].sudo().search([
                ('res_id', '=', project.id),
                ('res_model', '=', 'wb.proyek'),
                ('res_field', '=', 'main_image')
            ], limit=1)
            if attachment:
                main_image_url = '/web/image/{}/{}'.format(attachment.id, attachment.name)


       # Mengambil semua gambar dari relasi
        img_all = []
        additional_images = request.env['ir.attachment'].sudo().search([
            ('id', 'in', project.images.ids)
        ])

        for image in additional_images:
            img_all.append('/web/image/{}/{}'.format(image.id, image.name))

        # Mengambil dua gambar tambahan dengan ID terkecil
        limited_additional_image_urls = []
        if len(additional_images) > 0:
            # Mengambil dua ID terkecil
            smallest_image_ids = sorted(additional_images.ids)[:2]  # Ambil dua ID terkecil
            
            for image_id in smallest_image_ids:
                image = request.env['ir.attachment'].sudo().browse(image_id)
                limited_additional_image_urls.append('/web/image/{}/{}'.format(image.id, image.name))

    # Sekarang Anda bisa mengirim img_all dan limited_additional_image_urls ke template Anda


        paragraphs = project.desc.split("\n\n")  # Membagi teks berdasarkan jeda paragraf
        desc_part1 = paragraphs[0] if len(paragraphs) > 0 else ""
        desc_part2 = "\n\n".join(paragraphs[1:]) if len(paragraphs) > 1 else ""
        # Render template dengan data yang diperlukan
        return request.render('landing_EPA.jumbotron_detail', {
            'img_all': img_all,  # URL dari semua gambar yang diambil
            'limited_additional_image_urls': limited_additional_image_urls,  # Dua gambar dengan ID terkecil, jika ingin
            'main_image_url': main_image_url,  # URL gambar utama
            'name_proyek': project.name_proyek,  # Nama proyek
            'client': project.client,  # Nama klien
            'location': project.location,  # Lokasi proyek
            'process': project.process,  # Proses yang dilakukan
            'size': project.size,  # Ukuran proyek
            'years': project.years,  # Ukuran proyek
            'testi': project.testi,  # Ukuran proyek
            'name_testi': project.name_testi,  # Ukuran proyek
            'desc_part1': desc_part1,  # Deskripsi bagian 1
            'desc_part2': desc_part2,  # Deskripsi bagian 2
        })

