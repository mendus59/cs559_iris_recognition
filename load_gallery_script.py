
import hash_builder

def load_gallery_script():

   arr =[]
   hash_builder.build("gallery\\", arr)
   print(len(arr))
   print(arr)
   return arr


load_gallery_script()


