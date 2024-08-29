<div align="center">
<h1>djangoCars - Desenvolvido por Lucas E. Dickmann</h1>
</div>

**Descrição**

djangoCars é uma aplicação web Django que apresenta um catálogo de carros, permitindo aos usuários visualizar detalhes e imagens de diferentes modelos, bem como adicionar, editar ou excluir algum carro.

**Funcionalidades**

* **Listagem de Carros:** A página principal exibe uma lista de carros com miniaturas e nomes.
* **Detalhes do Carro:** Cada carro possui uma página de detalhes com informações adicionais e uma imagem maior.
* **Adicionar Veículo:** Cria um veículo e mostra na listagem.
* **Deletar Carro:** Deleta o carro.
* **Atualizar Carro:** Entra no carro específico e se necessário atualiza algum dado estipulado.

**Como Usar**

**Pré-requisitos:**

* Python
* Django
* Pillow

**Instalação:**

1. Clone este repositório: `git clone https://github.com/seu-usuario/djangoCars.git`
2. Navegue até o diretório: `cd djangoCars`
3. Crie um ambiente virtual: `python -m venv venv`
4. Ative o ambiente virtual:
    * Windows: `venv\Scripts\activate`
    * Linux/macOS: `source venv/bin/activate`
5. Instale as dependências: `pip install -r requirements.txt`

**Execução:**

1. Execute as migrações: `python manage.py migrate`
2. Crie um superusuário (opcional): `python manage.py createsuperuser`
3. Inicie o servidor de desenvolvimento: `python manage.py runserver`
4. Acesse a aplicação em seu navegador: `http://127.0.0.1:8000/`

**Contribuição**

Sinta-se à vontade para contribuir com melhorias ou novos recursos. Abra um issue para discutir ideias ou envie um pull request com suas alterações.

**Demonstração**

<div align="center">
<h3>Cars List</h3>
<table border=0 style="border: 1.2px solid #c6c6c6 !important; border-spacing: 2px; width: auto !important;">
<div align=center><img src="https://github.com/user-attachments/assets/83f84127-3b69-4537-b09e-48b152d2a494" alt="lista d ecarros" style="margin: 0 !important; height: 300px !important;">
</div></table></div>

<div align="center">
<h3>Cars Create</h3>
<table border=0 style="border: 1.2px solid #c6c6c6 !important; border-spacing: 2px; width: auto !important;">
<div align=center><img src="https://github.com/user-attachments/assets/55de4ff4-d383-47a0-9b02-6024b7a249c4" alt="Tabela para criar carro novo" style="margin: 0 !important; height: 400px !important;">
</div></table></div>


## Desenvolvido por Lucas E. Dickmann, no decorrer do curso Django Master.
