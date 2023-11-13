import requests

# Địa chỉ API
api_url = "https://scholar-pcrawler-1.elemarkuspet.repl.co/get_paper/YpOO60MAAAAJ"

# Lấy dữ liệu từ API
response = requests.get(api_url)
data = response.json()

# Tạo chuỗi markdown từ dữ liệu
markdown_content = "\n\n## Scholar List\n\n"
markdown_content += "| Title | Authors | Citations | Year |\n"
markdown_content += "|-------|---------|-----------|------|\n"

for paper in data["papers"]:
    markdown_content += (
        f"| [{paper['Title']}]({paper['Paper_URL']}) | {paper['Authors']} | {paper['Citations']} | "
        f"{paper['Year']} |\n"
    )

# Add the "Show more" row with center alignment and larger font size
markdown_content += "| <td colspan=4 align=center><p style='font-size:larger;text-align:center'>[Show more](" + data['user_scholar_url'] + ")</p></td> |\n"

# Đọc toàn bộ README.md
with open("README.md", "r", encoding="utf-8") as readme_file:
    readme_content = readme_file.read()

# Tìm vị trí bắt đầu và kết thúc của phần cần thay thế
start_marker = "<!-- SCHOLAR-LIST:START -->"
end_marker = "<!-- SCHOLAR-LIST:END -->"
start_pos = readme_content.find(start_marker) + len(start_marker)
end_pos = readme_content.find(end_marker)

# Thay thế phần giữa start_pos và end_pos bằng nội dung mới của bảng
new_readme_content = (
    readme_content[:start_pos] + markdown_content + readme_content[end_pos:]
)

# Ghi nội dung mới vào README.md
with open("README.md", "w", encoding="utf-8") as readme_file:
    readme_file.write(new_readme_content)
