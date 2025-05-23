# Prognóstico Veterinário Automatizado: Inteligência para a Saúde Animal

**Uma Solução para Prever Desfecho e Tempo de Internação de Pets**

* **Autor:** Rian
* **Contexto:** Hackathon FMU

## Visão Geral

Este projeto apresenta um sistema de prognóstico veterinário automatizado desenvolvido como parte de um desafio de faculdade. O objetivo principal é utilizar a inteligência artificial para auxiliar médicos veterinários a prever o desfecho de casos clínicos (ex: recuperação, óbito) e estimar o tempo de internação de animais de estimação, oferecendo um apoio mais objetivo às decisões clínicas.

## O Problema

No dia a dia da clínica veterinária, profissionais frequentemente se deparam com:

* Diagnósticos complexos e que podem demandar tempo considerável.
* Dificuldade em estimar com precisão o tempo de internação necessário para um paciente.
* Decisões prognósticas muitas vezes baseadas predominantemente na experiência subjetiva do veterinário.

Esses desafios podem impactar o planejamento do tratamento, a comunicação com os tutores e a gestão de recursos da clínica.

## Nossa Solução

Para endereçar esses problemas, desenvolvemos um sistema de prognóstico automatizado que, a partir de dados clínicos de entrada, oferece:

* **Previsão de Desfecho Clínico:** Classifica a probabilidade de diferentes desfechos (ex: recuperação, óbito).
* **Estimativa de Dias de Internação:** Regride o número provável de dias que o animal necessitará de internação.
* **Interface Intuitiva:** Uma aplicação web simples para que os veterinários insiram os dados e visualizem as previsões.

## Arquitetura da Solução

O sistema é composto por uma aplicação web front-end e uma API back-end:

1.  **Entrada de Dados:** O veterinário insere os dados clínicos do paciente através da interface web.
2.  **Interface Web (Streamlit):** Desenvolvida com Streamlit, esta interface amigável coleta os dados do animal.
3.  **Comunicação:** Os dados são enviados via JSON POST para a API de previsão.
4.  **API de Previsão (FastAPI):** O back-end, construído com FastAPI, recebe a requisição, valida os dados, carrega os modelos de IA treinados (`.pkl`) e os encoders necessários.
5.  **Inferência:** Os modelos de Machine Learning processam os dados e geram as previsões.
6.  **Retorno:** A API retorna a previsão de desfecho e a estimativa de dias de internação.
7.  **Exibição de Resultado:** As previsões são exibidas de forma clara na interface Streamlit para o veterinário.

*(Fluxo visual pode ser representado pela imagem `image_600074.png` fornecida no contexto do projeto).*

## Variáveis de Entrada do Modelo

Os modelos utilizam os seguintes indicadores clínicos vitais, escolhidos por sua relevância, facilidade de obtenção e impacto no prognóstico:

* **FC (Frequência Cardíaca):** Nº de batimentos cardíacos por minuto. Crucial para avaliar a função cardiovascular.
* **FR (Frequência Respiratória):** Nº de movimentos respiratórios por minuto. Reflete a função pulmonar e oxigenação.
* **PAS (Pressão Arterial Sistólica):** Pressão sanguínea nas artérias durante a contração cardíaca. Indica a perfusão sanguínea dos órgãos.
* **Temp (Temperatura Corporal):** Sinal clássico de processos inflamatórios, infecciosos ou distúrbios de termorregulação.
* **Hematócrito:** Percentual de glóbulos vermelhos no volume total de sangue. Informativo sobre anemia, hidratação e capacidade de transporte de oxigênio.

## Implementação Técnica

### 1. Coleta e Pré-processamento de Dados

* **Fontes de Dados:** Unificação de dados de prontuários (Excel), exames de sangue (CSV), evolução clínica (CSV) e informações estruturadas (JSON).
* **Tratamento:**
    * Valores ausentes foram preenchidos com zero (estratégia inicial).
    * Cálculo dos dias de internação a partir das datas de início e fim.
    * Codificação de variáveis categóricas para compatibilidade com os modelos.

### 2. Treinamento dos Modelos

Foram treinados e salvos dois modelos principais utilizando Scikit-learn:

* **Classificação (Desfecho Clínico):** `Random Forest Classifier`
* **Regressão (Dias de Internação):** `Gradient Boosting Regressor`

### 3. Desenvolvimento da Aplicação

* **Aplicação Web (Frontend):** `Streamlit` – para uma interface de usuário simples e interativa.
* **API de Previsão (Backend):** `FastAPI` – para um serviço robusto, escalável e que garante a correta formatação dos dados para inferência.

## Tecnologias Utilizadas

* **Python:** Linguagem principal de desenvolvimento.
* **Scikit-learn:** Para treinamento e utilização dos modelos de Machine Learning.
* **Pandas:** Para manipulação e pré-processamento de dados.
* **Streamlit:** Para a construção da interface web.
* **FastAPI:** Para a criação da API de previsão.
* **Formato de Dados:** CSV, Excel, JSON.

## Resultados Atuais

* Solução funcional capaz de gerar previsões de desfecho e tempo de internação.
* Código com boa estrutura e modularidade, separando as responsabilidades do frontend, backend e modelos.

## Próximos Passos e Melhorias Contínuas

* **Aprimorar Pré-processamento:** Avaliar e implementar estratégias mais sofisticadas para tratamento de dados ausentes.
* **Validação de Entrada Robusta:** Garantir que todas as features (variáveis) utilizadas no treinamento dos modelos sejam devidamente tratadas (ex: escalonamento, codificação) na API e na aplicação web antes da inferência.
* **Integração Cliente-Servidor Completa:** Implementar a comunicação direta da aplicação Streamlit consumindo a API FastAPI.
* **Avaliação de Modelos:** Adicionar e acompanhar métricas de desempenho detalhadas (ex: acurácia, precisão, recall, F1-score para classificação; RMSE, MAE para regressão) no processo de treinamento e validação dos modelos.
* **Deploy:** Empacotar e disponibilizar a aplicação em um ambiente de nuvem ou servidor local para testes e uso.

