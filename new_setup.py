try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requirements = [
    'rq'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='simple_scheduler',
    version='0.1.0',
    description='simple_scheduler is a wrapper for RQ',
    author='Eric Schles',
    author_email='eric.schles@gsa.gov',
    url='https://github.com/EricSchles/simple_rq_scheduler',
    packages=[
        'simple_scheduler',
    ],
    package_dir={'simple_scheduler':
                 'simple_scheduler'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='rq scheduler',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
