# MaxMin Select

## Sobre o Projeto
O **MaxMin Select** é um projeto acadêmico desenvolvido para implementar o algoritmo de **seleção simultânea do maior e do menor elementos** de uma sequência de números, utilizando a abordagem de **divisão e conquista**.

O objetivo do projeto é explorar a eficiência desse algoritmo, comparando-o com abordagens mais ingênuas e analisando sua complexidade assintótica.

## Algoritmo MaxMin Select
O **MaxMin Select** encontra o maior e o menor número em um array com um número mínimo de comparações, utilizando a técnica de **divisão e conquista**.

### **Passos do Algoritmo**
1. Se houver **apenas um elemento**, ele é tanto o maior quanto o menor.
2. Se houver **dois elementos**, apenas **uma comparação** é feita.
3. Para **mais de dois elementos**, divide-se o array em duas metades.
4. Recursivamente, encontra-se o maior e o menor de cada metade.
5. Os resultados são combinados para determinar o maior e menor geral.

## Estrutura do Projeto
O projeto contém os seguintes arquivos:

```
📂 maxmin-select
│── main.py          # Implementação do algoritmo MaxMin Select
│── README.md        # Documentação do projeto
│── assets/          # Contém imagens e diagramas explicativos
```

## Ambiente Virtual
Para garantir um ambiente isolado para o projeto, siga os passos abaixo:

### **Passo 1: Criar e ativar o ambiente virtual**

Crie um ambiente virtual usando o seguinte comando:
```bash
python -m venv venv
```

Ative o ambiente virtual:

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```

- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### **Passo 2: Instalar dependências (se houver)**
```bash
pip install -r requirements.txt
```

### **Passo 3: Executar o algoritmo**
```bash
python main.py
```

## Análise da Complexidade Assintótica
A complexidade do algoritmo **MaxMin Select** pode ser analisada por dois métodos:

### **1. Contagem de Operações**
- O algoritmo reduz o número de comparações ao dividir o array em duas metades.
- A cada nível da recursão, realizamos apenas **3 comparações por nível**.
- A complexidade final é **O(n)**.

### **2. Aplicação do Teorema Mestre**
A recorrência do algoritmo é dada por:
```
T(n) = 2T(n/2) + O(1)
```
- **Parâmetros:**
  - `a = 2`
  - `b = 2`
  - `f(n) = O(1)`
- **Cálculo de `log_b(a)`:**
  - `log_2(2) = 1`
- **Resultado:** O(n)

## Diagrama do Algoritmo
O projeto inclui um **diagrama da árvore de recursão** para melhor visualização do funcionamento do algoritmo. Ele está localizado na pasta `assets/diagrama.png` e representa:

1. Como o problema é dividido em subproblemas menores.
2. Como os subproblemas são combinados para obter o resultado final.
3. O número de comparações realizadas em cada nível da recursão.

## Exemplo de Entrada e Saída
### **Entrada:**
```python
arr = [3, 5, 1, 8, 2, 9, 4, 7, 6]
min_val, max_val = max_min_select(arr, 0, len(arr) - 1)
print(f"Menor elemento: {min_val}, Maior elemento: {max_val}")
```

### **Saída:**
```
Menor elemento: 1, Maior elemento: 9
```
## Licença
Este projeto está licenciado sob a **Licença MIT**. Sinta-se à vontade para utilizá-lo e modificá-lo conforme necessário.

---
