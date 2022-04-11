tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def my_gen():
    _tutors = (el for el in tutors)
    _klasses = (el for el in klasses)
    for _school in zip(_klasses,
                       _tutors):
        yield _school[::-1]
    for rest in _tutors:
        yield rest, None

my_gener = my_gen()
for item in my_gener:
    print(item)

        # объединять по длинному списку

    def school():
        for item in zip_longest(tutors, klasses):
            yield item
