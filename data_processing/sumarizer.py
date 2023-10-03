
def make_summary(homework_list):
    index = 0
    for item in homework_list:
        index += 1
        info = item.get_all()
        print(f"{index}. Name: {info['name']}\nCourse: {info['course']}\nDue: {info['due_date']}\n")
