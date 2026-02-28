jam = 60
mod60 = (jam * 5 + 45) % jam
jam60 = ((jam * 5 + 45) - mod60) / jam
print (jam * 5 + 45, "Minutes")
print (jam60, "Hours", mod60, "Minutes")
print("Upah per jam:", 85000)
print ("Total upah + 45 menit:", jam60 * 85000 + (85000 * 0.75))