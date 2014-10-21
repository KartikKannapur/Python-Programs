def add_complex():
        real_1 = int(raw_input("Enter the real part of number 1: "))
        img_1 = int(raw_input("Enter the imaginary part of number 1: "))
        real_2 = int(raw_input("Enter the real part of number 2: "))
        img_2 = int(raw_input("Enter the imaginary part of number 2: "))

        real_part = real_1 + real_2
        img_part = img_1 + img_2

        return "The complex number is "+str(real_part)+"+ j"+str(img_part)
