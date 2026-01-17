# School Administration System (Mini-SASAMS)

A simple school administration system to manage student records and attendance.

## Features (MVP)
- Add / Edit / View students
- Record daily attendance (Present / Absent / Late)
- Search students
- Export attendance reports (CSV)

## Tech Stack
- Python (Flask)
- SQLite
- HTML & CSS

## Database Design

### students
- id (PK)
- first_name
- last_name
- grade
- parent_name
- parent_phone

### attendance
- id (PK)
- student_id (FK)
- date
- status
- notes
