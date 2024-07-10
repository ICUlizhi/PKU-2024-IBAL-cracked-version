import ebooklib
from ebooklib import epub
import pdfkit

def epub_to_pdf(epub_path, pdf_path):
    book = epub.read_epub(epub_path)
    content = ''
    
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            content += item.get_body_content().decode('utf-8')

    # Generate PDF from HTML content
    pdfkit.from_string(content, pdf_path)

# Example usage
epub_path = '（狄更斯的圣诞故事）圣诞颂歌 (【英】查尔斯·狄更斯) (Z-Library).epub'
pdf_path = '（狄更斯的圣诞故事）圣诞颂歌 (【英】查尔斯·狄更斯) (Z-Library).pdf'
epub_to_pdf(epub_path, pdf_path)
