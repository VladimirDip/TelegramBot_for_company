from utils.db_api.database import session
from utils.db_api.models import Catalogs

session_connector = session()


class WorkWithDb:

    def get_one_value(self, name_table, filter_column, value_row):
        value = session_connector.query(name_table).filter(filter_column == value_row).one()
        return value[0]

# n = WorkWithDb()
#
# print(n.get_one_value(name_table=Catalogs.path, filter_column=Catalogs.title, value_row='Каталог опор'))

