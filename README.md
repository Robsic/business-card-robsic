# business-card-robsic
Modelo de cartão de visitas do Laboratório de Robótica, Sistemas Inteligentes e Complexos.

## Instruções para a utilização do modelo

### Pré-requisitos

- XeLaTeX - para compilação do projeto devido ao uso de fontes não-padrão
- Pacotes LaTeX utilizados:
  - geometry - para definição do tamanho do papel e margens
  - fontspec - para uso da fonte institucionald a Unifei
  - fontawesome - para os ícones
  - tikz - para os elementos gráficos
  - qrcode - para geração dos... qrcodes

### Compilação

Para compilar o projeto, é necessário, antes de tudo, possuir uma distribuição LaTeX instalada em seu sistema que suporte o ambiente XeLaTeX (ou LuaLaTeX).
Os pacotes acima também devem estar instalados.

Após a adequação do sistema, modifique o arquivo main.tex em duas partes:

- acerte o caminho para a fonte FontAwesome, conforme o local onde o pacote foi instalado em sua distribuição LaTeX.
Exemplo para a distribuição TeXLive no Linux:
  -   ```\defaultfontfeatures{ Path = /usr/local/texlive/2022/texmf-dist/fonts/opentype/public/fontawesome/ }```
  
- os dados pessoais, que estão em três comandos:
  - ```\newcommand{\nome}{Seu nome completo}```
  - ```\newcommand{\cargo}{Ocupação no RobSIC}```
  - ```\newcommand{\email}{seuemail@unifei.edu.br}```

Após as alterações, compile o arquivo main.tex com XeLaTeX ou LuaLaTeX e o PDF com o cartão será gerado.
O PDF está pronto para ser impresso na gráfica de sua preferência! Prefira papel couché 250g ou 300g para um melhor resultado.
