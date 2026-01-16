from utils import utils

def getData(data):
    connection = utils.getConnection()
    action = data['action']
    match action:
        case 'add':
            addAnime(data, connection)
        case 'watch':
            watchAnime(data, connection)
        case 'set':
            pass
        case 'search':
            pass
        case 'list':
            pass
    utils.closeConnection(connection)

def addAnime(data, connection):
    # Falta verificar el formato de las fechas
    cursor = connection.cursor()
    status_list = ['plan_to_watch', 'watching', 'completed', 'dropped']
    if  not data['status'] or (data['status'] not in status_list):
        data['status'] = 'plan_to_watch'
    cursor.execute('insert into animes(title, episodes, status, notes, started_at, finished_at) values(?, ?, ?, ?, ?, ?)', (data['title'], data['episodes'], data['status'], data['notes'], data['started_at'], data['finished_at']))
    connection.commit()
    # Cambiar el print a info.log 
    print("El anime se ha agregado correctamente.")

def watchAnime(data, connection):
    if (data['num'] < 1):
        print('Argumentos inválidos.')
        return
    cursor = connection.cursor()
    cursor.execute('select current_episode from animes where title = ?', (data['title'],))
    current = cursor.fetchone()
    new = current[0] + data['num']
    cursor.execute('update animes set current_episode = ? where title = ?', (new, data['title']))
    connection.commit()
    # Cambiar el print a info.log 
    print('Anime actualizado correctamente.')