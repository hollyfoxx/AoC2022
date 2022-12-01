if [ $# -eq 0 ]
then
   python -m pytest test.py -s -vv
else
   python -m pytest test.py -s -vv -k $1
fi