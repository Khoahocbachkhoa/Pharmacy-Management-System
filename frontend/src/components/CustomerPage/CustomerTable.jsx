// Bảng danh sách các khách hàng

import { useState } from "react";
import styles from "./CustomerTable.module.css";

export default function CustomerTable({ customers }) {
  const [page, setPage] = useState(1);
  const rowsPerPage = 5;

  const start = (page - 1) * rowsPerPage;
  const end = start + rowsPerPage;
  const currentRows = customers.slice(start, end);
  const totalPages = Math.ceil(customers.length / rowsPerPage);

  return (
    <>
      <table className={styles.table}>
        <thead>
          <tr>
            <th>ID</th>
            <th>Tên</th>
            <th>SĐT</th>
            <th>Địa chỉ</th>
          </tr>
        </thead>

        <tbody>
          {currentRows.length ? (
            currentRows.map((c) => (
              <tr key={c.id}>
                <td>#{c.id}</td>
                <td>{c.name}</td>
                <td>{c.phone || "---"}</td>
                <td>{c.address || "---"}</td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="4" className={styles.empty}>
                Chưa có dữ liệu
              </td>
            </tr>
          )}
        </tbody>
      </table>

      <div className={styles.pagination}>
        <button
          className={styles.pageBtn}
          disabled={page === 1}
          onClick={() => setPage((p) => p - 1)}
        >
          Prev
        </button>

        <span>
          {page} / {totalPages || 1}
        </span>

        <button
          className={styles.pageBtn}
          disabled={page >= totalPages}
          onClick={() => setPage((p) => p + 1)}
        >
          Next
        </button>
      </div>
    </>
  );
}