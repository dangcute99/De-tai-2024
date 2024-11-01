# Hướng Dẫn Đẩy Code Lên GitHub

## 1. Cài đặt Git

Nếu bạn chưa cài đặt Git, tải về và cài đặt từ trang chủ [Git](https://git-scm.com/).

## 2. Khởi tạo Repository cục bộ

Di chuyển vào thư mục dự án của bạn trên máy cục bộ và khởi tạo Git repository:

```bash
cd đường/dẫn/tới/dự/án
git init
```

## 3. Kết nối với Repository trên GitHub

- Tạo một repository mới trên GitHub (không thêm README, LICENSE, hoặc .gitignore).
- Kết nối repository cục bộ với GitHub bằng lệnh (thay `URL_REPO_GITHUB` bằng URL repository của bạn):

```bash
git remote add origin URL_REPO_GITHUB
```

## 4. Thêm và commit các tệp tin

Thêm tất cả các tệp tin vào staging và tạo commit với tin nhắn mô tả:

```bash
git add .
git commit -m "Initial commit"
```

## 5. Đẩy mã lên GitHub

### Trường hợp 1: Branch hiện tại là `main`

Nếu branch hiện tại là `main`, đẩy mã lên branch `main` trên GitHub:

```bash
git push -u origin main
```

### Trường hợp 2: Branch hiện tại là `master`

Nếu branch của bạn là `master`, bạn có thể đổi tên thành `main` để phù hợp với GitHub:

```bash
git branch -M main
git push -u origin main
```

Hoặc, nếu muốn giữ tên branch là `master`, đẩy mã lên branch `master` trên GitHub:

```bash
git push -u origin master
```

## Xử lý Lỗi `fetch first`

Nếu gặp lỗi `fetch first`, hãy kéo các thay đổi từ GitHub trước khi đẩy:

```bash
git pull origin main --rebase
git push -u origin main
```

## Cập nhật mã mới sau khi đã đẩy

Khi có thay đổi mới, hãy thực hiện lại các bước:

```bash
git add .
git commit -m "Mô tả thay đổi mới"
git push
```

**Chúc bạn thành công với Git và GitHub!**
git config --global core.autocrlf true
