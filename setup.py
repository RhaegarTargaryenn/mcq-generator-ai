from setuptools import setup, find_packages

setup(
    name='mcqgen',
    version='0.1.0',
    author='Shubham Rana',
    author_email='shubhamrana97262@gmail.com',
    packages=find_packages(),
    install_requires=[
        'openai',  
        'langchain',
        'streamlit',        
        'PyPDF2',
        'python-dotenv'
    ]
)
