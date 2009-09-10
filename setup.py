from distutils.core import setup

setup(
    name='django-birdflight',
    version='0.1',
    description='A Django project to help you name your Django project after \
        a famous jazz musician, reference, slang.',
    author='Kevin Fricovsky',
    author_email='kfricovsky@gmail.com',
    license='BSD',
    url='http://github.com/montylounge/django-birdflight/tree/master',
    packages=[
        'birdflight',
    ],
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)
