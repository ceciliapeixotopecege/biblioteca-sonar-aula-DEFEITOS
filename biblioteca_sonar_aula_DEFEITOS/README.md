# Biblioteca Sonar — aula prática

Projeto didático Python com cadastro, empréstimo, devolução e relatórios. Inclui testes e um módulo separado com problemas **intencionais** de manutenção.

## Como executar localmente

```bash
python main.py
python -m pip install coverage
python -m coverage run --source=biblioteca -m unittest discover -s tests -v
python -m coverage xml -o coverage.xml
python -m coverage report -m
```

## O que observar no SonarQube

- `biblioteca/diagnostico_didatico.py`: função de complexidade cognitiva alta, com vários blocos condicionais aninhados. Comparar antes/depois ao refatorar.
- Mesmo módulo: duas funções de busca com estruturas repetidas. Discutir possibilidade de extrair lógica compartilhada (a indicação de duplicação depende dos limiares do SonarQube).
- Cobertura: o GitHub Action agora executa os testes e produz `coverage.xml` antes da análise. Nem todos os ramos do módulo didático têm testes.
- Os indicadores concretos e a quantidade de alertas dependem do perfil de qualidade aplicado no serviço. Não há garantia de um número específico de issues.

## Configuração

1. Crie um repositório GitHub novo com branch `main`, sem outro workflow Sonar.
2. Importe esse repositório no SonarQube Cloud e **escolha CI-based analysis/GitHub Actions**; se houver Automatic Analysis, desligue em **Administration > Analysis Method**.
3. Copie a Project Key exata do SonarQube para `sonar-project.properties` (substitua `SUBSTITUA_PELA_PROJECT_KEY_EXATA`). A Organization Key já está configurada com o valor usado nas telas da aula; confira se corresponde à sua organização.
4. Gere um token autorizado para executar análises do novo projeto e crie no repositório GitHub `Settings > Secrets and variables > Actions > New repository secret`, com **Name** `SONAR_TOKEN` e **Secret** igual ao token.
5. Confirme que o workflow `.github/workflows/sonar.yml` usa `secrets.SONAR_TOKEN` e **não repete** a Project Key em `args`.
6. Faça commit/push para `main`; em `Actions`, confira o workflow e depois veja o projeto no SonarQube.

> Segurança: nunca copie o token para um arquivo versionado. Se algum token foi publicado em imagem ou chat, revogue e substitua por um novo.

> O comando de análise usa `SonarSource/sonarqube-scan-action@v6`; se a organização exigir uma versão mais recente ou SHA fixo, consulte a documentação oficial e atualize essa referência.
