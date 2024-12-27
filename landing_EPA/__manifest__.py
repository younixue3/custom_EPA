{
    'name': 'Landing Page',
    'version': '1.0',
    'summary': 'Landing page EPA',
    'description': 'custom web for EPA.',
    'category': 'Website',
    'author': 'Expertri.id',
    'depends': ['website', 'website_blog', 'project'],
    'data': [
         'views/assets.xml',
        
        # Template untuk landing page
        'views/landing/landing_page.xml',
        'views/landing/card_list.xml',
        'views/landing/jumbotron.xml',
        'views/landing/certi.xml',
        'views/landing/about.xml',
        'views/landing/construction.xml',
        'views/landing/testimoni.xml',
        'views/landing/contact_us.xml',
        # Template untuk form page
        'views/form/form.xml',
        'views/form/jumbotron_form.xml',
        'views/form/form_body.xml',

        # Template untuk about page
        'views/about/about.xml',
        'views/about/jumbotron_about.xml',
        'views/about/about_body.xml',

        # template lsk
        'views/legalitas/legalitas.xml',
        'views/legalitas/jumbotron_legalitas.xml',
        'views/legalitas/legalitas_body.xml',

        # template News
        'views/news/news.xml',
        'views/news/jumbotron_news.xml',
        'views/news/news_body.xml',

        # template services
        'views/servis/servis.xml',
        'views/servis/jumbotron_servis.xml',
        'views/servis/servis_body.xml',
        'views/servis/invite_us.xml',
        
        # template project
        'views/project/project.xml',
        'views/project/jumbotron_project.xml',
        'views/project/project_body.xml',

        # input project
        'views/project/project_detail/jumbotron_detail.xml',

        # template safety
        'views/safety/safety.xml',
        'views/safety/jumbotron_safety.xml',
        'views/safety/safety_body.xml',
    ],
    'qweb': [],                  # Jika ada QWeb template tambahan, masukkan di sini
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
