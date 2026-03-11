from setuptools import setup, find_packages

setup(
        name="cli_tool", 
        version="0.1.0", 
        packages=find_packages(where="src"), 
        package_dir={"": "src"},
        install_requires=['typer'],
        entry_points={
            "console_scripts": [
                "cli-tool=cli_tool:main", 
                ],
            },
        python_requires=">=3.10", 
        )
