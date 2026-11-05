from src.custom_stack_class import CustomStack

class NumberAscOrder:
    def sort(self, stack: CustomStack) -> list:
        """
        Retorna uma lista ordenada de forma ascendente com os elementos da pilha.
        Trata pilhas vazias retornando uma lista vazia.
        """
        if stack.is_empty():
            return []
        
        elements = []
        while not stack.is_empty():
            elements.append(stack.pop())
            
        elements.sort()
        return elements