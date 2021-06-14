#
# import pandas as pd
# import re
import csv
# """ Parsing format is <txid>,<fee>,<weight>,<parents>"""
# class MempoolTransaction():
#     def __init__(self, txid, fee, weight, parent_txids):
#         self.txid = txid
#         self.fee = int(fee)
#         self.weight = weight
#         self.parent_txids = parent_txids
#
#     def ParseString(self, filename):
#         return re.findall(self.weight, filename, re.DOTALL | re.MULTILINE)
#
#
# # TODO: add code to parse weight and parents fields
#
#     def parse_mempool_csv(self):
#         """Parse the CSV file and return a list of MempoolTransactions."""

outfile = open('block.txt', 'w')
with open('mempool.csv', 'r') as f:
    reader = csv.reader(f, delimiter=",")
    # header = next(reader)
    for row in reader:
        txid = row[0]
        fee = row[1]
        weight = row[2]
        parents = row[3]
        line = "{}\n".format(txid)
        outfile.write(line)

            # return ([MempoolTransaction(*line.strip().split(',')) for line in f.readlines()])



