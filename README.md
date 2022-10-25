# ETL para Cálculo de IMC

Projeto de ETL para cálculco de IMC.
O sistema consiste em extrair os dados de múltiplas fontes(CSV, XML, JSON). 
Após a extração é feita a transformação dos dados aplicando um data cleaning para regularizar as unidades de medidas e eliminar dados duplicados.
Uma vez os dados disponibilizados, é aplicado a regra de cálculo de IMC, e o resultado é carregado num arquivo pronto para consumo de usuários finais.

OBS: Os dados se encontram nas mesmas posições nos diversos arquivos, por isso não foi necessário tratamento de reposicionamento de dados.