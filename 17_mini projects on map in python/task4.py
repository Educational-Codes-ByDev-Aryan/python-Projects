# Add 18% GST to Product Prices
prices = [100, 250, 500, 1000, 1500]

gst_added_price = list(map(lambda x:x*1.18,prices))
print(gst_added_price)
