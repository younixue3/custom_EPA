from odoo import models, fields

class Proyek(models.Model):
    _name = "wb.proyek"
    _description = "Deskripsi Proyek"

    name_proyek = fields.Char("Nama Proyek")
    client = fields.Char("Nama Klien")
    location = fields.Char("Lokasi Proyek")
    process = fields.Char("Proses yang Dilakukan dalam Proyek")
    size = fields.Integer("Ukuran Proyek (m2)")
    years = fields.Char("Tahun Pengerjaan Proyek")
    desc = fields.Text("Deskripsi Proyek")
    testi = fields.Char("Testimoni Tentang Hasil Proyek")
    name_testi = fields.Char("Nama Pemberi Testimoni")
    main_image = fields.Image("Gambar Utama Proyek")  # Gambar utama disimpan sebagai Binary
    images = fields.Many2many(
        "ir.attachment", 
        string="Gambar Proyek",
        help="Upload beberapa gambar terkait proyek"
    )
    