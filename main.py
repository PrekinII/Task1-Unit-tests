# -*- coding: windows-1251 -*-

from pprint import pprint

courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
           "Frontend-разработчик с нуля"]
mentors = [
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков",
     "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев",
     "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов",
     "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов",
     "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев",
     "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин",
     "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский",
     "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин",
     "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер",
     "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая",
     "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]

durations = [14, 20, 12, 20]


def get_courses_list(courses_l, mentors_l, durations_l):
    courses_list = []
    for course, mentor, duration in zip(courses_l, mentors_l, durations_l):
        course_dict = {"title": course, "mentors": mentor, "duration": duration}
        courses_list.append(course_dict)
    pprint(courses_list)
    return courses_list


def get_direction_dict(courses_list):  # Task1 Упорядочиваем курсы
    durations_dict = {}
    for id, course in enumerate(courses_list):
        key = courses_list[id]["duration"]
        if key in durations_dict.keys():
            durations_dict[key].append(id)
        else:
            durations_dict[key] = [id]
    durations_dict = dict(sorted(durations_dict.items()))
    pprint(durations_dict)
    return durations_dict


def get_course(durations_dict, courses_list):
    x = []
    for key, id in durations_dict.items():

        for i in id:
            course = courses_list[i]["title"]
            a = f'{course} - {key} месяцев'
            x.append(a)
    print(x)
    return x


def get_connection(courses_list):  # Task2 Есть ли связь
    duration_index = []
    mcount_index = []
    for index, course in enumerate(courses_list):
        duration_index.append([course["duration"], index])
        mcount_index.append([len(course["mentors"]), index])

    duration_index.sort()
    mcount_index.sort()

    indexes_d = []
    indexes_m = []

    for dc, di in duration_index:
        indexes_d.append(di)

    for mc, mi in mcount_index:
        indexes_m.append(mi)
    return "Связь есть" if indexes_d == indexes_m else "Связи нет"


def get_min_duration(durations, courses_list):  # Task3 Самый короткий курс
    global min, max
    min_d = min(durations)
    max_d = max(durations)

    maxes = []
    minis = []
    for i, duration in enumerate(durations):
        if duration == max_d:
            maxes.append(i)
        elif duration == min_d:
            minis.append(i)

    courses_min = []
    courses_max = []
    for id in minis:
        courses_min.append(courses_list[id]["title"])
    for id in maxes:
        courses_max.append(courses_list[id]["title"])
    # print(f'Самый короткий курс(ы): {", ".join(courses_min)} - {min} месяца(ев)')
    return f'Самый короткий курс(ы): {", ".join(courses_min)} - {min_d} месяца(ев)'


if __name__ == '__main__':
    courses_list = get_courses_list(courses, mentors, durations)

    durations_dict = get_direction_dict(courses_list)

    result = get_course(durations_dict, courses_list)

    print(get_connection(courses_list))
    print(get_min_duration(durations, courses_list))
