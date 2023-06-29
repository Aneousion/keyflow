import time
import keyboard
import random
from colorama import Back, Fore, Style


class KeyFlowException(Exception):
    """
    Custom exception class for KeyFlow-related errors.
    """

    pass


def _print_formatted_text(underline=False, bold=False, italics=False, fore_color: str = None, back_color: str = None):
    if underline:
        print('\033[4m', end='', flush=True)
    if bold:
        print('\033[1m', end='', flush=True)
    if italics:
        print('\033[3m', end='', flush=True)
    if fore_color:
        print(Fore.__dict__.get(fore_color.upper(), Fore.RESET), end='', flush=True)
    if back_color:
        print(Back.__dict__.get(back_color.upper(), Back.RESET), end='', flush=True)



def kfprint(text: str, speed: float = 0.2, retype: str = None, fore_color: str = None, back_color: str = None, typing: bool = True, error: float = 0.2, underline: bool = False, bold: bool = False, italics: bool = False):
    """
    Prints the text with a simulated typing effect and supports custom foreground and background colors.

    Args:
    -
        `text` (str): The text to be printed.

        `speed` (float, optional): The typing speed in seconds per character. Default is 0.2.

        `retype` (str, optional): Text to be retyped after printing. Default is None.

        `fore_color` (str, optional): The foreground color code or name to apply to the text. Default is None.

        `back_color` (str, optional): The background color code or name to apply to the text. Default is None.

        `typing` (bool, optional): Whether to simulate typing effect. Default is True.

        `error` (float, optional): The probability of making an error while typing. Default is 0.2, that is, a 20% chance of making a mistake.

        `underline` (bool, optional): Whether to underline the text. Default is False.

        `italics` (bool, optional): Whether to italicize the text. Default is False.

        `bold` (bool, optional): Whether to bold the text. Default is False.

    Raises:
    -
        `KeyFlowException`: If any of the parameter types are incorrect or invalid color codes/names are provided.
    """
    if not isinstance(text, str):
        raise KeyFlowException("The 'text' parameter must be a string")
    if not isinstance(retype, (str, type(None))):
        raise KeyFlowException("The 'retype' parameter must be a string")
    if not isinstance(speed, float):
        raise KeyFlowException("The 'speed' parameter must be a float")
    if not isinstance(fore_color, (str, type(None))):
        raise KeyFlowException("The 'fore_color' parameter must be a string")
    if not isinstance(back_color, (str, type(None))):
        raise KeyFlowException("The 'back_color' parameter must be a string")
    if not isinstance(typing, bool):
        raise KeyFlowException("The 'typing' parameter must be a boolean")
    if not isinstance(error, float):
        raise KeyFlowException("The 'error' parameter must be a float")
    if not isinstance(underline, bool):
        raise KeyFlowException("The 'underline' parameter must be a boolean")
    if not isinstance(italics, bool):
        raise KeyFlowException("The 'italics' parameter must be a boolean")
    if not isinstance(bold, bool):
        raise KeyFlowException("The 'bold' parameter must be a boolean")

    if not typing:
        _print_formatted_text(underline=underline, bold=bold, italics=italics, fore_color=fore_color, back_color=back_color)
        print(text, end='', flush=True)
        print(Style.RESET_ALL, end='', flush=True)
        return
    stop_typing = False

    def pause_resume_typing(event):
        nonlocal stop_typing
        stop_typing = not stop_typing

    keyboard.on_press_key(key='Space', callback=pause_resume_typing)

    for char in text:
        if random.random() < error:
            mistyped_char = random.choice(text.replace('\n', ''))
            print(mistyped_char, end='', flush=True)
            time.sleep(random.uniform(0, speed))
            print('\b', end='', flush=True)

        while stop_typing:
            time.sleep(0.1)

        if char == '\n':
            print(Style.RESET_ALL, char, flush=True, end='')
            continue  

        _print_formatted_text(underline=underline, bold=bold,
                              italics=italics, fore_color=fore_color, back_color=back_color)
        print(char, end='', flush=True)
        time.sleep(speed)

    print(Style.RESET_ALL, end='', flush=True)

    keyboard.unhook_all()

    if retype:
        for _ in range(len(text)):
            print('\b \b', end='', flush=True)
            time.sleep(speed)
        kfprint(text=retype, speed=speed, fore_color=fore_color, back_color=back_color,
                error=error, underline=underline, bold=bold, italics=italics)
        return
   


def _blinking_cursor_animation():
    stop_animation = False

    def stop_animation_callback(event):
        nonlocal stop_animation
        stop_animation = True
    keyboard.on_press(callback=stop_animation_callback)
    while not stop_animation:
        print('_', end='', flush=True)
        time.sleep(1)
        print('\b', end='', flush=True)
        time.sleep(1)
    keyboard.unhook_all()


def kfinput(text: str, speed: float = 0.2, retype: str = None, fore_color: str = None, back_color: str = None, typing: bool = True, use_pyip = None, pyip_params: dict = {}, error: float = 0.2, underline: bool = False, bold: bool = False, italics: bool = False):
    """
    Displays text with a simulated typing effect and supports custom foreground and background colors.
    Waits for user input and returns the entered value.

    Args:
    -
        `text` (str): The text to be displayed as a prompt.

        `speed` (float, optional): The typing speed in seconds per character. Default is 0.2.

        `retype` (str, optional): Text to be retyped after printing. Default is None.

        `fore_color` (str, optional): The foreground color code or name to apply to the text. Default is None.

        `back_color` (str, optional): The background color code or name to apply to the text. Default is None.

        `typing` (bool, optional): Whether to simulate typing effect. Default is True.

        `use_pyip` (callable, optional): A pyinputplus function to use for input. Default is None.

        `pyip_params` (dict, optional): Additional parameters to pass to `use_pyip` function. Default is an empty dictionary.

        `error` (float, optional): The probability of making an error while typing. Default is 0.2, that is, a 20% chance of making a mistake.

        `underline` (bool, optional): Whether to underline the text. Default is False.

        `italics` (bool, optional): Whether to italicize the text. Default is False.

        `bold` (bool, optional): Whether to bold the text. Default is False

    Returns:
    -
        The value entered by the user.

    Raises:
    -
        `KeyFlowException`: If any of the parameter types are incorrect or invalid color codes/names are provided.

    """
    if not callable(use_pyip) and not isinstance(use_pyip, type(None)):
        raise KeyFlowException("The 'use_pyip' parameter must be a function")
    if not isinstance(pyip_params, dict):
        raise KeyFlowException(
            "The 'pyip_params' parameter must be a dictionary of parameters")
    if 'prompt' in pyip_params.keys():
        del pyip_params['prompt']

    kfprint(text, speed=speed, retype=retype, fore_color=fore_color,
            back_color=back_color, typing=typing, error=error, underline=underline, italics=italics, bold=bold)
    _blinking_cursor_animation()
    try:
        if use_pyip != None:
            var = use_pyip(**pyip_params)
            return var
        var = input()
        return var
    except Exception as e:
        KeyFlowException(f'Error in use_pyip() function {e}')    

