sellingprice=120
buyingprice=100
if(buyingprice<sellingprice):
    print("you got profit")
    profit=sellingprice-buyingprice
    print("profit is ",profit)
else:
    print("its a loss")