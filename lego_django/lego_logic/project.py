from lego_image import lego_object
from lego_pdf import main_page, pages_of_manual, part_description, save_output


if __name__ == '__main__':
    lego_object.save_output()
    main_page()
    part_description()
    pages_of_manual()
    save_output()
