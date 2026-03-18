import fitz
import os

def extract_images(pdf_path, output_dir):
    doc = fitz.open(pdf_path)
    images = []
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for page_index in range(len(doc)):
        page = doc[page_index]
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_filename = f"{output_dir}/page{page_index+1}_{img_index}.png"
            with open(image_filename, "wb") as f:
                f.write(image_bytes)
            images.append({"page": page_index + 1, "path": image_filename})
    return images
