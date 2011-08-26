import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-portfolio',
    version='0.1.0',
    description='A reusable portfolio management project.',
    long_description=read('README.markdown'),
    url='http://github.com/ktonon/django-portfolio/',
    keywords = ['django', 'portfolio', 'project', 'resume'],
    packages=[
        'portfolio',
        'portfolio.templatetags',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
)
