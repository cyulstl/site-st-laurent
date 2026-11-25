# Site St-Laurent — pages

Les pages des éléments HTML du site Wix de l'équipe St-Laurent (branche `site`).

Chaque élément du site ne contient qu'un petit chargeur. Le chargeur demande sa page à l'application Web de
l'Admin. Worksheet, qui la lit ici (`https://raw.githubusercontent.com/cyulstl/site-st-laurent/site/<page>.html`).
Une page modifiée ici est sur le site en 10 minutes au plus, sans rien coller dans Wix ni dans Apps Script.

| Fichier | Page du site |
| --- | --- |
| `horaire_equipe.html` | Horaire (calendrier) |
| `vacances.html` | Vacances |
| `comp.html` | Comp |
| `echanges.html` | Échanges |
| `equipes54.html` | Équipes 5-4 |
| `heures_ot.html` | Heures d'OT |
| `conges.html` | Congés |

Rien de privé ici : ces pages sont déjà visibles sur le site. La page Contacts (clé privée) n'y est pas.

## Français / English

Chaque page a un bouton FR | EN en haut à droite (le choix est gardé sur l'appareil ; `…&lang=en` dans un lien
ouvre la page en anglais). Les pages restent écrites en français : en anglais, chaque texte affiché est remplacé
par sa traduction.

- `outils/langue.html` : le bouton et le traducteur, le même dans toutes les pages.
- `outils/en/<page>.js` : l'anglais de chaque page (`commun.js` : partagé). `{x}` = une partie qui change.
- `python3 outils/langue.py` : recopie le bouton et les listes dans les pages (à faire après chaque changement).
