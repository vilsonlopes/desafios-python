import time

x = [5, 6, -15, 2, 4, -1, 12, -8]
# x = list(range(1000))

# start = time.perf_counter()
# min_value = float('-inf')

# for i in range(len(x)):
#     for j in range(i, len(x)):
#         soma = 0
#         for k in range(i, j+1):
#             soma += x[k]

#         if soma > min_value:
#             min_value = soma

# end = time.perf_counter()

# tempo = end - start

# print(min_value)
# print(tempo)


start = time.perf_counter()

max_soma = 0
soma = 0

for i in range(1, len(x)):
    if soma + x[i] > x[i]:
        soma += x[i]
    else:
        soma = x[i]

    if soma > max_soma:
        max_soma = soma

print(max_soma)

end = time.perf_counter()

print(end - start)
