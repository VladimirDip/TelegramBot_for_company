from utils.db_api.database import session
from utils.db_api.models import Catalogs, Admins


class WorkWithDb:
    def __init__(self):
        self.session_connector = session()

    def get_path_catalogs(self, filter_column, value_row):
        value = self.session_connector.query(Catalogs.path).filter(filter_column == value_row).one()
        print(value[0])
        return value[0]

    def add_new_admin(self, id_user, first_name, last_name, user_name):
        new_admin = Admins(id_user=id_user,
                           first_name=first_name,
                           last_name=last_name,
                           user_name=user_name)

        self.session_connector.add(new_admin)
        self.session_connector.commit()

    def check_admin(self, id_user):
        admin = bool(self.session_connector.query(Admins.id_user).filter_by(id_user = id_user).first())
        return admin
# n = WorkWithDb()
#
# print(n.get_one_value(name_table=Catalogs.path, filter_column=Catalogs.title, value_row='Каталог опор'))
