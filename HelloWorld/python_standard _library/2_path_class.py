from pathlib import Path

path = Path("ecommerce/__init__.py")

path.exists()
path.is_file()
path.is_dir()
path = path.with_name('file.txt')
print(path)
