import pytest

from main import get_courses_list, get_direction_dict, get_course, get_connection, get_min_duration


@pytest.mark.parametrize(
    "courses, mentors, duration, result_courses_list, result_courses_dict, result_task1, result_task2, result_task3", [
        (
                ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
                 "Frontend-разработчик с нуля"],
                [
                    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков"],
                    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин"],
                    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов"],
                    ["Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
                ],
                [14, 20, 12, 20],
                [{'duration': 14,
                  'mentors': ['Филипп Воронов', 'Анна Юшина', 'Иван Бочаров', 'Анатолий Корсаков'],
                  'title': 'Java-разработчик с нуля'},
                 {'duration': 20,
                  'mentors': ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин"],
                  'title': "Fullstack-разработчик на Python"},
                 {'duration': 12,
                  'mentors': ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов"],
                  'title': "Python-разработчик с нуля"},
                 {'duration': 20,
                  'mentors': ["Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"],
                  'title': "Frontend-разработчик с нуля"}],
                {12: [2], 14: [0], 20: [1, 3]},
                ['Python-разработчик с нуля - 12 месяцев', 'Java-разработчик с нуля - 14 месяцев',
                 'Fullstack-разработчик на Python - 20 месяцев', 'Frontend-разработчик с нуля - 20 месяцев'],
                'Связи нет',
                'Самый короткий курс(ы): Python-разработчик с нуля - 12 месяца(ев)'
        )
    ]
)
def test_list(courses, mentors, duration, result_courses_list,
              result_courses_dict, result_task1, result_task2, result_task3):
    courses_list = get_courses_list(courses, mentors, duration)
    assert courses_list == result_courses_list
    durations_dict = get_direction_dict(courses_list)
    assert durations_dict == result_courses_dict
    result = get_course(durations_dict, courses_list)
    assert result == result_task1
    assert get_connection(courses_list) == result_task2
    assert get_min_duration(duration, courses_list) == result_task3
