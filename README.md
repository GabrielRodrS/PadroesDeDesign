# PadroesDeProjeto

##### Builder
	Introdução:
		Design criacional
		Construir objetos complexos passo a passo
		Diferentes tipos e representações  de um objeto, usando o mesmo código de construção

	Problema:
		Imagine ao criar um novo objeto que requer vários campos de parâmetros ou objetos aninhados passo a passo para que sejam inicializados pelo construtor, o código poderia se estender demais.
		Uma solução não muito plausivel seria possuir uma classe base construtora gigante que envolveria todos os casos possíveis, não necessitando de outras subclasses. No entanto criaria parâmetros que muitas vezes não serão utilizados, deixando o construtor de forma incorreta.

	Solution:
		Então é sugerido que extraia o código de construção do objeto de sua classe para objetos separados chamados construtores.

		A construção do objeto é realizado passo a passo, chamando o processo de construção apenas uma única vez com as configurações particulares do objeto, executando apenas as implementações requeridas.

		Neste caso, é possível criar diversas classes construtoras que seguem o mesmo conjunto de etapas, mas de forma diferente. Um conjunto ordenado de chamadas de construtores

	Director
		Poderá extrair uma série de chamandas e passar para a classe director, onde director define a ordem de execução de construção, enquanto outras classes builder fornecem a implementação para estas etapas. No entanto não é realmente necessário uma classe director.

	Pros e Contras
		Pros:
			Construir objetos passo a passo, adiar etapas ou construir recursivamente
			Usar o mesmo código de construção para várias representações do mesmo produto
			Isolar o código de construção complexo da lógica de negócios do produto.
		Contras:
			Com a criação de novas múltiplas classes, a complexidade do código geral aumentará

##### Facade
	Introdução:
		É um padrão estrutural
		Fornece uma interface simplificada para conjuntos complexos de classes, como bibliotecas, frameworks e outros.

	Problema:
		Imagine que você queira trabalhar com objetos de bibliotecas ou frameworks sofisticados, é sempre necessário inicializar e configurar o ambiente para uso.
		Como depende dos detalhes de implementação de terceiros, ficaria complicado comprrender e corrigir a lógica de negócios das suas classes

	Solução:
		Facade é uma classe que fornece uma simples interface de um subsistema complexo que contém partes móveis. Pode ter uma funcionalidade um pouco limitade se comparado a trabalhar diretamente com o subsistema, no entanto os recursos necessários geralmente são disponíveis.
		É muito útil quando for utilizar apenas uma parte de funcionalidade de uma biblioteca complexa.


##### Observer

	Introdução:
		É um padrão comprotamental
		Define um mecanismo, onde notifica múltiplos objetos sobre qualquer evento que aconteça ao objeto que estão observando.

	Problem:
		Imagine que tenha mais de um tipo de objeto. Um cliente está interessando em uma nova versão de um produto em uma loja que será disponibilizado somente em breve.
		O cliente poderia ir ver se o novo produto está disponível visitando frequentemente, no entante, muitas destas viagens podem não teriam nenhum retorno.
		Uma solução não muito indicada, seria enviar um e-mail a todos os clientes notificando que o novo produto já está dispoível na loja, no entanto alguns cliente não estão interessado neste produto novo e neste caso serão apenas incomodades.
		No fim, se encontra em uma situação conflitante, cada cliente deverá ir a loja frequentemente ou a loja enviará notificações a todos o clientes independentemente.

	Solução:
		O objeto que possui uma mudança de estado interessante geralmente é chamado de assunto, mas como ele vai notificar outro objetos com sua mudança, então será chamado de publicador. Todos os outros objetos que querem buscar alterações são chamados de assinantes.
		O padrão recomenda que adicione um mecanismo de assinatura à classe publicador, para que possam assinar ou cancelar a assinatura individualmente por cada outro objeto.
		Agora sempre que um determinado evento ocorrer ao publicador, notificará por métodos os objetos assinantes.
		Alguns aplicativos reais podem ter várias classes de diferented tipos de assinantes para recorrer aos eventos de uma mesma classe publicadora. Se não for realmente bem implementada poderá ser confusa.
		Então é recomendado que todos os assinantes implementem a mesma interface e a comunicação ocorra somente por ela, com isto, o publicador pode passar alguns outros parâmetros que podem ser úteis junto à notificação
		Caso sua aplicação tenha muitos publicadores, uma solução seria fazer todos os publicador seguirem a mesma interface, onde seria apenas necessários alguns métodos dos assinantes, esta configuração permite que os assinantes observem os estados dos publicadores sem interligar às suas classes diretamente.

  ### UML

Builder
  ![Captura de tela 2024-12-23 215512](https://github.com/user-attachments/assets/d88993dc-01bb-4ec0-b9a3-2cf64c6c96cb)

Facade
  ![Captura de tela 2024-12-23 215531](https://github.com/user-attachments/assets/0d5c7609-bfde-4583-b757-6c9ddc696260)

Observer
  ![Captura de tela 2024-12-23 215552](https://github.com/user-attachments/assets/1d5b4930-db42-4448-a0ae-cf50d28ac1b4)

### A documentação dos códigos ficaram nos arquivos de códigos!

# Todo o conteúdo neste arquivo foi pesquisado e traduzido utilizando o site https://refactoring.guru/ como fonte de informação!
