from setuptools import find_packages, setup

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->list[str]:
    '''
    This function will return the list of requirements mentioned in the requirement.txt file
    '''

    requirements = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for raw_line in f:
            req = raw_line.strip()

            # Skip blank lines, comments, editable installs, and pip options.
            if not req or req.startswith('#'):
                continue
            if req == HYPHEN_E_DOT or req.startswith('-e ') or req.startswith('--'):
                continue

            requirements.append(req)

    return requirements

setup(
    name = "mlops",
    version = "0.0.1",
    author = "Shreyas",
    author_email="mshreyas762@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements('requirements.txt')
)