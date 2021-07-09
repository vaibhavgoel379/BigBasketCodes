import re
 
# opening and reading the file
file1 = open('/home/vaibhav/Desktop/ip', 'r')
fstring = file1.readlines()
 
# declaring the regex pattern for IP addresses
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?:/\d{1,2})?)')
 
s=""
count=0

# extracting the CIDR IP addresses
for line in fstring:
	if line is not None:
   		if (pattern.search(line)) is not None:
   			s=s+pattern.search(line)[0]+","
   			count+=1
print(s[:-1])
print(count)
