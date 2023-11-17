from src.build_database.DatabaseLoader import DatabaseLoader
# create new 'instance' of class DatabaseLoader()
loader = DatabaseLoader()
# call method 'get_table_list' in DatabaseLoader
tables = loader.get_table_list()

for table in tables:
    # call method 'get_table_size' in DatabaseLoader
    print(table, loader.get_table_size(table))
