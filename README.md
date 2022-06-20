# Lego Art Project with Django

![lego-bg](https://user-images.githubusercontent.com/56384764/174484354-d003cd0f-60c1-4d0a-9091-ec3f628d4beb.jpg)


This is a hobby project made with Python, Python Imaging Library (PIL), PDF document generation in Python library (fpdf2) and Django web framework as user interface.


Lego Art is a Lego Theme that allows you to build mosaic-like pictures based on iconic personalities and characters in pop culture. 

I was inspired to do this project when I saw similar projects on the web, and I wanted to make it with Python and Python libraries. This project allows you to make custom Lego Art mosaic-like pictures. Currently this project supports parts from LEGO Art 31205 Jim Lees Batman. 

The project is divided into to modules:

1. Lego Art pdf generation
2. Django website serving as user interface


# Lego Art pdf generation

The PDF is generated using PIL module and fpdf2 module. Here is short description how the logic works for this project:

1. Uploaded image is resized to 48x48 pixels
2. Each Lego part has it's own color value in RGB
3. Function matches each pixel from the resized image to match the part color
4. A list with each pixel and it's coresponding closest matching colour in RGB is created
5. Using fpd2 modul every pixel is drawn as a circle with its own colour and number marking the part number from the part list









This project is not affiliated with The Lego Group and it is only a hobby project.
