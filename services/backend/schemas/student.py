from pymongo.cursor import Cursor


def student_entity(db_item) -> dict:
    return {
        'id': str(db_item['_id']),
        'name': db_item['name'],
        'email': db_item['email'],
        'phone': db_item['phone']
    }


def list_of_students_entity(db_item_list: Cursor) -> list:
    return [student_entity(student) for student in db_item_list]
