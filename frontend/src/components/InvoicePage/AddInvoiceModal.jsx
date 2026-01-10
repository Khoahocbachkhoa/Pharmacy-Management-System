// form thêm một hóa đơn mới

import { useState, useEffect } from "react";
import { createInvoiceApi } from "../../api/invoiceApi";
import { getMedicineOptionsApi } from "../../api/medicineApi";
import { getCustomersApi } from "../../api/customerApi";

import styles from "./AddInvoiceModal.module.css";

export default function AddInvoiceModal({ onClose, onSuccess }) {
  const [medOptions, setMedOptions] = useState([]);
  const [cusOptions, setCusOptions] = useState([]);

  const [selectedCustomer, setSelectedCustomer] = useState("");
  const [cartItems, setCartItems] = useState([
    { medId: "", qty: 1, price: 0 },
  ]);

  useEffect(() => {
    getMedicineOptionsApi().then(res => setMedOptions(res.data));
    getCustomersApi().then(res => setCusOptions(res.data));
  }, []);

  // Xử lý danh mục các thuốc mà khách mua thay đổi?
  const handleCartChange = (index, field, value) => {
    const newCart = [...cartItems];

    if (field === "medId") {
      const med = medOptions.find(m => m.id === Number(value));
      newCart[index].medId = value;
      newCart[index].price = med ? med.price : 0;
    } else {
      newCart[index][field] = value;
    }

    setCartItems(newCart);
  };

  const addLine = () => {
    setCartItems([...cartItems, { medId: "", qty: 1, price: 0 }]);
  };

  const removeLine = (index) => {
    setCartItems(cartItems.filter((_, i) => i !== index));
  };

  const total = cartItems.reduce(
    (sum, i) => sum + i.price * i.qty,
    0
  );

  const handleSave = async () => {
    const items = cartItems.filter(i => i.medId);
    if (!items.length) return alert("Chọn ít nhất 1 thuốc");

    await createInvoiceApi({
      customer_id: selectedCustomer || null,
      details: items.map(i => ({
        medicine_id: i.medId,
        quantity: i.qty,
      })),
    });

    onSuccess();
    onClose();
  };

  return (
    <div className={styles.modalOverlay}>
      <div className={`${styles.modalContent} ${styles.large}`}>
        <h2 className={styles.modalTitle}>Tạo hóa đơn</h2>

        <div className={styles.formGroup}>
          <select
            className={styles.formSelect}
            value={selectedCustomer}
            onChange={e => setSelectedCustomer(e.target.value)}
          >
            <option value="">-- Khách lẻ --</option>
            {cusOptions.map(c => (
              <option key={c.id} value={c.id}>
                {c.name}
              </option>
            ))}
          </select>
        </div>

        <table className={styles.invoiceTable}>
          <thead>
            <tr>
              <th>Thuốc</th>
              <th>Số lượng</th>
              <th>Giá</th>
              <th>Thành tiền</th>
              <th></th>
            </tr>
          </thead>

          <tbody>
            {cartItems.map((item, idx) => (
              <tr key={idx}>
                <td>
                  <select
                    className={styles.formSelect}
                    value={item.medId}
                    onChange={e =>
                      handleCartChange(idx, "medId", e.target.value)
                    }
                  >
                    <option value="">-- Chọn thuốc --</option>
                    {medOptions.map(m => (
                      <option key={m.id} value={m.id}>
                        {m.name}
                      </option>
                    ))}
                  </select>
                </td>

                <td>
                  <input
                    className={styles.formInput}
                    type="number"
                    min="1"
                    value={item.qty}
                    onChange={e =>
                      handleCartChange(idx, "qty", Number(e.target.value))
                    }
                  />
                </td>

                <td className={styles.textRight}>{item.price}</td>
                <td className={styles.textRight}>
                  {item.price * item.qty}
                </td>

                <td>
                  {cartItems.length > 1 && (
                    <button
                      className={`${styles.btn} ${styles["btn-danger"]}`}
                      onClick={() => removeLine(idx)}
                    >
                      ✕
                    </button>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>

        <button
          className={`${styles.btn} ${styles["btn-secondary"]}`}
          onClick={addLine}
        >
          + Thêm dòng
        </button>

        <div className={styles.total}>
          Tổng tiền: <strong>{total}</strong>
        </div>

        <div className={styles.modalActions}>
          <button
            className={`${styles.btn} ${styles["btn-secondary"]}`}
            onClick={onClose}
          >
            Hủy
          </button>
          <button
            className={`${styles.btn} ${styles["btn-primary"]}`}
            onClick={handleSave}
          >
            Lưu hóa đơn
          </button>
        </div>
      </div>
    </div>
  );
}
