# Work at MaChiron

A MaChiron é uma startup que busca unir a inteligência artificial e o aprendizado de máquina e a expertise humana interdisciplinar para oferecersoluções em saúde. Nossos dois principais projetos, a LivIA e a SARA, tem objetivos similares: utilizar exames de imagem para detectar anomalias, condições físicas e doenças.

# Exemplo de Projeto

No projeto SARA, trabalhamos com tomografias computadorizadas do pulmão, as quais chegam até nós no formato DICOM.
Na pasta ???, temos o exemplo de 5 exames.

O formato DICOM guarda 2 tipos de informações: os labels dos exames e a imagem obtida no exame.

### Tarefa 1

Existem bibliotecas de leitura de DICOM para diferentes linguagens de programação, por exemplo, Python e R. A partir destes exames, extraia as informações:
- ID de paciente, idade e sexo;
- Em relação ao exame, obter o accession number (ID do exame), data e espaçamento dos slices.

### Tarefa 2

Utilize as informações obtidas pelo DICOM e construa a estrutura deste banco de dados.

### Tarefa 3

Os radiologistas quem visualizar este banco. Monte uma interface gráfica, em que possamos visualizar a quantidade de exames inseridos e com alguns filtros baseados nas informações do paciente.

### Tarefa 4 - Bonus: Colocar o CVAT no ar.


