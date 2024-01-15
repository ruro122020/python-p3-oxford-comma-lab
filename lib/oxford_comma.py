def oxford_comma(items):
  if len(items) <= 1:
    return ''.join(items)
  elif len(items) == 2:
    return ' and '.join(items)
  else:
    first_half = ', '.join(items[0: len(items) - 1])
    return f"{first_half}, and {items[-1]}"
 