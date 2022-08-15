import setuptools

setuptools.setup(
    name="PassGen",
    version="2.0.1",
    long_description=open("README.md").read(),
    license=open("LICENSE.md").read(),
    entry_points={"console_scripts": ["passgen=PassGen.cli:cli"]},
)
