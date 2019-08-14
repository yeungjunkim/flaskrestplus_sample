# from git import Repo
# repo = Repo('.')  # if repo is CWD just do '.'

# repo.index.add(['bla2.txt'])
# repo.index.commit('bla2.txt')
# origin = repo.remote('origin')
# origin.push()

import subprocess
from pexpect import popen_spawn


user = 'yeungjunkim'
password = 'ralalwjd!2'

cmd = "cd /home/poo97/PythonGit/pygit/src/flaskrestplus_sample"
returned_value = subprocess.call(cmd, shell=True)  # returns the exit code in unix

cmd = "git pull "
subprocess.call(cmd, shell=True)

cmd = "git add bla.txt" 
subprocess.call(cmd, shell=True)

cmd = 'git commit -m "python project update"'
subprocess.call(cmd, shell=True)

cmd = "git remote set-url origin https://github.com/yeungjunkim/flaskrestplus_sample.git"
subprocess.call(cmd, shell=True)

cmd = "git push "
subprocess.call(cmd, shell=True)
# child_process = popen_spawn.PopenSpawn(cmd)
# child_process.expect("Username")
# child_process.sendline(user)
# child_process.expect("Password")
# child_process.sendline(password)
print('returned value:', returned_value)

print('end of commands')


import MySQLdb

encoding = "utf-8" 

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                        user="testuser",         # your username
                        passwd="testpassword",  # your password
                        db="model_storage",        # name of the data base
					    charset='utf8',
   		    		    use_unicode=True)
# you must create a Cursor object. It will let
#  you execute all the queries you need
mycursor = db.cursor()

sql = "INSERT INTO model_list (file_name, model_name, model_version, model_writer, create_date, model_desc, args_desc) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = ('bla.txt', "keras_test_model", "0.0.1", "tonykim", "2019.08.14 11:22:22", "케라스 기반 테스트", "test_z, test_y")

mycursor.execute(sql, val)

db.commit()

print(mycursor.rowcount, "record inserted.")

