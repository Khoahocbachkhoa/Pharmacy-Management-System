import { FaUser, FaLock } from "react-icons/fa";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { loginApi } from "../../api/authApi";

import styles from "./LoginPage.module.css";

function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleLogin = async () => {
    setError("");

    try {
      const res = await loginApi(username, password);
      const { access_token, msg } = res.data;

      // Lưu JWT
      localStorage.setItem("token", access_token);

      alert(msg);
      navigate("/dashboard");
      
    } catch (err) {
      if (err.response) {
        setError(err.response.data.msg);
      } else {
        setError("Không thể kết nối tới server");
      }
    }
  };

  return (
    <div className={styles.pageWrapper}>
      <div className={styles.loginCard}>
        <h2 className={styles.loginTitle}>Đăng nhập</h2>

        <form className={styles.form}>
          {/* username */}
          <div className={styles.inputGroup}>
            <label className={styles.inputLabel}>Tên đăng nhập</label>
            <div className={styles.inputField}>
              <FaUser style={{ color: "#9ca3af", marginRight: 10 }} />
              <input
                className={styles.input}
                type="text"
                placeholder="Nhập tên đăng nhập"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
              />
            </div>
          </div>

          {/* pass */}
          <div className={styles.inputGroup}>
            <label className={styles.inputLabel}>Mật khẩu</label>
            <div className={styles.inputField}>
              <FaLock style={{ color: "#9ca3af", marginRight: 10 }} />
              <input
                className={styles.input}
                type="password"
                placeholder="Nhập mật khẩu"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </div>
          </div>

          {/* err */}
          {error && (
            <div style={{ color: "red", fontSize: 12 }}>
              {error}
            </div>
          )}

          <button
            type="button"
            className={styles.loginBtn}
            onClick={handleLogin}
          >
            Đăng nhập
          </button>
        </form>

        <div className={styles.signupBox}>
          Chưa có tài khoản?
          <span className={styles.signupLink}>Đăng ký</span>
        </div>
      </div>
    </div>
  );
}

export default LoginPage;