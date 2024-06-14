# https://docs.python.org/3/library/sqlite3.html
DB_FILENAME = '24-Databases_and_SQL.db'

import sqlite3
# Talking to the database happens through a "connection"
con = sqlite3.connect(DB_FILENAME)
# A cursor is the object we use to execute a query.
cur = con.cursor()

# # This returns an iterator!
# cur.execute("YOUR QUERY")

# # Save (commit) the changes
# con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
# con.close()

# A note on syntax:
# Use ''' ''' to have multiple lines without issue.
print(cur.execute('''
SELECT *
FROM cones;
'''))

print(cur.execute('''
SELECT *
FROM cones;
''').fetchall())

def show_query(query):
    result = cur.execute(query)
    for row in result:
        print(row)
    return result







# from random import randint, choice
# staff = [
#     'Michael',
#     'Gerald',
#     'Alex',
#     'Brian',
#     'Julia',
#     'Sophia',
#     'Shreya',
#     'Vandana',
#     'Cameron',
#     'Nick'
# ]
# get_staff = lambda: choice(staff)
# get_cone = lambda: randint(1, 6)
# get_month = lambda: randint(1, 12)

# values_list = ",\n".join([ '(\'{}\', {}, {}, {})'.format(get_staff(), tid, get_cone(), get_month()) for tid in range(500) ])

# sql_statement = 'INSERT INTO sales (Cashier, TID, Cone, Month) VALUES {};'.format(values_list)

# print(sql_statement)
