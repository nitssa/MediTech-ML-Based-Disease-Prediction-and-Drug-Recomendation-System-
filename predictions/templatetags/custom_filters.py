from django import template

register = template.Library()

@register.filter
def ordinal(value):
    """
    Converts a number to its ordinal representation: 1 => 1st, 2 => 2nd, 3 => 3rd, etc.
    """
    try:
        value = int(value)
        if 11 <= (value % 100) <= 13:
            suffix = "th"
        else:
            suffix = {1: "st", 2: "nd", 3: "rd"}.get(value % 10, "th")
        return f"{value}{suffix}"
    except (TypeError, ValueError):
        return value
