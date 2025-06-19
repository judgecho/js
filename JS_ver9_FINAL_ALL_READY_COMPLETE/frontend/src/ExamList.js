import React, { useEffect, useState } from "react";

function ExamList({ role }) {
  const [exams, setExams] = useState([]);
  const [message, setMessage] = useState("");

  const fetchExams = async () => {
    const res = await fetch("/api/exams", {
      headers: {
        Authorization: "Bearer " + localStorage.getItem("token"),
      },
    });
    const data = await res.json();
    if (Array.isArray(data)) {
      setExams(data);
    }
  };

  const handleClone = async (examId) => {
    const res = await fetch(`/api/exams/${examId}/clone`, {
      method: "POST",
      headers: {
        Authorization: "Bearer " + localStorage.getItem("token"),
      },
    });
    const data = await res.json();
    if (res.ok) {
      setMessage(`시험 복사 완료! 새 시험 ID: ${data.new_exam_id}`);
      fetchExams();
    } else {
      setMessage(data.error || "복사 실패");
    }
  };

  useEffect(() => {
    fetchExams();
  }, []);

  return (
    <div className="max-w-2xl mx-auto">
      <h2 className="text-xl font-semibold mb-3">시험 목록</h2>
      {message && <p className="text-green-600 mb-3">{message}</p>}
      <ul className="space-y-3">
        {exams.map((exam) => (
          <li
            key={exam.id}
            className="flex flex-col sm:flex-row sm:justify-between sm:items-center border p-3 rounded bg-white shadow"
          >
            <span className="text-base mb-2 sm:mb-0">{exam.title}</span>
            {role !== "viewer" && (
              <button
                onClick={() => handleClone(exam.id)}
                className="text-sm px-4 py-2 bg-blue-500 text-white rounded w-full sm:w-auto"
              >
                복사
              </button>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ExamList;