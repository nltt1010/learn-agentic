# File system tools
def write_text_file(filename: str, content: str) -> str:
    """
    Tạo hoặc ghi đè nội dung văn bản vào một file text (.txt) trên máy tính.
    
    Args:
        filename: Tên file muốn lưu (ví dụ: 'report.txt').
        content: Nội dung văn bản chi tiết muốn ghi vào trong file.
    """
    try:
        # Ghi file với mã hóa utf-8 để tránh lỗi tiếng Việt
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Thành công: Đã lưu dữ liệu vào file '{filename}'."
    except Exception as e:
        return f"Lỗi khi ghi file: {str(e)}"




# Tools relevent to caculate
def exponentiation(base: float, exponent: int) -> float:
    """
    Tính lũy thừa của một cơ số với số mũ cho trước (base^exponent).
    
    Args:
        base: Cơ số (ví dụ: 2, 3.5).
        exponent: Số mũ (ví dụ: 3, 5).
    """
    return (base**exponent)




# Tools relevent to finance
import yfinance as yf

def get_current_stock_price(ticker: str) -> str:
    """
    Lấy giá cổ phiếu thời gian thực từ Yahoo Finance dựa trên mã chứng khoán (ticker).
    
    Args:
        ticker: Mã chứng khoán của công ty (ví dụ: 'AAPL', 'GOOG', 'MSFT').
    """
    try:
        # Khởi tạo đối tượng ticker của Yahoo Finance
        stock = yf.Ticker(ticker.upper())
        
        # Lấy thông tin lịch sử của ngày gần nhất để trích xuất giá đóng cửa
        todays_data = stock.history(period='1d')
        
        if todays_data.empty:
            return f"Không tìm thấy dữ liệu cho mã chứng khoán {ticker}."
            
        # Lấy giá đóng cửa mới nhất
        current_price = todays_data['Close'].iloc[-1]
        
        return f"Giá cổ phiếu của {ticker.upper()} hiện tại là ${current_price:.2f} USD."
        
    except Exception as e:
        return f"Lỗi khi truy vấn dữ liệu cho mã {ticker}: {str(e)}"