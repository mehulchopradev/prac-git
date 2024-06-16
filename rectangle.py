def perimeter_rectangle(length, breadth=2):
  return 2 * (length + breadth)

def area(length, breadth):
  return length * breadth

l = input('enter length: ')
b = input('enter breadth: ')

print(perimeter_rectangle(l, b))
print(area(l, b))