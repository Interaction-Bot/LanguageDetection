from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='ShortLanguageDetection',
    description = 'A language detector for short string or chat.',
    url='https://github.com/Interaction-Bot/LanguageDetection/',
    author='Jourdelune',
    license='MIT',
    version='0.0.4',
    long_description=readme(),
    install_requires=[
        'fasttext',
        'emoji',
        'lingua-language-detector'
    ],
    keywords = ["language", "detection", "nlp", "identification"],
    include_package_data=True,
)