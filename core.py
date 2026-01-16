from utils import utils

def getData(data):
    connection = utils.getConnection()
    action = data['action']
    match action:
        case 'add':
            addAnime(data, connection)
        case 'watch':
            pass
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
    print("El anime se ha agregado correctamente.")