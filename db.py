import psycopg2

#connetct to the db
con = psycopg2.connect(
    host = "localhost",
    database = "mercado",
    user = "postgres",
    password = "admin")

#cursor
cur = con.cursor()

#execute query
cur.execute("select id, descricao, status from categoria")

rows = cur.fetchall()

for r in rows:
    print ("id " + str(r[0]) + " descricao " + str(r[1]) + " status " + str(r[2]))

#close the cursor
cur.close()

#close the connection
con.close()