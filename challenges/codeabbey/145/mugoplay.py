"""Modular Exponentiation """


def modulus_calculation(bin_ex_1, fst_modulus_1, input_vector_1):
    """Calculo del modulo"""
    counter_1 = 1
    len_bin_1 = len(bin_ex_1)

    while counter_1 < len_bin_1:
        if bin_ex_1[counter_1] == "1":
            fst_modulus_1 = (
                (fst_modulus_1**2)*(int(input_vector_1[0]))) % int(input_vector_1[2])
        else:
            fst_modulus = ((fst_modulus_1)**2) % int(input_vector_1[2])
        counter_1 += 1

    return fst_modulus_1


def create_members(file):
    """Creando miembros de la ecuacion"""
    with open(file, "r") as input_list:
        for lst in input_list.readlines():
            lst = lst.strip()
            input_vector = lst.split(" ")
            bin_ex = format(int(input_vector[1]), "b")
            fst_modulus = (
                (1**2)*(int(input_vector[0]))) % int(input_vector[2])
            modulus_result = modulus_calculation(
                bin_ex, fst_modulus, input_vector)

            print modulus_result


create_members("DATA.txt")
