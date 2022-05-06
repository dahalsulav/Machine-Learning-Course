def student_result(student_names: list, student_percents: list) -> dict:
    """This function takes two lists (i.e. student_names and 
    student_percents) as arguments, uniquely filter student_names as 
    well as student_percents greater than 50 and returns the dictionary 
    with key as student_name and value as student_percent

    Args:
        student_names (list): list of student names
        student_percents (list): list of student percents

    Returns:
        dict: dictionary of student_name and student_percent
         in a key: value pair
    """
    unique_students = []
    [unique_students.append(name)
     for name in student_names if name not in unique_students]
    percent_greater_than_50 = [
        percent for percent in student_percents if percent > 50]
    student_res = student_res = {student[0]: student[1]
                                 for student in zip(unique_students, percent_greater_than_50)}
    return student_res


student_names = ['ram', 'shyam', 'hari',
                 'sita', 'ram']  # list of student names
student_percents = [21, 22, 33, 44, 55, 66]  # list of student percents
# student_result function call
print(student_result(student_names, student_percents))
