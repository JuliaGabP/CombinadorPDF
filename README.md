# Combinador de PDF

Script em Python para combinar vários arquivos PDF em um único documento, ignorando automaticamente a primeira página de cada arquivo.

Projeto útil para situações em que vários PDFs possuem uma capa repetida ou uma primeira página desnecessária, e você deseja reunir apenas o conteúdo principal em um único arquivo final.

## Funcionalidades

- Procura automaticamente todos os arquivos `.pdf` da pasta atual
- Ordena os PDFs em ordem alfabética
- Lê cada arquivo PDF encontrado
- Ignora a primeira página de cada PDF
- Junta o restante das páginas em um único arquivo
- Gera um arquivo final chamado:

```bash
combined.pdf
```

> Os arquivos PDF que serão combinados devem estar na mesma pasta do script.

## Tecnologias Utilizadas

- **Python 3**
- **pypdf**
- **os** 


---

## Instalação

### Clone ou crie a pasta do projeto

```bash
mkdir pdf-combiner
cd pdf-combiner
```

### Crie um ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
```


### Instale a dependência necessária

```bash
pip install pypdf
```

## Executando

### Coloque todos os arquivos PDF na mesma pasta do script

Exemplo:

```bash
pdf-combiner/
├── combinar_pdfs.py
├── relatorio1.pdf
├── relatorio2.pdf
├── relatorio3.pdf
```

### Execute o script

```bash
python3 combinar_pdfs.py
```

### Resultado

Após a execução, será criado um novo arquivo:

```bash
combined.pdf
```

## Exemplo Prático

### PDFs originais:
- `aula1.pdf` - 5 páginas
- `aula2.pdf` - 4 páginas
- `aula3.pdf` - 6 páginas

### Resultado:
O arquivo `combined.pdf` terá:

- páginas 2, 3, 4 e 5 de `aula1.pdf`
- páginas 2, 3 e 4 de `aula2.pdf`
- páginas 2, 3, 4, 5 e 6 de `aula3.pdf`

## Observações Importantes

- O script **ignora PDFs com apenas 1 página**, pois não há páginas após a primeira.

