def reverse_string(a_string: str):
  """Take the input a_string and return it reversed (e.g. "hello" becomes
  "olleh"."""
  reversed_string = ""
  for i in range(len(a_string)):
    reversed_string += a_string[-i]
  return reversed_string
