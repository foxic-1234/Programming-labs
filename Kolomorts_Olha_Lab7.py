print('Програмування. Частина 2. Лаботаротна робота №7, Коломоєць Ольги ФБ-44 Варіант 9')
import matplotlib.pyplot as plt

def read_sunspot_data(filename):
    months = []
    values = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:
                months.append(int(parts[0]))
                values.append(float(parts[1]))
    return months, values

def plot_all_data(months, values):
    plt.figure(figsize=(12, 5))
    plt.plot(months, values, label='Кількість затемнень')
    plt.xlabel('Місяць з січня 1749')
    plt.ylabel('Кількість затемнень')
    plt.title('Графік кількості сонячних затемнень')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_first_1000(months, values):
    plt.figure(figsize=(12, 5))
    plt.plot(months[:1000], values[:1000], label='Перші 1000 значень')
    plt.xlabel('Місяць')
    plt.ylabel('Кількість затемнень')
    plt.title('Графік для перших 1000 значень')
    plt.legend()
    plt.grid(True)
    plt.show()

def moving_average(values, r=5):
    averaged = []
    for k in range(r, len(values) - r):
        total = 0
        for m in range(-r, r + 1):
            total += values[k + m]
        averaged.append(total / (2 * r + 1))
    return averaged

def plot_moving_average(values, r=5):
    original = values[:1000]
    averaged = moving_average(original, r)
    x_original = list(range(1000))
    x_avg = list(range(r, 1000 - r))
    plt.figure(figsize=(12, 5))
    plt.plot(x_original, original, label='Початкові значення')
    plt.plot(x_avg, averaged, label=f'Ковзаюче середнє (r={r})', color='red')
    plt.xlabel('Місяць')
    plt.ylabel('Кількість затемнень')
    plt.title('Порівняння: Початкові дані та ковзаюче середнє')
    plt.legend()
    plt.grid(True)
    plt.show()

filename = 'sunspots.txt'
months, values = read_sunspot_data(filename)

plot_all_data(months, values)
plot_first_1000(months, values)
plot_moving_average(values, r=5)
