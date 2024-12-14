
# range(start, stop, step)
for i in range(0, 40, 2):  # Incrementa de 2 en 2
    print(i)
    if(i==24):
        print("Se ha salido del bucle.")
        break

# Recorrer una lista
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(f"Number: {num}")