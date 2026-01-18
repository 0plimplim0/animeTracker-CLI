from utils import utils

logger = utils.initLogs()

def getData(data):
    connection = utils.getConnection()
    action = data['action']
    match action:
        case 'add':
            addAnime(data, connection)
        case 'watch':
            watchAnime(data, connection)
        case 'set':
            setAnime(data, connection)
        case 'search':
            searchAnime(data, connection)
        case 'list':
            listAnimes(data, connection)
    utils.closeConnection(connection)

def addAnime(data, connection):
    # Falta verificar el formato de las fechas
    cursor = connection.cursor()
    status_list = ['plan_to_watch', 'watching', 'completed', 'dropped']
    if  not data['status'] or (data['status'] not in status_list):
        data['status'] = 'plan_to_watch'
    cursor.execute('insert into animes(title, episodes, status, notes, started_at, finished_at) values(?, ?, ?, ?, ?, ?)', (data['title'], data['episodes'], data['status'], data['notes'], data['started_at'], data['finished_at']))
    connection.commit()
    logger.info('El anime se ha agregado correctamente.')
def watchAnime(data, connection, ):
    if (data['num'] < 1):
        print('Argumentos inválidos.')
        return
    cursor = connection.cursor()
    cursor.execute('select current_episode from animes where title = ?', (data['title'],))
    current = cursor.fetchone()
    new = current[0] + data['num']
    cursor.execute('update animes set current_episode = ? where title = ?', (new, data['title']))
    connection.commit()
    logger.info('El anime se ha actualizado correctamente.')

def setAnime(data, connection):
    cursor = connection.cursor()
    status_list = ['plan_to_watch', 'watching', 'completed', 'dropped']
    if  not data['status'] or (data['status'] not in status_list):
        data['status'] = 'plan_to_watch'
    cursor.execute('update animes set status = ? where title = ?', (data['status'], data['title']))
    connection.commit()
    logger.info('El estado del anime se ha actualizado correctamente.')

def searchAnime(data, connection):
    cursor = connection.cursor()
    cursor.execute('select * from animes where title = ?', (data['title'],))
    item = cursor.fetchone()
    if not item:
        print('No existe ningún item con ese titulo.')
        return
    print(f'\nID: {item[0]}\nTitulo: {item[1]}\nEpisodios: {item[2]}\nEpisodios vistos: {item[3]}\nEstado: {item[4]}\nNotas: {item[5]}\nEmpezado el: {item[6]}\nTerminado el: {item[7]}\n')

def listAnimes(data, connection):
    cursor = connection.cursor()
    status_list = ['plan_to_watch', 'watching', 'completed', 'dropped']
    if  not data['status'] or (data['status'] not in status_list):
        data['status'] = 'plan_to_watch'
    cursor.execute('select * from animes where status = ?', (data['status'],))
    animes = cursor.fetchall()
    if not animes:
        print("No existe ningún anime con ese estado asignado.")
        return
    for anime in animes:
        print(f'\nID: {anime[0]}\nTitulo: {anime[1]}\nEpisodios: {anime[2]}\nEpisodios vistos: {anime[3]}\nEstado: {anime[4]}\nNotas: {anime[5]}\nEmpezado el: {anime[6]}\nTerminado el: {anime[7]}\n')