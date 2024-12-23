'''
Desafio: Análise de Vendas de Produtos 
Objetivo: 
Dado um arquivo CSV contendo dados de vendas de produtos, 
o desafio consiste em ler os dados, processá-los em um 
dicionário para análise e, por fim, calcular e reportar 
as vendas totais por categoria de produto.
'''

# Funções
import csv
from pathlib import Path

def read_csv(file_path: Path) -> list[dict]:
    '''
    Function to read the CSV file and return a dictionary 
    list with the data read
    '''
    result_list: list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            result_list.append(row)

    return result_list

# def process_data(dados):
#     categorias = {}
#     for item in dados:
#         categoria = item['Category']
#         if categoria not in categorias:
#             categorias[categoria] = []
#         categorias[categoria].append(item)
#     return categorias


def process_data(data: list[dict]) -> dict:
    '''
    Function that gets the dictionary list of items and converts it into a 
    new dictionary, where each key is the category name and its values are
    each item in the category 
    '''
    category_dict: dict = {}
    for item in data:
        if item['Category'] not in category_dict.keys():
            category_dict[item['Category']] = []
        category_dict[item['Category']].append(
            {'Product': item['Product'], 
            'Quantity': item['Quantity'], 
            'Sale_Price': item['Sale_Price']}
            )
    
    return category_dict

def calculate_category_sales(processed_data: dict) -> dict:
    '''
    Function that receives the processed data and calculates, for each 
    unique category of products, the total sales value
    '''
    sales_dict: dict = {}
    for category, items in processed_data.items():
        total_sales: float = sum(int(item['Quantity']) * \
                                 float(item['Sale_Price']) for item in items)
        sales_dict[category] = total_sales
    
    # Round the values for two decimal places
    for category, value in sales_dict.items():
        sales_dict[category] = round(value, 2)

    # Sort the dictionary by value
    sales_dict = {category: value for category, 
                  value in sorted(sales_dict.items(),
                                  key=lambda item: item[1], 
                                  reverse=True)}

    return sales_dict

def main():
    csv_content = read_csv('sales_data.csv')
    processed_data = process_data(csv_content)
    total_sales = calculate_category_sales(processed_data)
    for category, total in total_sales.items():
        print(f'{category}: ${total}')

if __name__ == '__main__':
    main()

