from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
VERSION = '0.1.dev1'

REQUIRED_PACKAGES = [
    'numpy==1.19.5', 'scikit-learn==0.24.2', 'google-cloud-storage==1.44.0',
    'flask==2.0.3', 'gunicorn==20.1.0', 'xgboost==1.5.2'
]

setup(
    name='prop-predict',
    version=VERSION,
    author='Simeon Thomas',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/olaoluthomas/prop_predictor",
    project_urls={
        "Project": "",
        "Bug Tracker": "https://github.com/olaoluthomas/prop_predictor/issues",
    },
    license="Apache2",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=REQUIRED_PACKAGES,
    zip_safe=True)