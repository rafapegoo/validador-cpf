
# CPF Validator 🆔

A Python implementation of the Brazilian CPF (Cadastro de Pessoas Físicas) validation algorithm.

## 🔍 How It Works
Validates CPF numbers by:
1. Extracting first 9 digits
2. Calculating both verification digits
3. Comparing with original CPF digits

```python
CPF: 898.280.650-45 → Valid
```

## ⚙️ Algorithm Steps
1. **First Digit Calculation**:
   - Multiply each of 9 digits by descending weights (10→2)
   - Sum results and apply modulus 11
2. **Second Digit Calculation**:
   - Multiply 10 digits (original 9 + first digit) by weights (11→2)
   - Sum results and apply modulus 11
3. **Validation**:
   - Compare generated digits with original

## 🛠️ Technical Features
- Step-by-step digit calculation
- Proper modulus 11 handling
- Clean conditional checks
- Input validation ready (add your own)

## 🚀 How to Use
1. Set CPF in code:
```python
cpf = '89828065045'  # Without punctuation
```
2. Run script:
```bash
python cpf_validator.py
```

## 📝 Notes
- Works with raw numbers (no punctuation)
- Includes edge case handling (remainder > 9 → digit 0)
- Easy to integrate with input systems

## 📚 Learn More
[Official CPF Calculation Rules](https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/cpf)

---

Developed as part of Python learning journey - validating real-world identification systems.
```

Key features:
1. Clear algorithm explanation
2. Visual CPF format example
3. Technical implementation details
4. Usage instructions
5. Official reference
6. Learning context
