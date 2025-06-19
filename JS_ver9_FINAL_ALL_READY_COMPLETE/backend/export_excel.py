from flask import Blueprint, send_file
from models import Student
from app import db
import pandas as pd
import io

excel_bp = Blueprint('excel_bp', __name__)

@excel_bp.route("/api/export_excel/<int:exam_id>/<class_name>", methods=["GET"])
def export_excel(exam_id, class_name):
    students = Student.query.filter_by(exam_id=exam_id, class_name=class_name).all()
    if not students:
        return {"error": "No data found."}, 404

    data = [{
        "이름": s.name,
        "반": s.class_name,
        "시험 ID": s.exam_id,
        "점수": s.score
    } for s in students]

    df = pd.DataFrame(data)
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='성적표', index=False)

    output.seek(0)
    return send_file(output, download_name=f"{class_name}_exam_{exam_id}_scores.xlsx", as_attachment=True)