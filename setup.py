from setuptools import setup, Extension


long_description = open("README.md", "r").read()


setup(
    name="isiterable",
    description=(
        "Module that provides the isiterable function to check if an object is"
        " iterable quickly for code in production."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="1.0.post1",
    author="CosmicLivest",
    author_email="ezequielfx15@gmail.com",
    license="Unlicense License",
    keywoards="isiterable checks if an object is iterable",
    project_urls={
        "Source": "https://github.com/CosmicLivest/isiterable",
        "Tracker": "https://github.com/CosmicLivest/isiterable/issues",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "Programming Language :: C",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    url="https://github.com/CosmicLivest/isiterable",
    ext_modules=[
        Extension(
            "isiterable",
            sources=[
                "isiterable.c",
            ],
        ),
    ],
)
