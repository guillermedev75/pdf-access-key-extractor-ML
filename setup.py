from setuptools import setup, find_packages

setup(
    name='ml_access_key_extractor',
    version='0.0.1',
    license='MIT License',
    author='Guillerme Rezende Manhaes',
    keywords='nota_fiscal',
    description=u'Lib to access nf from Jira',
    packages=find_packages(),
    package_data={'access_key_extractor': ['*']},
    include_package_data=True,
    install_requires=[
        'pdfplumber',
        'scikit-learn>=0.24.0'  # Certifique-se de ajustar a versão conforme necessário
    ],
)
