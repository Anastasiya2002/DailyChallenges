def timeConversion(s):
    arr= s.split(":")
    if arr[2][2:]== "PM" or arr[0]=="12":
      arr[0] = str(int(arr[0]) +12)
    if arr[0]== "24" or arr[0]=="12":
        if arr[2][2:]== "PM":
            arr[0]= "12"
        else: arr[0]="00"
    arr[2]= arr[2][:2]
    return ":".join(arr)
print(timeConversion("12:40:22AM"))