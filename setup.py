from setuptools import setup, find_packages

setup(
    name='ml_access_key_extractor',
    version='0.0.2',
    license='MIT License',
    author='Guillerme Rezende Manhaes',
    keywords='nota_fiscal',
    description=u'Biblioteca para extrair chave de acesso na nota fiscal em PDF',
    packages=find_packages(),
    package_data={'access_key_extractor': ['*']},
    include_package_data=True,
    install_requires=[
        'pdfplumber',
        'scikit-learn>=0.24.0'
    ],
)
