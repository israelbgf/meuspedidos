# MeusPedidos
Projeto demonstrando técnicas de testes, arquitetura e clean code.

### Features
- Core da aplicação **completamente desacoplado** dos frameworks web (delivery mechanisms)
- Inspirado na arquitetura proposta pelo [Uncle Bob](https://www.youtube.com/watch?v=WpkDN78P884)
- Dois frameworks web, **Django** e **Flask** (alternados através de parâmetro de configuração)
- Core feito inteiramente com **TDD** (framworks nem tanto. =P)

Para alterar o delivery mechanism:

- heroku config:set DELIVERY_MECHANISM=FLASK
- heroku config:set DELIVERY_MECHANISM=DJANGO

Além disso é precisso configurar as variáveis de ambiente para o servidor de e-mail:

- EMAIL_HOST
- EMAIL_PORT
- EMAIL_HOST_USER
- EMAIL_HOST_PASSWORD