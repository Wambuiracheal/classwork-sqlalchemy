from app import app,db,Student

students = [
    {"name": "John", "age": 20, "teacher": "Anne"},
    {"name": "Jane", "age": 40, "teacher": "Joseph"},
    {"name": "Andrew", "age": 29, "teacher": "Alex"},
    {"name": "Ian", "age": 35, "teacher": "Antony"},
]

with app.app_context():
    for student in students:
        if not Student.query.filter_by(name=student["name"]).first():
            db.session.add(Student(**student))
            db.session.commit()
            print("Seeding Complete!!")