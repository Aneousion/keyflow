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

### kfprint

The `kfprint` function prints text with a simulated typing effect and supports custom foreground and background colors.

```python
from keyflow.keyflow import kfprint

kfprint(text, speed=0.2, retype=None, fore_color=None, back_color=None, typing=True, error=0.2, underline=False, bold=False, italics=False)
```

#### Parameters

- `text` (str): The text to be printed.
- `speed` (float, optional): The typing speed in seconds per character. Default is 0.2.
- `retype` (str, optional): Text to be retyped after printing. Default is None.
- `fore_color` (str, optional): The foreground color code or name to apply to the text. Default is None.
- `back_color` (str, optional): The background color code or name to apply to the text. Default is None.
- `typing` (bool, optional): Whether to simulate typing effect. Default is True.
- `error` (float, optional): The probability of making an error while typing. Default is 0.2.
- `underline` (bool, optional): Whether to underline the text. Default is False.
- `bold` (bool, optional): Whether to bold the text. Default is False.
- `italics` (bool, optional): Whether to italicize the text. Default is False.

### kfinput

The `kfinput` function displays text with a simulated typing effect, waits for user input, and returns the entered value.

```python
from keyflow.keyflow import kfinput

kfinput(text, speed=0.2, retype=None, fore_color=None, back_color=None, typing=True, use_pyip=None, pyip_params={}, error=0.2, underline=False, bold=False, italics=False)
```

#### Parameters

- `text` (str): The text to be displayed as a prompt.
- `speed` (float, optional): The typing speed in seconds per character. Default is 0.2.
- `retype` (str, optional): Text to be retyped after printing. Default is None.
- `fore_color` (str, optional): The foreground color code or name to apply to the text. Default is None.
- `back_color` (str, optional): The background color code or name to apply to the text. Default is None.
- `typing` (bool, optional): Whether to simulate typing effect. Default is True.
- `use_pyip` (callable, optional): A function to use for input. Default is None.
- `pyip_params` (dict, optional): Additional parameters to pass to the `use_pyip` function. Default is an empty dictionary.
- `error` (float, optional): The probability of making an error while typing. Default is 0.2.
- `underline` (bool, optional): Whether to underline the text. Default is False.
- `bold` (bool, optional): Whether to bold the text. Default is False.
- `italics` (bool, optional): Whether to italicize the text. Default is False.


# Note: When typing, you can press the spacebar to pause and resume the typing animation.


## License

KeyFlow is released under the [MIT License](https://opensource.org/licenses/MIT). You are free to use, modify, and distribute this library for both commercial and non-commercial purposes. Please see the [LICENSE](https://github.com/aneousion/keyflow/LICENSE) file for more details.

## GitHub Repository

The source code for KeyFlow is hosted on GitHub. You can find the repository at [https://github.com/aneousion/keyflow](https://github.com/aneousion/keyflow). Feel free to explore the repository, submit issues, and contribute to the project.

To clone the repository, run the following command:

```bash
git clone https://github.com/aneousion/keyflow
```
