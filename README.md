# Tarefa 1
Execute:

```
python src/tarefa1.jpg.
```

# Tarefa 2

Realizado no arquivo docs/Tarefa2.pdf


# Tarefa 3

# Tarefa 4

Realizado no arquivo videos/Tarefa4.mp4

# Work at MaChiron

A MaChiron é uma startup que busca unir a inteligência artificial e o aprendizado de máquina e a expertise humana interdisciplinar para oferecersoluções em saúde. Nossos dois principais projetos, a LivIA e a SARA, tem objetivos similares: utilizar exames de imagem para detectar anomalias, condições físicas e doenças.

# Exemplo de Projeto

No projeto SARA, trabalhamos com tomografias computadorizadas do pulmão, as quais chegam até nós no formato DICOM.
Na pasta EXAMES, temos o exemplo de 5 exames.

O formato DICOM guarda 2 tipos de informações: os metadados e a imagem obtida no exame.

### Tarefa 1 - Extração de informações

Existem bibliotecas de leitura de DICOM para diferentes linguagens de programação, por exemplo, Python e R. A partir destes exames, extraia as informações:
- ID, idade e sexo do paciente;
- Accession number (ID do exame), data do exame e espaçamento dos slices.

Apresente um programa que tem como saída as informações desejadas.

### Tarefa 2 - Estruturação de Banco de dados

Os radiologistas querem adicionar as seguintes informações para cada exame: Diagnóstico (Pnemonia, Tuberculose, Normal), Grau de severidade (Grave, Moderado, Leve, Ausente) e Nível de normalidade do exame (Típico ou Atípico).
Como seria a estrutura final deste banco de dados? Como você implementaria ele?

### Tarefa 3 - Visualização do Banco

Os pesquisadores gostariam de visualizar informações contidas neste banco. Monte uma interface gráfica em que possamos visualizar um resumo detalhado das informações dos exames inseridos.

Como exemplo, vejam o dashboard da LivIA
![DashLivia](https://user-images.githubusercontent.com/10574148/109868849-e9fa9300-7c46-11eb-955d-040c13e10786.jpeg)


Como bônus, faça uma ferramenta de anotação com suporte para imagens DICOM.

### Tarefa 4 - Ferramenta de Anotação


Para que os radiologistas possam anotar os exames, é necessario montar uma interface de visualização e anotação. O CVAT é uma ferramenta aberta que pode ser usada para esta finalidade.
Não precisa ser numa instalação remota.Monte uma instalação local do CVAT: https://hacarus.com/information/tech/20200717-cvat-dicom-ai/
e nos apresente uma gravação ou sequencia de screenshots mostrando que a interface do anotador está funcionando, incluindo uma anotação de um órgão em algumas fatias de um Dicom.
