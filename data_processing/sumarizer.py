
def make_summary(homework_list):
    for item in homework_list:
        info = item.get_all()
        print(f"Name: {info['name']}\nCourse: {info['course']}\n")
