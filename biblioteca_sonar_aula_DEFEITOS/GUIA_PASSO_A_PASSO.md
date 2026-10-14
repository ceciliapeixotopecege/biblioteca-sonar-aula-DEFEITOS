# Guia para criar o projeto sem conflitos GitHub Actions × SonarQube Cloud

## Etapa 1 — Repositório GitHub

1. Acesse GitHub > **New repository**.
2. Nome sugerido: `biblioteca-sonar-aula`. Escolha **Public** ou **Private** conforme sua preferência.
3. Não marque README, `.gitignore` ou licença na criação (eles já estão no ZIP).
4. Faça o upload **do conteúdo da pasta `biblioteca_sonar_aula`**, não da pasta como um único arquivo compactado. Verifique que `.github/workflows/sonar.yml` está no caminho correto. Se o GitHub Web omitir arquivos ocultos durante upload, crie manualmente essas pastas ou use Git local.
5. Faça commit na branch `main`. O primeiro Actions pode falhar até configurar SonarQube e token; para evitar o erro, conclua as etapas 2–4 antes de habilitar o workflow, ou aceite a primeira falha transitória.

## Etapa 2 — Projeto SonarQube Cloud

1. Acesse SonarQube Cloud > Projects > **Analyze new project / Import project** e importe **o novo repositório** do GitHub.
2. Selecione a organização correta e o repositório `biblioteca-sonar-aula`.
3. Escolha **CI-based analysis / GitHub Actions**, não Automatic Analysis.
4. Caso a opção Automatic Analysis tenha sido ativada, abra o projeto > **Administration > Analysis Method** e desligue a análise automática. Os rótulos exatos podem variar.
5. Encontre a **Project Key real** no SonarQube (pode incluir prefixo de organização ou não). Copie exatamente como fornecida — não monte manualmente.
6. Confira a **Organization Key**, que identifica a organização, e não o projeto.

## Etapa 3 — Configuração do código

1. No GitHub, edite `sonar-project.properties` na raiz.
2. Substitua **somente** o valor `SUBSTITUA_PELA_PROJECT_KEY_EXATA` pelo Project Key visto no SonarQube.
3. Confirme que `sonar.organization=ceciliapeixotopecege` é exatamente sua Organization Key.
4. **Não coloque** `sonar.projectKey` nem `sonar.organization` no workflow YAML: aqui eles ficam centralizados no `.properties`.
5. Faça commit da edição.

## Etapa 4 — Token e permissão

1. No SonarQube, gere um token de usuário com permissão de execução de análise no projeto **ou** um token de análise específico desse projeto.
2. Copie o token (ele será exibido no momento da criação).
3. GitHub > repositório > **Settings > Secrets and variables > Actions > New repository secret**.
4. Nome: `SONAR_TOKEN` (exatamente assim); Valor: token criado no SonarQube; clique em **Add secret**.
5. A ausência do valor na lista GitHub é normal: secrets não são exibidos novamente. Jamais imprima o token em logs.

## Etapa 5 — Executar

1. Com o workflow ativo, faça um commit em `main` (pode editar uma linha de texto no README).
2. Abra GitHub > **Actions > Python Tests and SonarQube Cloud**.
3. Confirme três passos: `Run tests and generate coverage.xml`, `SonarQube Cloud scan`, e execução verde.
4. Vá ao SonarQube Cloud, abra o novo projeto e veja **Issues**, **Coverage** e **Duplications**.

## Diagnóstico rápido

| Mensagem | Causa comum | Ação |
|---|---|---|
| `NOT_FOUND` | Project Key errada ou projeto não acessível | Conferir Project Key exata no SonarQube e permissões |
| `Not authorized` | Token ausente, inválido ou sem permissão | Conferir secret `SONAR_TOKEN` e permissão Execute Analysis |
| `Automatic Analysis is enabled` | Modos de análise conflitantes | Desligar Automatic Analysis; manter GitHub Actions |
| `coverage.xml` ausente | Testes/coverage não foram executados | Conferir passo coverage antes da análise |
| `0 issues` | Nenhum problema detectado pelo perfil vigente | Conferir escopo, perfil e o arquivo didático; não significa ausência de bugs |
| Workflow não aparece | YAML fora da pasta `.github/workflows` ou sem evento | Conferir caminho e branch `main` |

## Boas práticas de sala de aula

- Use **uma** organização e **um projeto Sonar** para cada repositório analisado.
- Defina **um** método de análise por projeto: GitHub Actions OU Automatic Analysis.
- Mantenha Project Key no `sonar-project.properties`, não duplicada no workflow.
- Use secret `SONAR_TOKEN` para autenticação; token exposto deve ser revogado.
- Antes de pedir que os alunos corrijam os problemas, confira quais issues o perfil de qualidade realmente gerou na sua organização.
