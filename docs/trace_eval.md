# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** [PHAM DINH BAO KHOI]  
> **Mã Sinh Viên / Mã Học viên:** [2A202602434]  
> **Chủ đề Lựa chọn:** [Trợ lý đặt lịch tập Gym]  

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | 4/ 5 | có yêu cầu chia nhỏ nhiều bước suy luận nối tiếp nhau 
: (1) Nhận diện nhóm cơ/mục tiêu buổi tập từ người dùng, (2) Kiểm tra ràng buộc khung giờ hợp lệ của gói tập (chỉ cho phép từ 5h30 đến 14h00), (3) Xác định từ khóa kỹ thuật chuẩn để tìm bài tập tương ứng, (4) Ghép nối thời gian đặt lịch cá nhân và tổng hợp video hướng dẫn từ kênh chỉ định. |
| **2. Tool Interaction** | 4 / 5 | Hệ thống cần kết nối với MCP Server / Cơ sở dữ liệu bên ngoài: Calendar API (Google Calendar) để kiểm tra lịch rảnh và tạo sự kiện tập luyện, (2) YouTube Data API / Search Tool (truy vấn lọc bài tập chính xác theo Channel ID của kênh SmallGym) |
| **3. Dynamic Decision** | 4 / 5 | Bước tiếp theo có phụ thuộc vào kết quả quan sát bước trước: nếu tìm kiếm video bài tập theo yêu cầu chưa khớp trên kênh SmallGym -> tự động phân tích từ khóa bài tập thay thế/biến thể liên quan cùng nhóm cơ trên web. |
| **4. Long Horizon Goal** | 3 / 5 | Hệ thống phải giữ mục tiêu xuyên suốt qua nhiều lượt xử lý: Mục tiêu trải qua nhiều bước tương tác hội thoại: Từ tiếp nhận yêu cầu nhóm cơ và giờ tập -> xác thực khung giờ -> tìm kiếm/đính kèm link video SmallGym -> thêm lịch vào Calendar -> gửi thông báo xác nhận hoàn tất buổi tập. |
| **TỔNG ĐIỂM AGENTIC FIT** | **15 / 20** | *Nếu tổng điểm > 12/20: Bài toán rất phù hợp triển khai Agentic System.* |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "action_type": "TOOL_EXECUTION",
    "tool_name": "academic_query",
    "arguments": {
      "student_id": "SV2026001"
    },
    "observation": {
      "status": "SUCCESS",
      "student_id": "SV2026001",
      "data": {
        "full_name": "Nguyễn Văn An",
        "gpa": 3.85
      }
    },
    "latency_ms": 120.5
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [ ] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** ___ / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** ___ lượt.
- **Kết quả đẩy Repo nộp bài:** [ ] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
