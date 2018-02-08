
username = "victim"
password = "'\' OR \'1\'=\'1"

password= password.replace("'", "''")
username= username.replace("'", "''")

test = "SELECT id FROM users WHERE username=%s AND password=%s" % (username, password)
print test
