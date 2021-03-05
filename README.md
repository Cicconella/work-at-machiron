# Work at MaChiron

A MaChiron é uma startup que busca unir a inteligência artificial e o aprendizado de máquina e a expertise humana interdisciplinar para oferecersoluções em saúde. Nossos dois principais projetos, a LivIA e a SARA, tem objetivos similares: utilizar exames de imagem para detectar anomalias, condições físicas e doenças.

# Exemplo de Projeto

No projeto SARA, trabalhamos com tomografias computadorizadas do pulmão, as quais chegam até nós no formato DICOM.
Na pasta ???, temos o exemplo de 5 exames.

O formato DICOM guarda 2 tipos de informações: os metadados dos exames e a imagem obtida no exame.

### Tarefa 1 - Extrair informações de dados Médicos

Existem bibliotecas de leitura de DICOM para diferentes linguagens de programação, por exemplo, Python e R. A partir destes exames, extraia as informações:
- ID, idade e sexo do paciente;
- Accession number (ID do exame), data do exame e espaçamento dos slices.

Apresente um programa que tem como saída as informações desejadas.

### Tarefa 2 - Estruturação de Banco de dados

Os radiologistas querem adicionar as seguintes informações para cada exame: Diagnóstico (Pnemonia, Tuberculose, Normal), Grau de severidade (Grave, Moderado, Leve, Ausente) e Nível de normalidade do exame (Típico ou Atípico).
Como seria a estrutura deste banco de dados? Como você implementaria ele?


### Tarefa 3 - Visualização do Banco

Os radiologistas quem visualizar este banco. Monte uma interface gráfica em que possamos visualizar um resumo detalhado das informações dos exames inseridos, com filtros baseados nas informações do paciente. 

Como exemplo, vejam o dashboard da LivIA
![DashLivia](https://user-images.githubusercontent.com/10574148/109868849-e9fa9300-7c46-11eb-955d-040c13e10786.jpeg)


### Tarefa 4 - Ferramenta de Anotação

Para que os radiologistas possam anotar os exames, é necessario montar uma interface de visualização e anotação. o CVAT é uma ferramenta aberta que pode ser usada para isso. Monte uma instalação local do CVAT com suporte para imagens DICOM: https://hacarus.com/information/tech/20200717-cvat-dicom-ai/


