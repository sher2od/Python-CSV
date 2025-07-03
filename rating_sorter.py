import csv
from pprint import pprint

# CSV faylni o'qish va eng yuqori ball bo'yicha saralash
with open('students.csv') as f:
    reader = csv.reader(f)
    next(reader)  # sarlavhani tashlab o'tamiz

    max_score = sorted(
        reader,
        key=lambda n: int(n[1]),
        reverse=True  # ball bo‘yicha kamayish tartibida
    )


# Yangi CSV faylga yozish
with open('rating.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(['rank', 'name', 'score'])  # sarlavha

    for i, row in enumerate(max_score, start=1):
        writer.writerow([i] + row)  # yangi tartib bilan yozamiz























