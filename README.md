# KeyFlow

KeyFlow is a Python library that provides interactive console printing with a simulated typing effect and customizable text formatting. It allows you to create dynamic and engaging command-line interfaces for your Python applications.

## Features

- Simulated typing effect: Display text with a realistic typing animation.
- Customizable formatting: Apply foreground and background colors, underline, bold, and italics to your printed text.
- Error simulation: Introduce random typing errors to make the output more human-like.
- Prompt input: Display prompts and wait for user input with support for various input validation options.
- Integration with PyInputPlus: Option to use PyInputPlus functions for input handling.
- Easy-to-use API: Simple and intuitive functions for printing and input.


## Installation

You can install KeyFlow using pip:

```shell
pip install keyflow
```
## Usage

Here's an example of how to use KeyFlow to print formatted text and receive user input:
```python
from keyflow import kfprint, kfinput

kfprint("Hello, World!", fore_color="red", back_color="yellow", underline=True, bold=True)
name = kfinput('What is your name?\n', fore_color='green', underline=True)
kfprint(f'Thanks for using KeyFlow, {name}.')
```


## License

KeyFlow is released under the [MIT License](https://opensource.org/licenses/MIT). You are free to use, modify, and distribute this library for both commercial and non-commercial purposes. Please see the [LICENSE](https://github.com/aneousion/keyflow/LICENSE) file for more details.

## GitHub Repository

The source code for KeyFlow is hosted on GitHub. You can find the repository at [https://github.com/aneousion/keyflow](https://github.com/aneousion/keyflow). Feel free to explore the repository, submit issues, and contribute to the project.

To clone the repository, run the following command:

```bash
git clone https://github.com/aneousion/keyflow.git
```
