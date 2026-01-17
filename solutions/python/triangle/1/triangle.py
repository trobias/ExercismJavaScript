def verificar(sides):
        a = sides[0]
        b = sides[1]
        c = sides[2]
        if a == 0:
            return False
        elif b == 0:
            return False
        elif c == 0:
            return False
        elif a + b < c:
            return False
        elif b + c < a:
            return False
        elif a + c < b:
            return False
        else:
            return True


def equilateral(sides): 
        a = sides[0]
        b = sides[1]
        c = sides[2]
        if verificar(sides) == False:
            return False
        elif a == b == c:
                return True
        else:
             return False

def isosceles(sides):
        a = sides[0]
        b = sides[1]
        c = sides[2]
        if verificar(sides) == False:
            return False
        elif a == b or b == c or c == a:
                return True
        else:
             return False
        


def scalene(sides):
        a = sides[0]
        b = sides[1]
        c = sides[2]
        if verificar(sides) == False:
            return False
        elif a != b and b != c and c != a:
                return True
        else:
             return False