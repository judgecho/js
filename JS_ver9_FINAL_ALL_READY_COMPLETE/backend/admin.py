from flask import Blueprint, request, jsonify
from models import Student
from app import db

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route("/api/students", methods=["GET"])
def get_students():
    class_filter = request.args.get("class")
    if class_filter:
        students = Student.query.filter_by(class_name=class_filter).all()
    else:
        students = Student.query.all()
    return jsonify([{
        "id": s.id,
        "name": s.name,
        "class_name": s.class_name,
        "exam_id": s.exam_id,
        "score": s.score
    } for s in students])

@admin_bp.route("/api/students", methods=["POST"])
def create_student():
    data = request.json
    student = Student(
        name=data["name"],
        class_name=data["class_name"],
        exam_id=data["exam_id"],
        score=data.get("score", 0)
    )
    db.session.add(student)
    db.session.commit()
    return jsonify({"message": "Student created"}), 201

@admin_bp.route("/api/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": "Not found"}), 404
    data = request.json
    student.name = data.get("name", student.name)
    student.class_name = data.get("class_name", student.class_name)
    student.exam_id = data.get("exam_id", student.exam_id)
    student.score = data.get("score", student.score)
    db.session.commit()
    return jsonify({"message": "Student updated"})

@admin_bp.route("/api/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": "Not found"}), 404
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": "Student deleted"})