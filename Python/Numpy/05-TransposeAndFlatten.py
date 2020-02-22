import numpy

N, M = map(int, input().split())
lines = []
for n in range(int(N)):
    lines.append(input().split())

array = numpy.reshape(numpy.array(lines, int), (N, M))

print(numpy.transpose(array))
print(array.flatten())
