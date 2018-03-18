def cesar_des(n,message):
    abc_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']  
    print ("el tamaño del abcdario es:",len(abc_list))
    temp='?'
    msn_cesar=""
    i=0
    j=0
    # for key, value in enumerate(message):
    print ("temp va en:",temp)
    while i<len(message):
      print ("i vale tanto:",i)
      if (message[i] in abc_list):
        print ("en message [",i,"] va la letra:",message[i])
        temp=message[i]
        #i+=1
        x=0
        while x<len(abc_list):
          if (temp==abc_list[x]):
            msn_cesar+=abc_list[(x-n)%26]   # it's vital to think about the abc_list length
            # msn_cesar+=abc_list[x+n]      # This way doesn't work well
            print ("msn_cesar --> ",msn_cesar)
            print ("va en temp:",temp)    
            temp=''
            print("ahora en temp:",temp)
          #j+=1
            print ("-x vale:",x)
          else:
            x+=1
      else:
        j+=1
        print ("la letra:",temp,"no ha sido encontrada")
      i+=1
      print ("i vale:",i)

    print ("The msn_cesar is:",msn_cesar)

# str1="ghhsgrzplpñrxlvldpdfñrvhwrphzruñhdpv"
str1 = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"
cesar_des(13,str1)