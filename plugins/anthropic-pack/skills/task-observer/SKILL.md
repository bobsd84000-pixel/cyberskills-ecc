---
name: task-observer
description: >
  Surveille l'état des tâches en cours (TaskList/TaskGet) et des sessions actives,
  puis rapporte un résumé compact. Se déclenche sur "état des tâches", "task status",
  "où en sont les tâches", "observe les tâches", "task observer".
---

## But

Donner un état des lieux fiable des tâches et sessions en cours sans que l'utilisateur ait à interroger chaque outil manuellement.

## Déroulé

1. Lister les tâches actives (`TaskList`) et leur statut (pending / in_progress / completed).
2. Pour toute tâche `in_progress` ancienne ou bloquée, vérifier sa sortie (`TaskOutput`) pour détecter un blocage.
3. Si des sessions distantes liées sont en cours (PR surveillées, agents lancés), vérifier leur état.
4. Rapporter un résumé court : combien de tâches par statut, laquelle nécessite une action, rien à signaler sinon.

## Règles

- Ne jamais arrêter ou modifier une tâche sans que l'utilisateur le demande explicitement — ce skill observe, il n'agit pas.
- Si aucune tâche active, le dire simplement plutôt que de produire un rapport vide avec des sections inutiles.
- Rester bref : un résumé en 2-3 lignes suffit sauf si plusieurs tâches nécessitent une attention distincte.
