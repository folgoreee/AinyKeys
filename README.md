# AinyKeys - Gerador de Senhas Seguras 🔐

O **AinyKeys** é um aplicativo de interface gráfica (GUI) desenvolvido em Python que permite gerar senhas criptograficamente seguras e personalizadas. O foco da ferramenta é oferecer uma interface simples para criar senhas robustas, ao mesmo tempo em que calcula a entropia matemática para informar o nível exato de segurança da senha gerada.

---

## Principais Funcionalidades

* **Personalização de Tamanho:** Escolha o comprimento da senha entre 8 e 128 caracteres.
* **Seleção de Conjuntos:** Ative ou desative o uso de letras maiúsculas, minúsculas, números e símbolos especiais.
* **Filtro Anti-Ambiguidade:** Opção para remover caracteres visualmente semelhantes (como `1`, `l`, `I`, `0`, `O`), evitando confusões na hora de ler ou digitar a senha.
* **Cálculo de Entropia:** Analisa matematicamente a força da senha com base no tamanho e no conjunto de caracteres disponível.
* **Integração com a Área de Transferência:** Botão de um clique para copiar a senha gerada de forma rápida.
* **Geração Segura:** Utiliza a biblioteca nativa `secrets` do Python, recomendada para a geração de dados criptograficamente fortes, substituindo o módulo comum `random`.

---

## Como a Força da Senha é Calculada?

A segurança da senha não depende apenas do seu tamanho, mas do número de possibilidades de caracteres. O AinyKeys calcula a entropia da senha (em bits) usando a seguinte fórmula matemática:

$$E = L \times \log_2(R)$$

Onde:
* **$E$** = Entropia (força em bits).
* **$L$** = Comprimento da senha (tamanho).
* **$R$** = Tamanho do conjunto de caracteres selecionado (*pool size*).

Com base no resultado dessa equação, o sistema classifica a senha conforme a tabela abaixo:

| Entropia (Bits) | Classificação | Cor do Indicador |
| :--- | :--- | :--- |
| Menor que 28 | Muito fraca | Vermelho |
| De 28 a 35 | Fraca | Laranja |
| De 36 a 59 | Razoável | Amarelo |
| De 60 a 127 | Forte | Verde claro |
| 128 ou maior | Muito forte | Verde escuro |

---

## Pré-requisitos

O projeto foi construído utilizando apenas as bibliotecas padrão do Python. Você não precisa instalar dependências externas via `pip`.

* **Python 3.x** instalado na sua máquina.
* **Tkinter** (normalmente já incluído nas instalações padrão do Python na maioria dos sistemas operacionais. No Linux, pode ser necessário instalar o pacote `python3-tk`).

---

## Como Executar

1. Salve o código-fonte em um arquivo chamado `ainykeys.py`.
2. Abra o terminal ou prompt de comando.
3. Navegue até o diretório onde o arquivo foi salvo.
4. Execute o seguinte comando:

```bash
python ainykeys.py
