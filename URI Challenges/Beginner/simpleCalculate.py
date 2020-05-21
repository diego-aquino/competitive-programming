product1Data = input()
product2Data = input()

def getFloatDataFrom(productData):
   productData = productData.split(" ")

   for i in range(0, len(productData)):
      productData[i] = float(productData[i])
   
   return productData

product1Data = getFloatDataFrom(product1Data)
product2Data = getFloatDataFrom(product2Data)

price = (product1Data[1] * product1Data[2]) + (product2Data[1] * product2Data[2])

print("VALOR A PAGAR: R$ {:.2f}".format(price))
