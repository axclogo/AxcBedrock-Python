from setuptools import setup, find_packages

setup(
    name="axc-bedrock",
    version="0.1",
    packages=find_packages(),
    # Metadata
    author="AxcLogo",
    author_email="axclogo@outlook.com",
    url="https://github.com/axclogo",
    description="Just like bedrock in Minecraft, it supports upper-layer development and provides basic APIs. Unlike SwifterSwift, it uses the namespace method for calling",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license="MIT",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
)
