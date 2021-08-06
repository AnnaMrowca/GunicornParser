# GunicornParser

Invoking file:
python parser.py --from 20-11-2016_11-23-11 --to 21-11-2016_01-33 logfile.log

python parser.py --from 20-11-2016_11-23-11 gunicorn.log2

python parser.py --to 21-11-2016_01-33 gunicorn.log2

python parser.py gunicorn.log2


Exemplary output:

Requests: 99999
Requests/sec: 10.65
Responses: {'200': 96205, '404': 3794}
Avg size of 2xx responses: 0.29 Mb


Code starts with reading file and parsing arguments from cmd/ terminal

Logic is divided into three sections:

1) Preparing statistics when dates --from and --to are not given
2) Preparing staticsts when dates --from and --to are given
3) Preparing statistics when date --from is given
4) Preparing statistics when date --to is given
