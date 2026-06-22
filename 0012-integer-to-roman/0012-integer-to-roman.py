class Solution:
    def intToRoman(self, num: int) -> str:
        value=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        symb=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']

        roman=''
        for i in range(0,len(value)):
            while num>=value[i]:
                roman+=symb[i]
                num-=value[i]
        return roman

