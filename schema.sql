DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS attendance;

CREATE TABLE students (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  grade TEXT NOT NULL,
  parent_name TEXT,
  parent_phone TEXT
);

CREATE TABLE attendance (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  student_id INTEGER NOT NULL,
  date TEXT NOT NULL,
  status TEXT NOT NULL CHECK(status IN ('Present','Absent','Late')),
  notes TEXT,
  FOREIGN KEY (student_id) REFERENCES students (id)
);
