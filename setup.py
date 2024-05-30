# just to install my packages in my local virtual environment

from setuptools import find_packages,setup

setup(
name="medical_llm_app",
version="0.0.1",
author="Saurabh",
author_email = 'smishra.cs@gmail.com',
packages = find_packages(),
install_requires = ['openai', 'streamlit', 'python-dotenv']
)