context.stocks = symbols(‘VTI’, ‘VXUS’, ‘BND’, ‘BNDX’)
context.bought = False

risk_level = 5
risk_based_allocation = {0: (0,0,0.686,0.294),
                         1: (0.059,0.039,0.617,0.265),
                         2: (0.118,0.078,0.549,0.235),
                         3: (0.176,0.118,0.480,0.206),
                         4: (0.235,0.157,0.412,0.176),
                         5: (0.294,0.196,0.343,0.147),
                         6: (0.353,0.235,0.274,0.118),
                         7: (0.412,0.274,0.206,0.088),
                         8: (0.470,0.314,0.137,0.059),
                         9: (0.529,0.353,0.069,0.029),
                         10: (0.588,0.392,0,0)}
    #Saves the weights to easily access during rebalance
context.target_allocation = dict(zip(context.stocks,
                            risk_based_allocation[risk_level]))

    #To make initial purchase
context.bought = False

#if statement checking if bought- if not runs a for loop that 
if not context.bought:
#using a for loop to go over the stocks we have
        for stock in context.stocks:
          # calculating amount  
            amount = (context.target_allocation[stock] *
                      context.portfolio.cash) / data.current(stock,’price’)
            if (amount != 0):
                order(stock, int(amount))
                #log purchase
            log.info(“buying “ + str(int(amount)) + “ shares of “ +
                     str(stock))

         #now won’t purchase again and again
         context.bought = True