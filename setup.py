from setuptools import setup, find_packages

version = __import__('minitrue').__version__

setup(
    name = 'django-minitrue',
    version = version,
    description = 'Search & Replace for Django Models content',
    author = 'Jonas Obrist et al.',
    url = 'http://github.com/piquadrat/django-minitrue',
    packages = find_packages(),
    zip_safe=False,
    install_requires = ('django-load',),
    package_data={
        'mailchimp': [
            'templates/minitrue/*.html',
            'locale/*/LC_MESSAGES/django.?o',
            'static/minitrue/js/*.js'
        ],
    },
)
