# Generate Certificate

Generate Certificate é um projeto em Python que permite automatizar a geração de certificados personalizados para cursos, workshops ou eventos. Este projeto foi desenvolvido para facilitar o processo de criação de certificados, economizando tempo e esforço.

## Funcionalidades Principais
- Leitura de Dados da Planilha Excel: O sistema utiliza a biblioteca `openpyxl` para ler os dados dos alunos a partir de uma planilha do Excel.
- Manipulação de Imagens: A biblioteca Pillow (PIL) é empregada para abrir a imagem padrão do certificado e adicionar dinamicamente os dados dos alunos a ela.
- Geração Automatizada de Certificados: Após a inserção dos dados na imagem do certificado, o sistema gera automaticamente os certificados para cada aluno, garantindo precisão e consistência.
- Interface de Usuário (opcional): Uma interface gráfica simples pode ser implementada para facilitar a interação do usuário, permitindo que ele selecione a planilha de dados e inicie o processo de geração de certificados com apenas alguns cliques.
- Personalização Flexível: O projeto é altamente personalizável, permitindo ajustes na formatação do certificado, posicionamento dos dados e escolha da fonte.

## Como Usar
1. Clone este repositório em sua máquina local.
2. Instale as dependências do projeto executando `pip install -r requirements.txt`.
3. Certifique-se de ter uma imagem padrão do certificado e uma planilha Excel com os dados dos alunos.
4. Execute o script `generate_certificate.py`, fornecendo o caminho para a planilha Excel como argumento.
5. Os certificados serão gerados e salvos em um diretório de saída.

## Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para reportar problemas, sugerir melhorias ou enviar pull requests para este projeto.

## Licença
Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais informações.
