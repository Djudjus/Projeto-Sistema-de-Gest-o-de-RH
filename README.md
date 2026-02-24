# 🚀 Sistema de Gestão de RH - TechSolutions

Este é um projeto em **Python** desenvolvido para simular um sistema de reajuste salarial corporativo. Ele automatiza o cálculo de aumentos baseados em faixas salariais e simula descontos de encargos sociais (INSS).

## 📋 Funcionalidades

- **Cálculo de Aumento Progressivo**: Aplica percentuais de aumento diferentes conforme o salário atual (estratégia de retenção de talentos).
- **Cálculo de INSS**: Realiza a dedução automática para cálculo do salário líquido.
- **Relatório Profissional**: Gera um extrato detalhado com data e formatação de moeda brasileira.

## 🛠️ Tecnologias Utilizadas

- **Python 3.13**
- **Biblioteca Datetime**: Para capturar o ano vigente do sistema.

## 📈 Lógica de Aumento

O sistema segue as seguintes regras de negócio:
- Salários até **R$ 2.000,00**: 15% de aumento.
- Salários entre **R$ 2.000,01 e R$ 5.000,00**: 10% de aumento.
- Salários acima de **R$ 5.000,00**: 5% de aumento.

## 🚀 Como executar o projeto

1. Certifique-se de ter o Python instalado.
2. Clone este repositório:
   ```bash
   git clone [https://github.com/Djudjus/Projeto-Sistema-de-Gest-o-de-RH.git](https://github.com/Djudjus/Projeto-Sistema-de-Gest-o-de-RH.git)

Desenvolvido por Pedro Eduardo – 