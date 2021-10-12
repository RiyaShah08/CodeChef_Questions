amt,withdraw = map(float, input().split())
if(amt%5==0 and (amt<=withdraw-0.50)):
    balance=(withdraw-0.50-amt)
    print("{:.2f}".format(balance));
else:
    print("{:.2f}".format(withdraw));