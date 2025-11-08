"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    redondeados = []
    for nota in student_scores:
        redondeado = round(nota)
        # Usamos append porque 'redondeado' solo guarda un valor por vez;
        # así acumulamos todos los resultados en una lista para devolverlos al final
        redondeados.append(redondeado)
    return redondeados

def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    reprobados = []
    for nota in student_scores:
        if nota <= 40:
            reprobados.append(nota)
    return len(reprobados)



def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    mejores = []
    for nota in student_scores:
        if nota >= threshold:
            mejores.append(nota)
    return mejores



def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    contador = round((highest - 40) / 4) 
    grados = []
    for numero in range(41, highest, contador):
        grados.append(numero)
    return grados




def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    contador = []
    ranking = []
    cantidad = len(student_names)
    for numero in range(1 , cantidad+1):
        contador.append(numero)
    for indice, nombre in enumerate(student_names):
        ranking.append(f"{contador[indice]}. {nombre}: {student_scores[indice]}")
    return ranking



def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    for estudiante in student_info:
        if estudiante[1] == 100:
            return estudiante
            break
    else:
            student_info.clear()
            return student_info
