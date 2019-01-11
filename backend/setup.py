from setuptools import find_packages, setup

setup(
    name='codeforpoznan.pl',
    version='3.0',
    packages=find_packages(),
    install_requires=[
        'Flask==1.0.2',
        'Flask-SQLAlchemy==2.3.1',
        'Flask-Migrate==2.3.0',
        'psycopg2==2.7.6',
        'Flask-Mail==0.9.1',
        'marshmallow==3.0.0rc1',
        'flask-cors==3.0.7',
        'pytest==4.1.0',
    ],
)
