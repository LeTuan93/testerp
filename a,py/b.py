# Danh sách thông báo đa ngôn ngữ
ERROR_MESSAGES = {
    "logout_msg": {
        "en": "Logged out successfully",
        "vi": "Đăng xuất thành công"
    },
    "dataset_notexist": {
        "en": "Dataset does not exist",
        "vi": "Bộ dữ liệu không tồn tại"
    },
    "category_error": {
        "en": "lỗi cài đặt getting list of labels",
        "vi": "Lỗi xảy ra khi lấy danh sách nhãn"
    },
    "dataset_nolabel": {
        "en": "No images without labels",
        "vi": "Không có ảnh không có nhãn"
    },
        "datasel": {
        "en": "No images without labels",
        "vi": "Không có ảnh không có nhãn"
    }
}

def getxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx(error_code: str, lang: str = "vi") -> str:
    """
    Lấy thông báo lỗi theo mã và ngôn ngữ (mặc định là 'vi').
    Nếu không tìm thấy ngôn ngữ, trả về tiếng Anh ('en').
    """
    error = ERROR_MESSAGES.get(error_code)
    if not error:
        return f"Mã lỗi không xác định: {error_code}"
    
    return error.get(lang, error.get("en", "Unknown error"))

# Test hàm
if __name__ == "__main__":
    print(get_message("dataset_notexist", lang="vi"))  # Bộ dữ liệu không tồn tại
    print(get_message("logout_msg", lang="en"))        # Logged out successfully
    print(get_message("invalid_key"))                  # Mã lỗi không xác định: invalid_key
