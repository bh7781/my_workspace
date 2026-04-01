def get_valid_input(prompt, valid_choices=None, cast_type=str):
    """
    Ask the user for input until they enter a valid response.

    The function shows a prompt and waits for the user to type something.
    If valid_choices is given, the input must match one of those values.
    The input is converted to the given type before validation.

    Args:
        prompt (str): The message shown to the user.
        valid_choices (iterable, optional): Allowed values (any datatype).
        cast_type (type, optional): Function to convert input (e.g., int, float, str).

    Returns:
        The validated user input in the specified datatype.

    Notes:
        - Keeps asking until valid input is entered.
        - Handles invalid type conversion safely.
        - Prints "Invalid response." for wrong input.
    """

    # Convert valid_choices to a set for faster lookup (if provided)
    if valid_choices is not None:
        valid_choices = set(valid_choices)

    while True:
        # Take raw input from user
        user_input = input(prompt)

        try:
            # Convert input to desired type
            converted_input = cast_type(user_input.strip())

            # If no valid choices, accept anything
            # OR if input matches allowed values, return it
            if valid_choices is None or converted_input in valid_choices:
                return converted_input
            else:
                print("Invalid response.")

        except ValueError:
            # Handles cases where conversion fails (e.g., int("abc"))
            print("Invalid response.")