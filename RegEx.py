import re

txt = "The rain in Spain. Rain is good"

x = re.findall("is good",txt)

# Split by whitespace
y = re.split("\s",txt)

# Return index of matching pattern
z = re.search("ai",txt)
print(z.span())