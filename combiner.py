from pathlib import Path
from pypdf import PdfWriter


def combine_pdfs(input_folder, output_file):
    input_folder = Path(input_folder)
    output_file = Path(output_file)

    pdf_files = sorted(input_folder.glob("*.pdf"))

    if not pdf_files:
        print("No PDF files found.")
        return

    writer = PdfWriter()

    for pdf_file in pdf_files:
        print(f"Adding: {pdf_file.name}")

        writer.append(str(pdf_file))

    with open(output_file, "wb") as output:
        writer.write(output)

    writer.close()

    print()
    print(f"Successfully combined {len(pdf_files)} documents.")
    print(f"Output: {output_file}")


if __name__ == "__main__":
    combine_pdfs(
        input_folder="./documents",
        output_file="./combined_document.pdf"
    )