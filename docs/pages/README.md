# PyTrinamic GitHub Pages

This directory contains the sources for the online documentation at [https://analogdevicesinc.github.io/PyTrinamic](https://analogdevicesinc.github.io/PyTrinamic)

## How to build the website locally

In order to build the website locally follow these steps:

* Install the required Python packages into your Python interpreter, with the following command, being in the `pages` directory: `python -m pip install -r requirements.txt`.
* Building the website is then done via command `make html`.
* Now the websites content is available in directory `./build/html`.
* On windows you can view the website in your default browser calling `start ./build/html/index.html`.

## Technology

The text-basis for the documentation is written in markdown and parsed by the [MyST parser](https://myst-parser.readthedocs.io/). The documentation of the syntax can be found [here](https://myst-parser.readthedocs.io/en/latest/syntax/typography.html#syntax-core)
The markdown code is located inside the `source` directory, where the main entry point is the `index.md`.