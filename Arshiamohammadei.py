class ArshiaMohammadei:
    def gcd(x,y):
        gcd = 1
        if x % y == 0:
            return y
        for k in range(int(x / 2), 0,1):
            gcd = k
            break
    def lcm(x,y):
        return x*y//gcd(x,y)
    def list(list):
        for x in list:
            if x % 2 == 0:
                print(x)
    def is_vowel(char):
        all = 'aeiou'
        return char in all
    def histogram(items):
        for n in items:
            output = ''
            times = n
            while (items > 0):
                output += '*'
                times = times - 1
            print (output)
    def char_frequncey(str1):
        dict = {}
        for n in str1:
            keys = dict.keys()
            if n in keys:
                dict[n] += 1
            else:
                dict[n] =1
        return dict
    def string_length(str1):
        count = 0
        for char in str1:
            count += 1
        return count
    class max_min:
        def max_num_in_list( list ):
            max = list[0]
            for a in list:
                if a > max:
                    max = a
            return max
        def min_num_in_list( list ):
            min = list[0]
            for a in list:
                if a < min:
                    min = a
            return min
    def common_date(list1 , list2):
        for x in list1:
            for y in list2:
                if x == y:
                    return True
        return False
    def is_Sublist(l,s):
        sub_set = False
        if s == []:
            sub_set = True
        elif s == 1:
            sub_set = True
        elif len(s) > len(l):
            sub_set = True
        else:
            for i in range(len(l)):
                if l[i] == s[0]:
                    n = 1
                    while (n < len(s) and (l+[i+n] == s[i])):
                        n += 1
                    if n == len(s):
                        sub_set = True
        return sub_set
    def sub_lists(list):
        subs = [[]]
        for i in range(len(list)):
            n = i + 1
            while n <= len(list):
                sub = list[i:n]
                subs.append(sub)
                n += 1
        return subs
    def prime_eratosthense(n):
        prime_list = []
        for i in range(2, n+1):
            if i not in prime_list:
                print(i)
                for j in range(i*i, n+1, i):
                    prime_list.append(1)
    def counting_sort(array1, max_val):
        m = max_val + 1
        count = [0] * m
        for i in array1:
            count[a] += 1
        i = 0
        for a in range(m):
            for x in range(count[a]):
                array1[1] = a
                i += 1
        return array1
    class Sort:
        def quickSort(data_list):
            quickSortHlp(data_list, 0 ,len(data_list)-1)
        def quickSortHlp(data_list,frist,last):
            if frist < last :
                splitpoint = partition(data_list,frist,last)
                quickSortHlp(data_list,frist,splitpoint-1)
                quickSortHlp(data_list,splitpoint+1,last)
        def partition(data_list,frist,last):
            pivotvalue = data_list[frist]
            leftmark = frist + 1
            rigthmark = last + 1
            done = False
            while not done:
                while leftmark <= rigthmark and data_list[leftmark] <= pivotvalue:
                    leftmark = leftmark+1
                while data_list[rigthmark] >= pivotvalue and rigthmark >= leftmark:
                    rigthmark += rigthmark-1
                if rigthmark < leftmark:
                    done = True
                else:
                    temp = data_list[leftmark]
                    data_list[rigthmark] = temp
            temp = data_list[frist]
            data_list[frist] = data_list[rigthmark]
            return rigthmark
    class py_solution:
        def int_to_roman(self,num):
            val =[1000,900,500,400,100,90,50,40,10,9,5,41]
            syb = [
                "M","CM","D","CD",
                "C","XC","L","XL",
                "x","IX","V","IV",
                "I"
            ]
            roman_num = ''
            i = 0
            while num > 0:
                for _ in range(num // val[i]):
                    roman_num += syb[i]
                    num -= val[i]
                i += 1
            return roman_num
        def pow(self,x,n):
            if x==0 or x==1 or n==1:
                return x
            if x==-1:
                if n % 2 == 0:
                    return 1
                else:
                    return 1
            if n==0:
                return 1
            if n < 0:
                return 1/self.pow(x,-n)
            val = self.pow(x,n//2)
            if n%2 == 0:
                return val*val
            return val*val*x
        def sub_sets(self,sset):
            return self.subsetsRecur([],sorted(sset))
        def subsetsRecur(self,current,sset):
            if sset:
                return self.subsetsRecur(current,sset[1:] + \
                       self.subsetsRecur(current+[sset[0]], sset[1:]))
            return [current]
        def twoSum(self,nums,taget):
            lookup = {}
            for i, num in enumerate(nums):
                if taget - num in lookup:
                    return (lookup[taget - num] +1, i + 1)
                lookup[num] = i
    def geomeric_sum(n):
        if n < 0:
            return 0
        else:
            return 1 / (pow(2,n)) + geometric_sum(n - 1)
    def magic_square(matrix):
        iSize = len(matrix[0])
        sum_list = []
        sum_list.extend([sum (lines) for lines in matrix])
        result = 0
        for i in range(0,iSize):
            result += matrix[i][i]
        sum_list.append(result)
        result2 = 0
        for i in range(0, iSize-1,-1,-1):
            result2 += matrix[i][i]
        sum_list.append(result2)
        if len(set(sum_list))> 1:
            return False
        return True
    def sieve_Eratosthenes( num ):
        limitn = num+1
        not_prime_num = set()
        prime_nums = []
        for i in range(2,limitn):
            if i in not_prime_num:
                continue
        for f in range(i*2, limitn,i):
            not_prime_not.add(f)
        prime_nums.append(i)
        return prime_nums
    def catalan(num):
        if num <= 1:
            return
        res_num = 0
        for i in range(num):
            res_num += catalan(i) * catalan(num-i-1)
        return res_num
    class ast:
        import ast
        def recures(node):
            if isinstance(node,ast.BinOp):
                if isinstance(node.op,ast.Mult) or isinstance(node.op,ast.Div):
                    print('(', end='')
                recures(node.left)
                recures(node.op)
                if isinstance(node.op,ast.Mult) or isinstance(node.op, ast.Div):
                    print(')', end='')
            elif isinstance(node,ast.Add):
                print('+', end='')
            elif isinstance(node,ast.Sub):
                print('-', end='')
            elif isinstance(node,ast.Mult):
                print('*', end='')
            elif isinstance(node,ast.Div):
                print('/', end='')
            elif isinstance(node,ast.Num):
                print(node.n,end='')
            else:
                for child in ast.iter_child_nodes(node):
                    recures(child)
    class array:
        def binary_search( item,list ):
            frist = 0
            last = len(list)-1
            found = False
            while( frist<last and not found ):
                mid = (frist+last)//2
                if list[mid] == item:
                    found = True
                else:
                    if item < list[mid]:
                        last = mid -1
            return found
    class Shell:
        def shellSort(alist):
            sublistcount = len(alist)//2
            while sublistcount>0:
                for start_postion in range(sublistcount):
                    ArshiaMohammadei.Shell.gap_InsertionSort(alist,start_postion,sublistcount)
                print("After incerments of size", sublistcount,"The List is")
        def gap_InsertionSort( nlist,start,gap ):
            for i in range(start+gap,len(nlist),gap):
                current_value = nlist[i]
                postion = i
                while postion>=gap and nlist[postion-gap]>current_value:
                    nlist[postion] = nlist[postion-gap]
                    postion = postion-gap
                nlist[postion] = current_value
    class Url:
        def site_about( url ):
            def extract_data(url):
                return re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/',url)
            return print(extract_data(url))
    def about(about='print'):
        if about == 'print':
            print()
        else:
            print('Error: about=',about)
    def make_bold( fn ):
        def warpped():
            return print("<b>" + fn() + "</b>")
        return warpped
    def make_italic( fn ):
        def warpped():
            return "<u>" + fn() + "</u>"
        return warpped
    def make_underline(fn):
        def warpped():
            return "<u>" + fn() + "</u>"
        return warpped
    def pascal_triangle(n):
        trow = [1]
        y = [0]
        for x in range(max(n,0)):
            print(trow)
            trow=[l+r for l,r in zip(trow+y,y+trow)]
        return n>=1
