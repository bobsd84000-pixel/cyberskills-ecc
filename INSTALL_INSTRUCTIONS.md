# Ruflo Installation — Path A (Claude Code Plugins)

## Pour exécuter dans Claude Code Web/Desktop

**Cet environnement n'a pas accès aux commandes slash. Voici comment faire:**

### Étape 1: Ouvrir Claude Code Web
1. Aller à: https://claude.ai/code
2. Ou utiliser l'extension Claude Code (VS Code, JetBrains)

### Étape 2: Exécuter dans le chat Claude Code

Copie-colle ces commandes une par une dans le chat:

```
/plugin marketplace add ruvnet/ruflo
```

Attends la confirmation ✅

```
/plugin install ruflo-core@ruflo
```

Attends l'installation (peut prendre quelques secondes)

### Étape 3: Vérifier l'installation

```
/help ruflo
```

Ou:

```
/plugin list
```

Tu devrais voir `ruflo-core` dans la liste.

### Étape 4: Initialiser le projet

```
/ruflo init
```

Suis les instructions du wizard.

## Commandes disponibles après installation

```bash
/ruflo status          # Vérifier la santé du système
/ruflo agent spawn -t coder --name mon-agent
/ruflo memory search -q "votre recherche"
/help agents           # Voir tous les types d'agents (98+)
/help ruflo            # Aide Ruflo complète
```

## Si tu n'as pas Claude Code

### Alternative: Path B (CLI Full)

```bash
# Depuis ce dossier
cd /home/user/cyberskills-ecc
npx ruflo init --wizard
```

**Note**: Cela peut échouer si tu n'as pas d'authentification npm pour les packages privés `@claude-flow/*`.

## Troubleshooting

**Problème**: Commandes slash non disponibles
- **Solution**: Utilise Claude Code web (https://claude.ai/code) ou l'extension

**Problème**: Plugin install échoue
- **Solution**: Attends quelques secondes entre les commandes
- Redémarre Claude Code si nécessaire

**Problème**: MCP tools non disponibles
- **Solution**: `ruflo-core` enregistre son propre serveur MCP
- Redémarre Claude Code pour activer les tools

## Next Steps

1. ✅ Installation complète dans Claude Code
2. Exécute `/ruflo init` pour configurer
3. Explore les agents: `/help agents`
4. Crée un agent: `/ruflo agent spawn -t coder`
5. Teste la mémoire: `/ruflo memory store --key test --value "hello"`

---

**Status**: Prêt pour installation dans Claude Code  
**Date**: 2026-09-01
