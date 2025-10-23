def capitalize_first_letter_list(fruits):
    """
    Return a new list where the first character of each fruit name is capitalized.
    Non-string items are returned unchanged. Empty strings are preserved.
    """
    out = []
    for f in fruits:
        if not isinstance(f, str) or f == "":
            out.append(f)
            continue
        s = f.strip()  # remove surrounding whitespace
        if s == "":
            out.append("") 
            continue
        out.append(s[:1].upper() + s[1:])
    return out

if __name__ == "__main__":
    raw = input("Enter fruits separated by commas: ")
    fruits = [item for item in raw.split(",")]
    result = capitalize_first_letter_list(fruits)
    print(result)