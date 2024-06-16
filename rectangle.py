def perimeter(length, breadth):
  return 2 * (length + breadth)

def area(length, breadth):
  return length * breadth

l = input('enter length: ')
b = input('enter breadth: ')

print(perimeter(l, b))
print(area(l, b))