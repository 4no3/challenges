import re

txt = "The fhost that says boo haunts the loo"
m = re.findall(".oo", txt, re.IGNORECASE)
print(m)
