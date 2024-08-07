import setuptools # Import the setuptools package for packaging Python projects

# Read the long description from the README.md file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Define the package version
__version__ = "0.0.0"

# Define repository and author information
REPO_NAME = "Chest-Cancer-Classification"
AUTHOR_USER_NAME = "Jesteban247"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "jesteban.castiblanco@outlook.com"

# Call the setup function from setuptools to set up the package
setuptools.setup(
    name=SRC_REPO,  # Name of the package
    version=__version__,  # Version of the package
    author=AUTHOR_USER_NAME,  # Author's name
    author_email=AUTHOR_EMAIL,  # Author's email
    description="A small python package for CNN app",  # Short description of the package
    long_description=long_description,  # Long description read from README.md
    long_description_content_type="text/markdown",  # Type of the long description content
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # URL of the package repository
    project_urls={  # Additional URLs related to the project
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},  # Root directory for the package source
    packages=setuptools.find_packages(where="src")  # Automatically find packages in the specified directory
)