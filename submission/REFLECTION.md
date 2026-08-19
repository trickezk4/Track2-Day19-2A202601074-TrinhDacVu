# Reflection — Lab 19

**Tên:** Trịnh Đắc Vụ
**Cohort:** 2A202601074 - Track 2
**Path đã chạy:** lite

---

## Câu hỏi (≤ 200 chữ)

> Trên golden set 50 queries, mode nào thắng ở loại query nào (`exact` /
> `paraphrase` / `mixed`), và tại sao? Khi nào bạn **không** dùng hybrid
> (i.e. khi nào pure BM25 hoặc pure vector là lựa chọn đúng)?

- **Exact queries:** Pure BM25 & Hybrid dẫn đầu (P@10 = 96.7% vs Semantic 80.0%) do BM25 khớp chính xác từ khóa, thuật ngữ chuyên ngành và tên riêng mà không bị suy hao ngữ nghĩa.
- **Paraphrase queries:** Hybrid (32.0%) và BM25 (33.3%) vượt trội Semantic (24.0%) nhờ RRF dung hòa giữa ngữ nghĩa đồng nghĩa của dense vector và từ khóa nòng cốt.
- **Mixed queries:** Hybrid thắng tuyệt đối (P@10 = 100.0% vs Semantic 98.5%, BM25 97.0%), chứng minh ưu thế vượt trội khi truy vấn vừa có từ khóa đặc thù vừa mang ngữ cảnh rộng.

**Khi nào KHÔNG dùng hybrid:**

1. Khi hệ thống yêu cầu SLA siêu thấp (<5ms) hoặc tài nguyên phần cứng hạn chế (pure BM25 nhẹ hơn và không tốn chi phí inference embedding).
2. Khi dữ liệu tra cứu là SKU, serial code, định danh chính xác (pure BM25 là tối ưu).
3. Khi tìm kiếm cross-lingual/đa ngôn ngữ hoàn toàn khác biệt từ vựng (pure vector phát huy tối đa sức mạnh).

---

## Điều ngạc nhiên nhất khi làm lab này

RRF (Reciprocal Rank Fusion k=60) cực kỳ đơn giản không cần tuning trọng số phức tạp nhưng lại mang lại độ chính xác tổng thể (78.6%) vượt cả BM25 (77.8%) và Semantic (73.2%), đặc biệt đạt 100% trên tập mixed queries.

---

## Bonus challenge

- [X] Đã làm bonus (xem `notebooks/` 05 -> 08: Filtered ANN, Agent Decomposition, Semantic Cache, Feature Engineering)
- [ ] Pair work với: _<tên đồng đội nếu có>_
