# SKILL: VALIDAÇÃO DE EVENTOS

## Objetivo
Verificar a qualidade e confiabilidade das informações de cada evento curado,
garantindo que o público receba dados corretos antes da publicação.

## Quando usar
- Após a curadoria (skill curadoria)
- Antes da formatação final para o Telegram

## Processo de validação

### Passo 1 — Verificação de links
Para cada evento:
- ✅ VÁLIDO: URL completa e específica do evento (ex: ticketandgo.com.br/evento/33a-expotche)
- ⚠️ GENÉRICO: URL de portal sem página específica (ex: agitabrasilia.com) → buscar URL específica
- ❌ INVÁLIDO: "Mais informações", "Clique aqui", sem link → remover o evento

Para links genéricos (⚠️), tente encontrar a URL específica:
- Busque "[nome do evento] Brasília site:[portal]"
- Se encontrar → promova para ✅ com a URL específica
- Se não encontrar → marque como ❌ e remova

### Passo 2 — Verificação de locais
Corrija locais incorretos conhecidos:
- **Expotchê**: local correto é **Pavilhão de Exposições do Parque da Cidade** (não Centro de Convenções Ulysses Guimarães)
- **Rock Saloon**: verificar o local específico da edição atual
- Qualquer local que pareça genérico ou incorreto → buscar confirmação

### Passo 3 — Consistência de datas
- Confirme que o evento realmente acontece no fim de semana buscado
- Eventos de longa duração (ex: "4 a 14 de junho"): ✅ se o fim de semana está dentro do período
- Remova eventos com datas claramente erradas ou já encerrados

### Passo 4 — Classificação final
Classifique cada evento:
- ✅ CONFIRMADO — URL específica real + local correto + data válida
- ⚠️ VERIFICAR — alguma informação incompleta mas evento provavelmente real
- ❌ REMOVER — sem URL específica, local inválido ou data incorreta

## Formato de saída

```
## RELATÓRIO DE VALIDAÇÃO

### ✅ EVENTOS CONFIRMADOS ([N])
- **[Nome]**
  - Data: [data corrigida se necessário]
  - Local: [local correto]
  - Preço: [preço]
  - Link: [URL específica real]

### ⚠️ EVENTOS COM RESSALVA ([N])
- **[Nome]** — [descrição do problema]
  - [informações disponíveis]
  - Recomendação: [o que o leitor deve fazer para confirmar]

### ❌ EVENTOS REMOVIDOS ([N])
- **[Nome]** — Motivo: [razão da remoção]

## ALERTA AO FORMATADOR
- Total confirmado: [N] eventos
- Total com ressalva: [N] eventos
- Total removido: [N] eventos
- Publicar? [SIM se confirmados >= 3 | PARCIAL se 1-2 | NÃO se 0]
```

## Regras
- Nunca valide um link genérico como "Agita Brasília" sem URL específica do evento
- Sempre corrija o local quando souber o correto
- Seja conservador: na dúvida, marque como ⚠️ em vez de ✅
- Não remova eventos apenas por falta de preço — isso é aceitável
- O objetivo é proteger o leitor de informações erradas