# Copies the FR/EN switch (outils/langue.html) and each page's English list (outils/en/<page>.js) into the pages.
# Usage: python3 outils/langue.py   (from the repo folder)
import re, os, sys
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
bloc = open(os.path.join(R, 'outils/langue.html'), encoding='utf-8').read().strip()
PAGES = {  # page: English lists (in order; later entries win)
  'equipes54.html': ['equipes54'], 'conges.html': ['conges'], 'heures_ot.html': ['heures_ot'],
  'echanges.html': ['echanges'], 'comp.html': ['echanges', 'comp'], 'vacances.html': ['vacances'],
  'horaire_equipe.html': ['horaire_equipe'], 'plan.html': ['horaire_equipe'],
}
seul = sys.argv[1:]
for page, listes in PAGES.items():
    if seul and page not in seul: continue
    f = os.path.join(R, page); s = open(f, encoding='utf-8').read()
    en = '\n'.join(open(os.path.join(R, 'outils/en', l + '.js'), encoding='utf-8').read().strip() for l in ['commun'] + listes
                   if os.path.exists(os.path.join(R, 'outils/en', l + '.js')))
    tout = bloc + '\n<!-- EN:debut — the English of this page (source: outils/en/) -->\n<script>\nwindow.EN_PAGE = [\n' + en + '\n];\n</script>\n<!-- EN:fin -->'
    if '<!-- LANGUE:debut' in s:
        s = re.sub(r'<!-- LANGUE:debut.*?<!-- EN:fin -->', lambda m: tout, s, flags=re.S)
    else:
        i = s.index('</title>') + len('</title>')
        s = s[:i] + '\n' + tout + s[i:]
    open(f, 'w', encoding='utf-8').write(s)
    print(page, 'ok', len(en.splitlines()), 'lignes de traduction')
