#!/bin/bash
if [ $# -nif [ $# -ne 3 ]
then
    echo "Usage: bash bookletise.sh [option] input_file.pdf output_file.pdf size_of_booklets"
    exit $E_BADARGS
else
    NumberOfPages=$(pdftk $1 dump_data | grep NumberOfPages | sed 's/[^0-9]*//')
    var=$(python bookletise.py $3 $NumberOfPages)
    pdftk A=$1 B=blank.pdf cat $var output $2
fi

#
#!/bin/bash
#pdftk A=$1 B=blank.pdf cat B  A161 A162 A175 A174 A163 A164 A173 A172 A165 A166 A171 A170 A167 A168 A169 output $2
 
