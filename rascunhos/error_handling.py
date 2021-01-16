

from resources import *

row = '=' * 15


"======================================================================================================================"
string_incompatible_data = [
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '[', ']', '{', '}', '!', '?', '/', '\\', '|', '(', ')', '=', '+',
'-', '_', '¬', '~', '*', '<', '>', '^', '@', '#', '$', '%', '&', '£', '¢', ':', ';', ',', '.', "'", '"', '¨', 'º', 'ª',
'`', '´']
"======================================================================================================================"



"======================================================================================================================"
string_incompatible_data_display = \
"""0 1 2 3 4 5 6 7 8 9 ! ? = + - _ ¬ * / | ( ) [ ] { } < > ^ ~ ´ ` @ # $ % & £ ¢ : ; . , ' ¨ " º ª \\"""
"======================================================================================================================"



"======================================================================================================================"
mistake_at_float = """
    {}
    {}Allowed kind of data:{}
        {}Integers without spacing            ->{} {}1234      12345      123456      1234567{}
        {}Integers with underline             ->{} {}1_234     12_345     123_456     1_234_567{}
        {}Not integers with dot               ->{} {}1234.44   12345.55   123456.66   1234567.77{}
        {}Not integers with underline and dot ->{} {}1_234.44  12_345.55  123_456.66  1_234_567.77{}
    {}Incorrect data:{} 
        {}Not integers with dot and underline        ->{} {}1.234_44  12.345_55  123.456_66  1.234.567_77{}
        {}Numbers with letters or special characters ->{} {}1s  12/  123 dollars  1234@  12,345{}
    """.format(announcement,
               colors[4], colors[7],
               colors[0], colors[7], colors[2], colors[7],
               colors[0], colors[7], colors[2], colors[7],
               colors[0], colors[7], colors[2], colors[7],
               colors[0], colors[7], colors[2], colors[7],
               colors[1], colors[7],
               colors[0], colors[7], colors[2], colors[7],
               colors[0], colors[7], colors[2], colors[7])
"======================================================================================================================"



"======================================================================================================================"
mistake_at_integer = """
    {}
    {}Allowed type of data:{} 
        {}numbers without any spacing   ->{} {}1234  / 1234567{}
        {}numbers with an underline     ->{} {}1_234 / 1_234_567{} 
    {}Improper data:{}
        {}numbers with dot              ->{} {}1.234 / 1.234.567{}
        {}numbers with comma            ->{} {}1,234 / 1,234,567{}
        {}numbers mixed with letters    ->{} {}1234 dollars{} 
    """.format(announcement,
               colors[4], colors[7],
               colors[0], colors[7], colors[2], colors[7],
               colors[0], colors[7], colors[2], colors[7],
               colors[1], colors[7],
               colors[0], colors[7], colors[2], colors[7],
               colors[0], colors[7], colors[2], colors[7],
               colors[0], colors[7], colors[2], colors[7],)
"======================================================================================================================"



"======================================================================================================================"
mistake_at_string = \
    """
    {}
    POSSIBLE ERRORS:
    1. Names {}must not carry ->{} {}
    2. Names {}cannot be empty{}
    3. Names {}cannot be only space (void){}
    4. Names with {}two or less characters are nearly impossible{}
    5. Names which have {}no spacing between each new word are gramatically improper{}
    """.format(announcement, colors[1], colors[7], string_incompatible_data_display, colors[1], colors[7],
               colors[1], colors[7], colors[1], colors[7], colors[1], colors[7])
"======================================================================================================================"



"======================================================================================================================"
mistake_empty_input = """
    {}{} Warning {}{}
    {}You did not type something!{}""".format(row, colors[1], colors[7], row, colors[1], colors[7])
"======================================================================================================================"



"======================================================================================================================"
improbable_name_size = """
    {}{} Error found {}{}
    {}The name provided seems too short{}
    """.format(row, colors[1], colors[7], row, colors[1], colors[7])
"======================================================================================================================"



"======================================================================================================================"
error_invalid_data = """
    {}
    {}The type of input provided does not make sense in the context{}
    """.format(announcement, colors[0], colors[7])
"======================================================================================================================"
