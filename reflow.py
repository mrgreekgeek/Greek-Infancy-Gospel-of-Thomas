import re, sys

with open(sys.argv[1], "r", encoding="utf-8") as input:
    with open(sys.argv[2], "w", encoding="utf-8") as output:
        text = input.read()

        text = re.sub(r"- \n", r"", text, flags=re.M)
        text = re.sub(r"\n", r"¶", text, flags=re.M)
        text = re.sub(r"¶¶", r"\n\n", text, flags=re.M)
        text = re.sub(r"¶", r" ", text, flags=re.M)
        text = re.sub(r"  ", r" ", text, flags=re.M)

        output.write(text)
