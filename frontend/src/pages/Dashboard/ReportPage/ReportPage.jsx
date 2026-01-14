import { useEffect, useState } from "react";
import {
  getSaleByMonth,
  getNumInvoiceByMonth,
  getTopCustomer,
  getReportMedicines,
} from "../../../api/reportApi";

import styles from "./ReportPage.module.css";

export default function ReportPage() {
  // dữ liệu hiển thị
  const [totalSales, setTotalSales] = useState(0);
  const [invoiceCount, setInvoiceCount] = useState(0);
  const [topCustomers, setTopCustomers] = useState([]);
  const [bestMedicines, setBestMedicines] = useState([]);
  const [slowMedicines, setSlowMedicines] = useState([]);
  const [loading, setLoading] = useState(true);

  // fetch data
  useEffect(() => {
    const fetchReportData = async () => {
      try {
        const [saleRes, invoiceRes, customerRes, medicineRes] =
          await Promise.all([
            getSaleByMonth(),
            getNumInvoiceByMonth(),
            getTopCustomer(),
            getReportMedicines(),
          ]);

        setTotalSales(saleRes.data.total_sales || 0);
        setInvoiceCount(invoiceRes.data.total_invoices || 0);
        setTopCustomers(customerRes.data || []);
        setBestMedicines(medicineRes.data.best_sellers || []);
        setSlowMedicines(medicineRes.data.slow_sellers || []);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchReportData();
  }, []);

  if (loading) {
    return <p className={styles.loading}>Đang tải dữ liệu báo cáo...</p>;
  }

  return (
    <div className={styles.page}>
      <h1 className={styles.title}>Thống kê</h1>

      {/* Doanh thu thàng và số hóa đơn */}
      <div className={styles.cardGrid}>
        <div className={styles.card}>
          <p className={styles.cardLabel}>Doanh thu tháng này</p>
          <h2 className={styles.cardValue}>
            {totalSales.toLocaleString("vi-VN")} ₫
          </h2>
        </div>

        <div className={styles.card}>
          <p className={styles.cardLabel}>Số hóa đơn tháng này</p>
          <h2 className={styles.cardValue}>{invoiceCount}</h2>
        </div>
      </div>

      {/* Thống kê khách mua nhiều và thuốc bán chạy, bán ế */}
      <div className={styles.bottomGrid}>
        {/* Top Khách hàng */}
        <div className={styles.tableCard}>
          <h3>Khách mua nhiều nhất</h3>
          <table className={styles.table}>
            <thead>
              <tr>
                <th className={styles.th}>Tên khách</th>
                <th className={`${styles.th} ${styles.right}`}>Tổng mua</th>
              </tr>
            </thead>
            <tbody>
              {topCustomers.map((c, i) => (
                <tr key={i}>
                  <td className={styles.td}>{c.name}</td>
                  <td className={`${styles.td} ${styles.money}`}>
                    {c.total.toLocaleString("vi-VN")} ₫
                  </td>
                </tr>
              ))}
              {topCustomers.length === 0 && (
                <tr>
                  <td colSpan="2" className={styles.td}>
                    Chưa có dữ liệu
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>

        {/* Danh sách Thuốc bán chạy, bán ế */}
        <div className={styles.tableCard}>
          <h3>Thuốc bán chạy</h3>
          <ul className={styles.list}>
            {bestMedicines.map((m, i) => (
              <li key={i} className={styles.goodItem}>
                {m.name} <strong>({m.quantity})</strong>
              </li>
            ))}
            {bestMedicines.length === 0 && <li>Chưa có dữ liệu</li>}
          </ul>

          <h3 className={styles.subTitle}>Thuốc bán chậm</h3>
          <ul className={styles.list}>
            {slowMedicines.map((m, i) => (
              <li key={i} className={styles.badItem}>
                {m.name} <strong>({m.quantity})</strong>
              </li>
            ))}
            {slowMedicines.length === 0 && <li>Chưa có dữ liệu</li>}
          </ul>
        </div>
      </div>
    </div>
  );
}