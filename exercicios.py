# 1. Calcular Média de Valores em uma Lista
from typing import List
def calc_mean_values(numbers_list: List[float]) -> float:
    mean_value = round(sum(numbers_list) / len(numbers_list), 2)
    return mean_value

lst = [4,4,4,4]
print(calc_mean_values(lst))

# 2. Filtrar Dados Acima de um Limite
def filter_values_above_limit(list_to_be_filtered: List[float], limit: float) -> List[float]:
    filtered_list = [x for x in list_to_be_filtered if x < limit]
    return filtered_list

lst = [1,2,3,4,5,6,7,8]
print(filter_values_above_limit(lst, 5))

# 3. Contar Valores Únicos em uma Lista
from typing import Dict
def count_unique_values(list_to_count: List[int]) -> Dict:
    dict_count = {}
    for number in list_to_count:
        dict_count[number] = dict_count.get(number,0) + 1
    return dict_count
    
lst = [2,4,5,6,6,6,6,6,6,7,8,9,8,8,8,8,7,6,5,34,3,3,3]
print(count_unique_values(lst))

#  4. Converter Celsius para Fahrenheit em uma Lista
def convert_celsius_to_fahrenheit(list_celsius: List[float]) -> List[float]:
    list_fahrenheit = [(temp * (9/5) + 32) for temp in list_celsius]
    return list_fahrenheit

list_celsius = [0, -10, 14, 25, 32, 38, 45, 100]
print(convert_celsius_to_fahrenheit(list_celsius))

# 5. Calcular Desvio Padrão de uma Lista
def calc_standard_deviation(list_to_calc: List[float]) -> float:
    mean_list = sum(list_to_calc) / len(list_to_calc)
    std = (sum([(x - mean_list)**2 for x in list_to_calc]) / len(list_to_calc))**(1/2)
    return std

list_std = [2,3,4,5]
print(calc_standard_deviation(list_std))

# 6. Encontrar Valores Ausentes em uma Sequência
# Oficial:
def encontrar_valores_ausentes(sequencia: List[int]) -> List[int]:
    completo = set(range(min(sequencia), max(sequencia) + 1))
    return list(completo - set(sequencia))

# Alternativa
def find_missing_in_sequence(sequence_list: List[float]) -> List[float]:
    missing_list = []
    for i in range(min(sequence_list), max(sequence_list)+1):
        if i not in sequence_list:
            missing_list.append(i)
    return missing_list

sequence_list = [1,3,4,5,7,10,20]
print(find_missing_in_sequence(sequence_list))

