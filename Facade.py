from __future__ import annotations


class Facade:
    """
    a classe Facede traz uma interface simples para a lógica complexa de um ou vários sistemas;
    Facade traz as solicitações feitas pelo usuário para os objetos apropriados;
    É responsável por gerenciar o ciclo de vida;
    Tudo acima é utilizado como proteção contra a complexidade do subsistema.
    """

    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2) -> None:
        """
        A depender de sua aplicação, você pode fornercer objetos de subsistema existentes ao Facade
        ou forçar ele mesmo a criá-los.
        """

        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2 or Subsystem2()

    def operation(self) -> str:
        """
        Os métodos são atallhos convenientes para a sofisticada funcionalidade do subsistema.
        E os usuários chegam apenas a uma pequena fração do subsistema.
        """

        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())
        return "\n".join(results)


class Subsystem1:
    """
    O susistema pode aceitar solicitações tanto de Facade, quanto diretamente do usuário.
    Facade seria como um outro usuário, não sendo parte do subsistema.
    """

    def operation1(self) -> str:
        return "Subsystem1: Ready!"

    # ...

    def operation_n(self) -> str:
        return "Subsystem1: Go!"


class Subsystem2:
    """
    Algumas Facade podem trabalhar com múltiplos subsistemas ao mesmo tempo.
    """

    def operation1(self) -> str:
        return "Subsystem2: Get ready!"

    # ...

    def operation_z(self) -> str:
        return "Subsystem2: Fire!"


def client_code(facade: Facade) -> None:
    """
    O usuário trabalha com um subsistema complexo utilizando uma simples interface pela Facade.
    Quando facade gerencia o ciclo de vida, o usuário não tem necessidade de conhecer a existência do subsistema.
    Esta forma de organização, garante controle sobre a complexidade.
    """

    print(facade.operation(), end="")


if __name__ == "__main__":
    # The client code may have some of the subsystem's objects already created.
    # In this case, it might be worthwhile to initialize the Facade with these
    # objects instead of letting the Facade create new instances.
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)
    client_code(facade)