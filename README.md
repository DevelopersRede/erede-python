# SDK Python

SDK de integração eRede

# Funcionalidades

Este SDK possui as seguintes funcionalidades:
* Autorização
* Captura
* Consultas
* Cancelamento
* 3DS1 (descontinuada)
* Zero dollar
* iata
* MCC dinâmico

A função 3DS1 foi descontinuada e será atualizada nas próximas versões do SDK.

# Utilizando

## Autorizando uma transação

```python
from erede import *

store = Store("PV", "TOKEN", Environment.sandbox())

transaction = Transaction(12345, "Reference")
transaction.credit_card("5448280000000007", "123", "12", "2020", "Fulano de Tal")
transaction.set_additional(3456, 12)

try:
    transaction = eRede(store).create(transaction)

    if transaction.returnCode == "00":
        print("Transação aprovada com sucesso. O tid é: {}".format(transaction.tid))
except RedeError as e:
    print("Opz[{}]: {}".format(e.code, e))
```

Por padrão, a transação é capturada automaticamente; caso seja necessário apenas autorizar a transação, o método `Transaction.capture_transaction(False)` deverá ser chamado com o parâmetro `False`:

```python
from erede import *

store = Store("PV", "TOKEN", Environment.sandbox())

transaction = Transaction(12345, "Reference")
transaction.credit_card("5448280000000007", "123", "12", "2020", "Fulano de Tal").capture_transaction(False)

try:
    transaction = eRede(store).create(transaction)

    if transaction.returnCode == "00":
        print("Transação aprovada com sucesso. O tid é: {}".format(transaction.tid))
except RedeError as e:
    print("Opz[{}]: {}".format(e.code, e))
```

## Autorizando uma transação com MCC dinâmico

```python
from erede import *

store = Store("PV", "TOKEN", Environment.sandbox())

transaction = Transaction(12345, "Reference")
transaction.credit_card("5448280000000007", "123", "12", "2020", "Fulano de Tal")
transaction.mcc("LOJADOZE", "22349202212", SubMerchant("1234", "Sao Paulo", "Brasil"))

try:
    transaction = eRede(store).create(transaction)

    if transaction.returnCode == "00":
        print("Transação aprovada com sucesso. O tid é: {}".format(transaction.tid))
except RedeError as e:
    print("Opz[{}]: {}".format(e.code, e))
```

## Autorizando uma transação com identificação de plataforma

```python
from erede import *

store = Store("PV", "TOKEN", Environment.sandbox())

transaction = Transaction(12345, "Reference")
transaction.credit_card("5448280000000007", "123", "12", "2020", "Fulano de Tal")
transaction.set_additional(1234, 12)

try:
    transaction = eRede(store).create(transaction)

    if transaction.returnCode == "00":
        print("Transação aprovada com sucesso. O tid é: {}".format(transaction.tid))
except RedeError as e:
    print("Opz[{}]: {}".format(e.code, e))
```

## Autorizando uma transação IATA

```python
from erede import *

store = Store("PV", "TOKEN", Environment.sandbox())

transaction = Transaction(12345, "Reference")
transaction.credit_card("5448280000000007", "123", "12", "2020", "Fulano de Tal")
transaction.set_iata("code123", "250")

try:
    transaction = eRede(store).create(transaction)

    if transaction.returnCode == "00":
        print("Transação aprovada com sucesso. O tid é: {}".format(transaction.tid))
except RedeError as e:
    print("Opz[{}]: {}".format(e.code, e))
```
