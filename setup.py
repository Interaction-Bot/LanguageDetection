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
    version='0.0.9',
    long_description=readme(),
    long_description_content_type='text/markdown',
    install_requires=[
        'fasttext-wheel',
        'emoji',
        'lingua-language-detector==1.3.1'
    ],
    keywords = ["language", "detection", "nlp", "identification", "short"],
    include_package_data=True,
    package_data={
        'ShortLanguageDetection.DictDetector': ['*'],
        'ShortLanguageDetection.DictDetector.dict': ['*'],
        'ShortLanguageDetection.models': ['*'],
   },
)
