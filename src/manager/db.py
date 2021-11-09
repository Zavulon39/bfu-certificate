import os
from datetime import datetime

SERVER = ''
DATABASE = ''
USERNAME = ''
PASSWORD = ''
# у меня не получилось поставить этот пакет, тк там нужны зависимости от "Microsoft C++ Build Tools", а мне их впадлу ставить
pyodbc = None


class DBManager:
    """ Менеджер для работы с базой данных """

    def get_request_spr(self):
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

    def update_request_spr(self, sprID, status):
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
