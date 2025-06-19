from flask import Blueprint, jsonify, send_file
from models import db, Student
from io import BytesIO
from reportlab.pdfgen import canvas

stats_bp = Blueprint("stats", __name__)

@stats_bp.route("/api/stats/<int:exam_id>", methods=["GET"])
def get_exam_stats(exam_id):
    students = Student.query.filter_by(exam_id=exam_id).all()
    if not students:
        return jsonify({"error": "데이터 없음"}), 404

    scores = [s.score for s in students]
    avg_score = round(sum(scores) / len(scores), 2)
    max_score = max(scores)
    min_score = min(scores)

    return jsonify({
        "count": len(students),
        "average": avg_score,
        "max": max_score,
        "min": min_score
    })

@stats_bp.route("/api/pdf_report/<int:exam_id>/<class_name>", methods=["GET"])
def generate_pdf_report(exam_id, class_name):
    students = Student.query.filter_by(exam_id=exam_id, class_name=class_name).all()
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, 820, f"[시험 리포트] {class_name}")
    p.setFont("Helvetica", 12)
    p.drawString(100, 800, f"응시자 수: {len(students)}명")

    y = 770
    for s in students:
        p.drawString(100, y, f"{s.name}: {s.score}점")
        y -= 20
        if y < 100:
            p.showPage()
            y = 800

    p.save()
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name="report.pdf", mimetype="application/pdf")

@stats_bp.route("/api/class_scores/<int:exam_id>", methods=["GET"])
def get_class_average_scores(exam_id):
    students = Student.query.filter_by(exam_id=exam_id).all()
    if not students:
        return jsonify({"error": "데이터 없음"}), 404

    class_scores = {}
    for s in students:
        class_scores.setdefault(s.class_name, []).append(s.score)

    result = []
    for class_name, scores in class_scores.items():
        avg = round(sum(scores) / len(scores), 2)
        result.append({"class_name": class_name, "average_score": avg})

    return jsonify(result)