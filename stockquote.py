import ystockquote, argparse, sys
from pprint import pprint

parser = argparse.ArgumentParser()
parser.add_argument("stockname", help="The symbol  of the stock you want to display")
args = parser.parse_args()

#Get stock information for the provided symbol
print "Getting stock information for  " + args.stockname + "..." + "\n",
sys.stdout.flush()

allInfo = ystockquote.get_all(args.stockname)
print args.stockname + " Price = " + allInfo["price"]
print args.stockname + " Market cap = " + allInfo["market_cap"]
pprint(ystockquote.get_all(args.stockname))
