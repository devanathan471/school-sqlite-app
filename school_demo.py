import sqlite3
class SchoolDatabase:
    def __init__(self,db_name="school.db"):
        self.conn=sqlite3.connect(db_name)
        self.cursor=self.conn.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON;")
        self.create_table()
    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS subjects(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS students(id INTEGER, name TEXT NOT NULL, score INTEGER, sub_id INTEGER, FOREIGN KEY (sub_id) REFERENCES subjects(id))")
        self.conn.commit()
    def seed_data(self):
        subjects=[("computer science",),("history",),("mathematics",)]
        self.cursor.executemany("INSERT OR IGNORE INTO subjects (name) VALUES(?)",(subjects))
        students=[("ana",78,1),("ben",85,2),("cole",97,3)]
        self.cursor.executemany("INSERT OR IGNORE INTO students (name,score,sub_id) VALUES (?,?,?)",(students))
        self.conn.commit()
   # def query_data(self):
        #self.cursor.execute("SELECT students.name ,students.score ,subjects.name FROM students INNER JOIN subjects ON students.sub_id = subjects.id ORDER BY students.score DESC")
        #a = self.cursor.fetchall()
        #for  e in a:
         #   print(f" name:{e[0]}, score:{e[1]}, subject:{e[2]}")
    def view(self):
        print(" want to view")
        try:
         n = int(input(" enter 1 to view / 2 to skip "))
         if n == 1:
          self.cursor.execute("SELECT students.name ,students.score ,subjects.name FROM students INNER JOIN subjects ON students.sub_id = subjects.id WHERE students.score > 75 ORDER BY students.score DESC")
          b = self.cursor.fetchall()
          for h in b:
             print(f" name:{h[0]}, score:{h[1]}, subject:{h[2]}")
         else:
            print("skipping view ")
        except ValueError:
           print("invalid input ")
    def delete(self):
        print(" want to delete")
        try:
         n = int(input(" enter 1 to delte / 2 to skip "))
         if n == 1:
            name = input(" enter the name to delete ")
            self.cursor.execute(" DELETE FROM students WHERE name = ?",(name,))
            self.conn.commit()
         else:
             print(" skipping delete")
        except ValueError:
            print("invalid input")
    def update(self):
        print(" want to update")
        try:
            l = int(input(" enter 1 to update / 2 to skip "))
            if l == 1:
             name = input(" enter the name  ")
             sub_id = int(input(" enter the subject id "))
             score = int(input(" enter the score "))
             self.cursor.execute(" UPDATE students SET sub_id=? , score=? WHERE name=?",(sub_id,score,name))
             self.conn.commit()
            else:
                print("skipping update")
        except ValueError:
            print("invalid input")
if __name__ == "__main__":
    db =SchoolDatabase()
    db.seed_data()
    #db.query_data()
    db.view()
    db.delete()
    db.update()