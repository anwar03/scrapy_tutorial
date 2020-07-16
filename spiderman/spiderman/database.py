import sqlite3

conn = sqlite3.connect("spiderman.db")
curr = conn.cursor()

# curr.execute("""
#                 create table quotes_tb(
#                     title text,
#                     author text,
#                     tag text
#                 )
# """)

conn.execute("""
    INSERT INTO quotes_tb values('python title', 'me', 'python')
""")

conn.commit()
conn.close()