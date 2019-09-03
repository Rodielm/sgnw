
import gettext
import os

# msgfmt test_i18n.po -o test_i18n.mo
# locale/fr/LC_MESSAGES
# Set domain , attach base, dir , enable fallback
t = gettext.translation('test_i18n','locale',fallback=True)
_ = t.gettext

print(_('Hello World.'))

# print('Prueba de os:')
# abspath = os.path.abspath(os.path.dirname(__file__))
# localedir = os.path.join(abspath, 'locale')

# cat = gettext.Catalog('noti', localedir)
# _ = cat.gettext
# print(_('Hello World'))

# Buscar como realizar un script de idiomas con babel, una vez hecho
# Generara la plantilla del lenguaje por medio ella.