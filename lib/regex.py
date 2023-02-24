import re


my_pattern = r"[A-Z].*today.*"
my_regex = re.compile(my_pattern)



# [A-Z] => first letter is one of A-Z
# . => any character (except for line terminators)
# * => the previous token between zero and unlimited times, as many times as possible, giving back as needed (greedy)
# today => the characters today literally (case sensitive)
# . => any character (except for line terminators)
# * => the previous token between zero and unlimited times, as many times as possible, giving back as needed (greedy)
