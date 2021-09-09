subjects = ['Svenska', 'Engelska', 'Matematik', 'Programmering', 'Datorkunskap']
grades = {"ig": 0, "g": 1, "vg": 3, "mvg": 5}
studentyeargrades = []

def gradingyear():
    points = 0
    for subject in subjects:
        print(f'Grading system: IG- {grades["ig"]}, G- {grades["g"]}, VG- {grades["vg"]}, MVG- {grades["mvg"]}')
        while True:
            try:
                points += grades[input(f'Grade {subject}: \n').lower()]
                break
            except:
                print('Invalid Input')
    else:
        if points / len(subjects) < 1:
            return None
        elif points / len(subjects) >= 5:
            print('Student got a star medal, full score')
            return points / len(subjects)
        else:
            print(f'Students average points are: {points / len(subjects)}')
            return points / len(subjects)


def yearpass():
    for year in range(3):
        while True:
            if gradingyear() is not None:
                print(f'Student passes the {year + 1} year')
                studentyeargrades.append(gradingyear())
                break
            else:
                print(f'Student need to redo {year + 1} grades!')
    else:
        print(f'The student graduated with the avarage of each year {studentyeargrades}')


if __name__ == '__main__':
    yearpass()
