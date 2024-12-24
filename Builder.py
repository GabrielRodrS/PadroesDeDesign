from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):
    """
    A interface builder epecifica os métodos para a criação de diferentes partes dos objetos do Produto.
    """

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass


class ConcreteBuilder1(Builder):
    """
    A classe Concrete Builder ordena a interface builder e provê as implementaçõe específicas dos passos de construção.
    Então o programá poderá ter variações na hora de construir um objeto, com implementações diferentes.
    """

    def __init__(self) -> None:
        """
        Uma nova instância deve ter um produto em branco, no qual será usado em montagens posteriores.
        """
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        """
        Pode haver várias variações para a criação de produtos que não seguem a mesma interface,
        então a classe concrete builders devem requisitar os métodos relacionados para chegar ao resultado esperado.

        Recomenda-se quando chegar o resultado final chegar ao cliente, a instância builder
        deve estar preparada para começar a processar um novo outro produto. 
        """
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("PartA1")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")

    def produce_part_c(self) -> None:
        self._product.add("PartC1")


class Product1():
    """
    Usar o padrão builder é interessante quando seus produtos são complexos e necessitam de extensa configuração.
    Os resultados de vários construtores podem não seguir sempre a mesma interface.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Director:
    """
    O diretor é apenas responsável por sequenciar a etapa de construção, é
    recomendado quando é preciso seguir uma ordem específica ou configuração,
    no entanto a classe diretor é opcional.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
        O diretor pode trabalhar com qualquer instância que passar para ele,
        deste modo pode alterar o tipo final do produto.
        """
        self._builder = builder

    """
    O diretor pode construir diversas variaçoês de produtos usando o mesmos passos de construção.
    """

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__ == "__main__":
    """
    O usuário cria um objeto builder,
    passa ao diretor, no qual inicia o processo de construção
    e o resultado final é recuperado do objeto builder.

    """

    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Standard full featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    print("Custom product: ")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()