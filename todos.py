import os
import sys
import fire
import sqlite3
from colored import fg, bg, attr

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')
conn = sqlite3.connect(DEFAULT_PATH)
cur = conn.cursor()

def create_todos():
    sql = """
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY,
            body TEXT NOT NULL,
            due_date TEXT NOT NULL,
            status TEXT DEFAULT "incomplete",
            user_id INTEGER,
            project_id INTEGER
        )
    """
    cur.execute(sql)

def create_users():
    sql = """
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            user_name TEXT NOT NULL,
            gender TEXT NOT NULL,
            birthday TEXT NOT NULL,
            email TEXT NOT NULL,
            starting_date TEXT NOT NULL

        )

    """
    cur.execute(sql)

def create_project_id():
    sql = """
        CREATE TABLE IF NOT EXISTS projects (

        project_id INTEGER PRIMARY KEY,
        project_name TEXT NOT NULL
        )
    """
    cur.execute(sql)



def create_tables():
    create_todos()
    create_users()
    create_project_id()


create_tables()

def show_help_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print ('%s Todo List Options: %s' % (fg(208), attr(0)))
    print ('%s * %s'  % (fg(126), attr(0)))
    print ('%s 1. List all todos: %s' % (fg(208), attr(0)))
    print ('%s \t python3 todos.py list %s' % (fg(15), attr(0)))
    print ('%s 2. Add a new todo: %s' % (fg(208), attr(0)))
    print ('%s \t python3 todos.py add "My Todo Body"%s' % (fg(15), attr(0)))
    print ('%s 3. Delete a todo: %s' % (fg(208), attr(0)))
    print ('%s \t python3 todos.py delete 1 %s' % (fg(15), attr(0)))
    print ('%s 4. Mark a todo complete: %s' % (fg(208), attr(0)))
    print ('%s \t python3 todos.py do 1 %s' % (fg(15), attr(0)))
    print ('%s 5. Mark a todo uncomplete: %s' % (fg(208), attr(0)))
    print ('%s \t python3 todos.py undo 1 %s' % (fg(15), attr(0)))
    print ('%s-%s'% (fg(208), attr(0)))
    print ('%s User Options: %s' % (fg(40), attr(0)))
    print ('%s * %s'  % (fg(126), attr(0)))
    print ('%s 1. List all uers: %s' % (fg(40), attr(0)))
    print ('%s \t python3 todos.py list_user %s' % (fg(15), attr(0)))
    print ('%s 2. Add a new user: %s' % (fg(40), attr(0)))
    print ('%s \t python3 todos.py add_user "My new user name"%s' % (fg(15), attr(0)))
    print ('%s 3. Delete a user: %s' % (fg(40), attr(0)))
    print ('%s \t python3 todos.py delete_user 1 %s' % (fg(15), attr(0)))
    print ('%s-%s'% (fg(40), attr(0)))
    print ('%s Project Options: %s' % (fg(164), attr(0)))
    print ('%s * %s'  % (fg(208), attr(0)))
    print ('%s 1. List all projects: %s' % (fg(164), attr(0)))
    print ('%s \t python3 todos.py staff %s' % (fg(15), attr(0)))
    print ('%s 2. Add a new project: %s' % (fg(164), attr(0)))
    print ('%s \t python3 todos.py add_project "My new project name"%s' % (fg(15), attr(0)))
    print ('%s 3. Delete a project: %s' % (fg(164), attr(0)))
    print ('%s \t python3 todos.py delete_project 1 %s' % (fg(15), attr(0)))
    print ('%s-%s'% (fg(164), attr(0)))


def add(body,date,user_id,project_id):
    print('%s Adding Todo: %s' % (fg(33), attr(0)))
    sql = """
        INSERT INTO todos (body, due_date, user_id, project_id) VALUES (?,?,?,?)
    """
    cur.execute(sql,(body, date,user_id,project_id))
    conn.commit()

def delete(id):
    print('%s Deleting Todo: %s' % (fg(33), attr(0)))
    sql = """
        DELETE FROM todos
            WHERE id = ?
    """
    cur.execute(sql,(id,))
    conn.commit()

def show_list(thingy = None):
    print('%s Showing List: %s' % (fg(33), attr(0)))
    if thingy == None:
        # print('%s Showing List: %s' % (fg(33), attr(0)))
        sql = """
            SELECT * FROM todos
            ORDER BY due_date DESC
        """
        cur.execute(sql)
        results = cur.fetchall()

    if thingy == "completed":
        # print('%s Showing List: %s' % (fg(33), attr(0)))
        sql = """
            SELECT * FROM todos
            WHERE status = ?
            ORDER BY due_date DESC
        """
        cur.execute(sql,("completed",))
        results = cur.fetchall()

    

    if type(thingy) == int :
        sql = """
            SELECT * FROM todos
            WHERE project_id = ?
        """
        cur.execute(sql,(thingy,))
        results = cur.fetchall()

    
    for row in results:
        print(row[0],row[1],row[2], row[3],row[4], row[5])
        



def do(id):
    print('%s Get done: %s' % (fg(33), attr(0)))
    sql = """
        UPDATE todos
            SET status = "completed"
        WHERE id = ?
    """
    cur.execute(sql,(id,))
    conn.commit()
    
def undo(id):
    print('%s Undo todo: %s' % (fg(33), attr(0)))
    sql = """
        UPDATE todos
            SET status = "incomplete"
        WHERE id = ?
    """
    cur.execute(sql,(id,))
    conn.commit()

def add_user(name,gender,bday,email, date):
    print('%s Adding New User: %s' % (fg(33), attr(0)))
    sql = """
        INSERT INTO users (user_name,gender,birthday,email,starting_date) VALUES (?,?,?,?,?)
    """
    cur.execute(sql,(name,gender,bday,email,date))
    conn.commit()

def delete_user(id):
    print('%s Deleting User: %s' % (fg(33), attr(0)))
    sql = """
        DELETE FROM users
        WHERE user_
        id = ?
    """
    cur.execute(sql,(id,))
    conn.commit()

def list_user(thingy = None):
    print('%s Showing Users: %s' % (fg(33), attr(0)))
    if thingy == None:
        sql = """
        SELECT * FROM users
        ORDER BY due_date DESC

    """
    cur.execute(sql)
    results = cur.fetchall()

    if thingy == "completed":
        sql = """
            SELECT * FROM todos
            WHERE status = ?
        """
    cur.execute(sql("completed"))
    results = cur.fetchall()


    # if type(thingy) == int:
    #     sql = """
    #     SELECT * FROM users
    #     WHERE user_id = ?
        
    # """
    # cur.execute(sql,(id,))
    # results = cur.fetchall()

    for row in results:
        print(row[0],row[1],row[2], row[3])


def add_project(name):
    print('%s Adding New Project: %s' % (fg(33), attr(0)))
    sql = """
        INSERT INTO projects (project_name) VALUES (?)
    """
    cur.execute(sql,(name,))
    conn.commit()

def delete_project(id):
    print('%s Deleting New Project: %s' % (fg(33), attr(0)))
    sql = """
        DELETE FROM projects
        WHERE project_id = ?
    """
    cur.execute(sql,(id,))
    conn.commit()

def list_project(thingy = None):
    print('%s Showing Projects: %s' % (fg(33), attr(0)))
    # if thingy == None:
    #     sql = """
    #     SELECT * FROM projects
    #     ORDER BY project_id ASC

    # """
    # cur.execute(sql)
    # results = cur.fetchall()

    if thingy == None:
        sql = """
            SELECT user_name, project_name 
            FROM todos 
            LEFT JOIN users 
            ON users.user_id = todos.user_id
            left join projects
            on todos.project_id = projects.project_id
        """
        cur.execute(sql)
        results = cur.fetchall()
        # print(results)
    for row in results:
        print(row[0],row[1])

def user_not_working():
    sql = '''
    SELECT user_name FROM users LEFT JOIN todos ON users.user_id = todos.user_id
   WHERE todos.project_id is NULL
    '''
    cur.execute(sql)
    results = cur.fetchall()   
    print(results)


if __name__ == '__main__':
    try:
        arg1 = sys.argv[1]
        if arg1 == '--help':
            show_help_menu()
        else:
            fire.Fire({
                'add': add,
                'do': do,
                'delete': delete,
                'undo': undo,
                'list': show_list,
                'add_user': add_user,
                'delete_user': delete_user,
                'list_user': list_user,
                'add_project': add_project,
                'delete_project': delete_project,
                'staff': list_project,
                'who_to-fire': user_not_working


                
                
            })
    except IndexError:
        show_help_menu()
        sys.exit(1)

