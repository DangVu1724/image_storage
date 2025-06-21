from PIL import Image
import os

# Đường dẫn tới thư mục chứa ảnh đầu vào
input_folder = 'input_images'
# Đường dẫn tới thư mục chứa ảnh JPG đầu ra
output_folder = 'output_images'

# Tạo thư mục đầu ra nếu chưa có
os.makedirs(output_folder, exist_ok=True)

# Duyệt qua tất cả file trong thư mục đầu vào
for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)
    name, ext = os.path.splitext(filename)
    
    # Bỏ qua các file không phải ảnh
    if ext.lower() not in ['.png', '.jpg', '.jpeg', '.webp', '.bmp', '.tiff']:
        continue
    
    try:
        # Mở ảnh và chuyển về chế độ RGB
        with Image.open(file_path) as img:
            rgb_img = img.convert('RGB')
            output_path = os.path.join(output_folder, f"{name}.jpg")
            rgb_img.save(output_path, format='JPEG', quality=95)
            print(f"✅ Chuyển {filename} thành {name}.jpg")
    except Exception as e:
        print(f"❌ Lỗi với file {filename}: {e}")
