from setuptools import setup

setup(
    name="cyberbrain",
    version="1.0.0",
    py_modules=["cyberbrain"],
    install_requires=[
        "torch",
        "transformers",
        "accelerate",
        "huggingface_hub"
    ],
    entry_points={
        "console_scripts": [
            "cyberbrain=cyberbrain:main",
        ],
    },
)