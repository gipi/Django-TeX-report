from setuptools import setup

setup(
    name = "django-tex-report",
    version = "0.1",
    #url = 'http://github.com/jacobian/django-shorturls',
    license = 'BSD',
    description = "PDF report for human being.",
    author = 'Gianluca Pacchiella',
    packages = [
        'tex_report',
        'tex_report.management',
        'tex_report.management.commands',
    ],
    install_requires = ['setuptools', 'envoy',],
)
