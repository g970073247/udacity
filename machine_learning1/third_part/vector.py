from math import sqrt, acos, pi
from decimal import Decimal, getcontext

getcontext().prec = 30


class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates


    def plus(self, v):
        #new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        
        new_coordinates = []
        n = len(self.coordinates)
        for i in range(n):
            new_coordinates.append(self.coordinates[i] + v.coordinates[i])
        
        return Vector(new_coordinates)

    def minus(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)


    def times_scalar(self, c):
        new_coordinates = [c*x for x in self.coordinates]
        return Vector(new_coordinates)


    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))


    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(1./magnitude)

        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')


    def dot(self, v):
        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])


    def angle_with(self, v, in_degrees=False):
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            angle_in_radians = acos(u1.dot(u2))

            if in_degrees:
                degrees_per_radian = 180. / pi
                return angle_in_radians * degrees_per_radian
            else:
                return angle_in_radians

        except Exception as e:
            if str(e) == self.
'''
my_vector1 = Vector([1, 2, 3])
print my_vector1

my_vector2 = Vector([1, 2, 3])
my_vector3 = Vector([-1, 2, 3])

print my_vector1 == my_vector2
print '-----'
print my_vector1 == my_vector3
'''
v1 = Vector([8.218, -9.341])
v12 = Vector([-1.129, 2.111])
v13 = v1.plus(v12)
print v13
print '--1--'

v2 = Vector([7.119, 8.215])
v21 = Vector([-8.223, 0.878])
print v2.minus(v21)
#v22 = v2.minus(v21)
#print v22
print '--2--'

v3 = Vector([1.671, -1.012, -0.318])
print v3.times_scalar(7.41)

magV1 = Vector([-0.221, 7.437])
print magV1.magnitude()
print '---magv1---'

magV2 = Vector([8.813, -1.331, -6.247])
print magV2.magnitude()
print '---magv2---'

dirV1  = Vector([5.581, -2.136])
print dirV1.normalized()
print '---dirv1---'

dirV2 = Vector([1.996, 3.108, -4.554])
print dirV2.normalized()