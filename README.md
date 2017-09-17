
# *Bookletise*. Print a booklet using _any_ pdf printer.


##  

Some expensive proprietary software, such as [_FinePrint_](http://fineprint.com/fp/) or [_Adobe InDesign_](http://www.adobe.com/products/indesign.html),
can create multi-page documents to be easily printed as books. 
These typically set four pages on a single sheet, in a way that,
when you collate, fold, and staple the double-sided sheets, the result is a single book with the appropriate page order.


As an example, let us suppose that we wish to print out a book out of a multi-page document,
and bind the booklet pages in groups of eigth.
In this case,  page two must be positioned next to page 7, so that when the two pages are printed on the same sheet,
folded, and collated, the pages end up in the appropriate order.

*Bookletise* allows you to print any multipage pdf document of any size as a book for free,
regardless of the software and the operating system that you wish to use to visualise and print the document.



## Usage

This guide demonstrates what *Bookletise* is capable of doing.

The core program is the python script `bookletise`, which can be deployed in a Python shell with
```{python}
>>> from bookletise import *
>>> bookletise(4, 10)
```
```
4,1,2,3,8,5,6,7
There are 2 pages left,
 make another booklet of 4 pages
NA,9,10,NA
```
This called the function to set a book of 10 pages with four-page booklest (of one sheet each).
The order page numbers are in the first and last line. The warning output, as well a the last line, is only
showed when a reminder number of pages remain (this occurs when the total number of pages is not multiple of the
number of pages per booklet).

The `bookletise` function ouputs to the standard output a sequence of pages, ordered in booklets.
The corrected order is calculated by the doppio-Anagni algorithm.
The number `size_of_booklets` of page per booket and the total number `number_of_pages`  of pages in the original pdf document must be specified. Obviously, the variable `size_of_booklets` must be multiple of 4,
but smaller than the total number of pages in the document.

The Python script can be called by the terminal using
```{sh}
python bookletise.py number_of_pages size_of_booklets
```

Copy the output values from the standar error and paste in the `Pages` bor. A click on the `print` button will obviously
print the document pages in the expected order.


Alternatively, the script `bookletise.sh` provides a one-liner interface to the python program.
If the software [_PDFTKtk Server_](https://www.pdflabs.com/tools/pdftk-server/) is installed, then
```{sh}
sh bookletise.sh input_file.pdf output_file.pdf size_of_booklets
```
automatically creates an output pdf file ready to be printed as a book.

## Licence

*Bookletise* is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

*Bookletise* is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should find a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.


