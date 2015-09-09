
xelatex '\def\treadmill{foo} \input{personal_greek_reader.tex}'
mv personal_greek_reader.pdf reader_treadmill.pdf
xelatex '\input{personal_greek_reader.tex}'
mv personal_greek_reader.pdf reader_normal.pdf

open reader_normal.pdf