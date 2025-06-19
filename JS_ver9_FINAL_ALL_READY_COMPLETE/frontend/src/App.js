import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Login from "./Login";
import ExamList from "./ExamList";

function App() {
  const [token, setToken] = useState(localStorage.getItem("token"));
  const [role, setRole] = useState(localStorage.getItem("role"));

  const handleLogin = (userRole) => {
    setToken(localStorage.getItem("token"));
    setRole(userRole);
  };

  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("role");
    setToken(null);
    setRole(null);
  };

  useEffect(() => {
    const storedToken = localStorage.getItem("token");
    const storedRole = localStorage.getItem("role");
    if (storedToken && storedRole) {
      setToken(storedToken);
      setRole(storedRole);
    }
  }, []);

  return (
    <Router>
      <div className="p-4 font-sans">
        <h1 className="text-2xl font-bold mb-4">JS 자동 채점 시스템</h1>
        {token ? (
          <div>
            <button onClick={handleLogout} className="mb-4 px-4 py-1 bg-red-500 text-white rounded">
              로그아웃
            </button>
            <Routes>
              <Route path="/" element={<ExamList role={role} />} />
              <Route path="*" element={<Navigate to="/" />} />
            </Routes>
          </div>
        ) : (
          <Login onLogin={handleLogin} />
        )}
      </div>
    </Router>
  );
}

export default App;