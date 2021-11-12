import os
from datetime import datetime, date

SERVER = ''
DATABASE = ''
USERNAME = ''
PASSWORD = ''
pyodbc = None


class DBManager:
    """ Менеджер для работы с базой данных """

    @staticmethod
    def get_request_spr() -> list[tuple]:
        """ Получает все заявки на справку """
        try:
            smss = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                  'SERVER=' + SERVER + ';'
                                                       'DATABASE=' + DATABASE + ';'
                                                                                'UID=' + USERNAME + ';PWD=' + PASSWORD)
            cursor = smss.cursor()

            tsql = f"select dS.ID, dS.CreatedOn, cp.LastName, cp.FirstName, cp.PatrName, cp.DateOfBirth, dS.CopiesCount, (select Name from docs_SprTypes where id=dS.TypeId) as Type  from docs_SprRequests dS " \
                   f" inner join stud_Students ss on ss.Id=dS.StudentId" \
                   f" inner join core_Persons cp on cp.id = ss.core_PersonId" \
                   f" where dS.StatusId=1 and dS.IsDeleted=0 and dS.CreatedOn > '01.09.2021' and dS.TypeId in (1, 6)"
            with cursor.execute(tsql):
                rows = cursor.fetchall()
                # print(rows, sep='\n')
                return [(row[0], row[1], f"{row[2]} {row[3]} {row[4]}", row[5], row[6], row[7]) for row in rows]
        except Exception as e:
            print(e)
            return [(1, datetime.now(), 'Ошибка, в запросе select', date.today(), 0, -1)]

    @staticmethod
    def dev_get_request_spr():
        """ Функция для разработки """
        return [
            (1, datetime.now(), 'Костылева', 'Екатерина', 'Михайловна', date(*reversed(list(map(int, '17.04.1997 0:00:00'.split(' ')[0].split('.'))))), 2, 'Отпечатана'),
            (2, datetime.now(), 'Костылева', 'Елизавета', 'Максимовна', date(*reversed(list(map(int, '05.03.2001 0:00:00'.split(' ')[0].split('.'))))), 4, 'Заказана')
        ]

    @staticmethod
    def update_request_spr(sprID, status):
        """ Обновляет запись """
        try:
            smss = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                  'SERVER=' + SERVER + ';'
                                                       'DATABASE=' + DATABASE + ';'
                                                                                'UID=' + USERNAME + ';PWD=' + PASSWORD)
            cursor = smss.cursor()

            tsql = f"UPDATE docs_SprRequests set StatusId={status}, WhoPrinted='KANTIANA\{os.getenv('username')}', CompletedOn='{datetime.now()}' where Id={int(sprID)}"
            print(sprID)
            cursor.execute(tsql)
            cursor.commit()
            smss.close()
        except Exception as e:
            print('update', e)
