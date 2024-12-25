import os
from PyPDF2 import PdfMerger

def combine_pdfs(input_folder, output_file):
    """
    Combines all PDF files in a specified folder into a single PDF file.

    :param input_folder: The folder containing PDF files to combine.
    :param output_file: The output PDF file path.
    """
    merger = PdfMerger()

    try:
        pdf_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith('.pdf')]

        if not pdf_files:
            print("No PDF files found in the specified folder.")
            return

        for pdf in pdf_files:
            print(f"Adding {pdf}...")
            merger.append(pdf)

        merger.write(output_file)
        print(f"Combined PDF saved as {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        merger.close()

if __name__ == "__main__":
    input_folder = "./files"

    output_file = "combined.pdf"

    combine_pdfs(input_folder, output_file)