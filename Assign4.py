
def countCode(str):
  len = str.length();

  count = 0;

  co = "co";

  e = "e";

   

  if (len < 4):

    return 0;

   

  for (i = 0, i < len - 3, i++):

    if 
        (co.compareTo(str.substring(i,i+2)) == 0 &&          e.compareTo(str.substring(i+3, i+4)) == 0)

      count++;

print countcode('aaacodebbb')

  }

  return count;

}
