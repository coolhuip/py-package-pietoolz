from subprocess import run

# Build the distribution
run(['python', 'setup.py', 'sdist', 'bdist_wheel'])

# Upload to PyPI
run(['twine', 'upload', 'dist/*'])
