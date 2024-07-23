from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("test.pdf")  # open input
writer = PdfWriter()  # open output

n = len(reader.pages)

for i in range(n):
    writer.add_page(reader.pages[i])  # insert page


# add a bookmark on the first page
# writer.add_outline_item("Краткое содержание", 5, parent=None)

# add a bookmark on the sixth page
par = writer.add_outline_item("Краткое содержание", 5, parent=None)

# add a child bookmark on the eighth page
writer.add_outline_item("Введение", 17, parent=par)
writer.add_outline_item("Глава 1. Объектно-ориентированное проектирование", 23, parent=par)
writer.add_outline_item("Глава 2. Объекты в Pythoп", 60, parent=par)
writer.add_outline_item("Глава 3. Когда объекты одинаковы", 110, parent=par)
writer.add_outline_item("Глава 4. Ожидаемые неожиданности", 146, parent=par)
writer.add_outline_item("Глава 5. Когда без ООП не обойтись", 184, parent=par)
writer.add_outline_item("Глава 6. Абстрактные классы и перегрузка операторов", 224, parent=par)
writer.add_outline_item("Глава 7. Структуры данных Python", 270, parent=par)
writer.add_outline_item("Глава 8. Объектно-ориентированное и функциональное программирование", 326, parent=par)
writer.add_outline_item("Глава 9. Строки, сериализация и пути к файлам", 379, parent=par)
writer.add_outline_item("Глава 10. Паттерн Итератор", 443, parent=par)
writer.add_outline_item("Глава 11. Общие паттерны проектирования", 483, parent=par)
writer.add_outline_item("Глава 12. Новые паттерны проектирования", 539, parent=par)
writer.add_outline_item("Глава 13. Тестирование объектно-ориентированных программ", 590, parent=par)
writer.add_outline_item("Глава 14. Конкурентная обработка данных", 646, parent=par)
with open("result.pdf", "wb") as fp:  # creating result pdf JCT
    writer.write(fp)  # writing to result pdf JCT

