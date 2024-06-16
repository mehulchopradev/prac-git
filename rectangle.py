def perimeter_rectangle(length, breadth):
  # deliberately adding this wrong formula
  return 3 * (length + breadth)

def area(length, breadth):
  return length * breadth

l = input('enter length: ')
b = input('enter breadth: ')

print(perimeter_rectangle(l, b))
print(area(l, b))