import random
import pytest
from src.custom_stack_class import CustomStack
from src.number_asc_order import NumberAscOrder

def test_sort_stack_with_six_random_numbers():
    # Cenário: Uma pilha de 6 posições, contendo 6 números sorteados (aleatoriamente)
    stack = CustomStack(6)
    random_numbers = random.sample(range(1, 61), 6)  # Ex: números da Mega Sena de 1 a 60
    
    for num in random_numbers:
        stack.push(num)
        
    sorter = NumberAscOrder()
    result = sorter.sort(stack)
    
    # Verifica se ordenou de forma ascendente e manteve os 6 números
    assert len(result) == 6
    assert result == sorted(random_numbers)
    assert stack.is_empty() == True  # A pilha é esvaziada ao retirar os elementos

def test_sort_empty_stack():
    # Cenário: Uma pilha de 6 posições, vazia
    stack = CustomStack(6)
    
    sorter = NumberAscOrder()
    result = sorter.sort(stack)
    
    # Verifica se lida corretamente com a pilha vazia retornando lista vazia
    assert result == []
    assert stack.is_empty() == True