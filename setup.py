import setuptools

setuptools.setup(
    name='coffeafrag',
    version='0.0.0',
    description='Coffea based b-fragmentation analyzer',
    packages=setuptools.find_packages(),
    # Include data files (Note: "include_package_data=True" does not seem to work)
    package_data={
        "coffeafrag" : [
        ],
    }
)

