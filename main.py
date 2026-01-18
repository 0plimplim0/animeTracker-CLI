from utils import utils
import core
import logging
import argparse

utils.initDb()
utils.initLogs()

parser = argparse.ArgumentParser(
    description=utils.banner,
    formatter_class=argparse.RawTextHelpFormatter
)
actions = parser.add_mutually_exclusive_group()
advanced_options = parser.add_argument_group('Opciones avanzadas')

# Opciones utilitarias
parser.add_argument('-v', '--version', action='version', version='AnimeTracker-CLI v1.0.0', help='Muestra la version del programa.')
# Opciones generales [Operaciones]
actions.add_argument('-a', '--add', dest='action', action='store_const', const='add', help='Agrega un anime a la base de datos.')
actions.add_argument('-w', '--watch', dest='action', action='store_const', const='watch', help='Avanza el contador de episodios "n" veces.')
actions.add_argument('-s', '--set', dest='action', action='store_const', const='set', help='Establece el estado actual del anime ingresado.')
actions.add_argument('-f', '--search', dest='action', action='store_const', const='search', help='Busca en la base de datos un anime con el titulo ingresado.')
actions.add_argument('-l', '--list', dest='action', action='store_const', const='list', help='Muestra todos los animes en la base de datos con el estado especificado.')
#Opciones avanzadas [Data]
advanced_options.add_argument('-t', '--title', dest='anime_title', type=str, action='store', help='Titulo del anime a ingresar.')
advanced_options.add_argument('-ep', '--episodes', dest='anime_episodes', type=int, action='store', help='Número de episodios del anime ingresado.')
advanced_options.add_argument('--status', dest='anime_status', type=str,action='store', help='Estado actual del anime ingresado.')
advanced_options.add_argument('--note', dest='anime_notes', type=str, action='store', help='Nota sobre el anime ingresado.')
advanced_options.add_argument('-st', '--started-at', dest='anime_start', type=str, action='store', help='Fecha de cuando se empezo a ver el anime ingresado (AAAA-MM-DD).')
advanced_options.add_argument('-ft', '--finished-at', dest='anime_finish',type=str, action='store', help='Fecha de cuando se acabó de ver el anime ingresado (AAAA-MM-DD).')
advanced_options.add_argument('-en', '--ep-num', dest='episodes_num', type=int, action='store', help='Número de episodios vistos.')

try:
    args = parser.parse_args()
    action = args.action

    match action:
        case 'add':
            data = {
                'action': 'add',
                'title': args.anime_title,
                'episodes': args.anime_episodes,
                'status': args.anime_status,
                'notes': args.anime_notes,
                'started_at': args.anime_start,
                'finished_at': args.anime_finish
            }
        case 'watch':
            data = {
                'action': 'watch',
                'title': args.anime_title,
                'num': args.episodes_num
            }
        case 'set':
            data = {
                'action': 'set',
                'title': args.anime_title,
                'status': args.anime_status
            }
        case 'search':
            data = {
                'action': 'search',
                'title': args.anime_title
            }
        case 'list':
            data = {
                'action': 'list',
                'status': args.anime_status
            }
    core.getData(data)
except Exception as e:
    logging.error(e)
    print('Ha ocurrido un error.\nMás información en /logs/error.log')