count = 0

def is_triangle(a, b, c):
	return a + b > c and a + c > b and b + c > a

with open("day3.input") as f:
	lines = f.readlines()

#	for line in lines:
#		a, b, c = line.strip().split()	
#		a = int(a)
#		b = int(b)
#		c = int(c)

	for i in range(len(lines) / 3):
		line1 = lines[3*i].strip().split()
		line2 = lines[3*i+1].strip().split()
		line3 = lines[3*i+2].strip().split()

		line1a = int(line1[0])
		line1b = int(line1[1])
		line1c = int(line1[2])
		line2a = int(line2[0])
		line2b = int(line2[1])
		line2c = int(line2[2])
		line3a = int(line3[0])
		line3b = int(line3[1])
		line3c = int(line3[2])

		if is_triangle(line1a, line2a, line3a):
			count += 1
		if is_triangle(line1b, line2b, line3b):
			count += 1
		if is_triangle(line1c, line2c, line3c):
			count += 1

print count
