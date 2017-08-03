from math import sqrt, acos, pi
from decimal import Decimal, getcontext

getcontext().prec = 30


class Vector(object):

    def __init__(self, coordinates):

        self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'cannot normalize the zero vector'
        self.NO_UNIQUE_PARALLEL_COMPONENT_MSG = 'no unique parallel component'
        self.ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG = 'only defined in 2 and 3 dimensions'


        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(self.coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    
    def is_zero(self, tolerance = 1e-10):
        return self.magnitude() < tolerance

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
        new_coordinates = [Decimal(c)*x for x in self.coordinates]
        return Vector(new_coordinates)


    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return Decimal.sqrt(sum(coordinates_squared))


    def normalized(self):
        try:
            magnitude = self.magnitude()
            #return self.times_scalar(1.0/magnitude)
            return self.times_scalar(Decimal(1)/Decimal(magnitude))

        except ZeroDivisionError:
            raise Exception('self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG')


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
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with the zero vector')
            else:
                raise e

# lesson 9 function
    def is_orthogonal_to(self, v, tolerance = 1e-10):
        return abs(self.dot(v)) < tolerance


    def is_parallel_to(self, v):
        return ( self.is_zero() or
            v.is_zero() or
            self.angle_with(v) == 0 or
            self.angle_with(v) == pi )


    def is_zero(self, tolerance = 1e-10):
        return self.magnitude() < tolerance


# lesson 11 function
    def component_orthogonal_to(self, basis):
        try:
            projection = self.component_parallel_to(basis)
            return self.minus(projection)

        except Exception as e:
            if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
                raise Exception(self.NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG)
            else:
                raise e


    def component_parallel_to(self, basis):
        try:
            u = basis.normalized()
            weight = self.dot(u)
            return u.times_scalar(weight)

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e


    def cross(self, v):
        try:
            x_1, y_1, z_1 = self.coordinates
            x_2, y_2, z_2 = v.coordinates
            new_coordinates =[ y_1*z_2 - y_2*z_1 ,
                            -(x_1*z_2 - x_2*z_1),
                            x_1*y_2 - x_2*y_1 ]
            return Vector(new_coordinates)

        except ValueError as e:
            msg = str(e)
            if msg == 'need more than 2 values to unpack':
                self_embedded_in_R3 = Vector(self.coordinates + ('0',))
                v_embedded_in_R3 = Vector(v.coordinates + ('0',))
                return self_embedded_in_R3.cross(v_embedded_in_R3)
            elif (msg == 'too many values to unpack' or
                  msg == 'need more than 1 value to unpack'):
                raise Exception(self.ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG)
            else:
                raise e

    def area_of_triangle_with(self, v):
        return self.area_of_parallelogram_with(v) / Decimal('2.0')

    def area_of_parallelogram_with(self, v):
        cross_product = self.cross(v)
        return cross_product.magnitude()

        
        

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
print '---dirv2---'

dotV1 = Vector([7.887, 4.138])
dotV12 = Vector([-8.802, 6.776])
print dotV1.dot(dotV12)
print '---dot1---'

dotV2 = Vector([-5.955, -4.904, -1.874])
dotV22 = Vector([-4.496, -8.755, 7.103])
print dotV2.dot(dotV22)
print '---dot2---'

thtV1 = Vector([3.183, -7.627])
thtV12 = Vector([-2.668, 5.319])
print thtV1.angle_with(thtV12)
print '---tht1---'

degV1 = Vector([7.35, 0.221, 5.188])
degV2 = Vector([2.751, 8.259, 3.985])
print degV1.angle_with(degV2, True)
print '---deg1---'

'''
_v1 = Vector([1.000, 2.000])
_v2 = Vector([2.000, 4.000])
print _v1.angle_with(_v2)

print '&&&&&'

_v3 = Vector([-7.578, -7.88])
_v4 = Vector([22.737, 23.64])
print _v3.angle_with(_v4)
'''

p_or_oV1 = Vector([-7.579, -7.88])
p_or_oV12 = Vector([22.737, 23.65])
#print p_or_oV1.is_parallel_to(p_or_oV12)
#print p_or_oV1.angle_with(p_or_oV12)
print '---p1---'
print p_or_oV1.is_orthogonal_to(p_or_oV12)
print '---v1---'


p_or_oV2 = Vector([-2.029, 9.97, 4.172])
p_or_oV22 = Vector([-9.231, -6.639, -7.245])
print p_or_oV2.is_parallel_to(p_or_oV22)
print '---p2---'
print p_or_oV2.is_orthogonal_to(p_or_oV22)
print '---v2---'

p_or_oV3 = Vector([-2.328, -7.284, -1.214])
p_or_oV32 = Vector([-1.821, 1.072, -2.94])
print p_or_oV3.is_parallel_to(p_or_oV32)
print '---p3---'
print p_or_oV3.is_orthogonal_to(p_or_oV32)
print '---v3---'

p_or_oV4 = Vector([2.118, 4.827])
p_or_oV42 = Vector([0, 0])
print p_or_oV4.is_parallel_to(p_or_oV42)
print '---p4---'
print p_or_oV4.is_orthogonal_to(p_or_oV42)
print '---v4---'

projV1 = Vector([3.039, 1.879])
projV12 = Vector([0.825, 2.036])
print projV1.component_parallel_to(projV12)
print '---proj1---'

ortV1 = Vector([-9.88, -3.264, -8.159])
ortV12 = Vector([-2.155, -9.353, -9.473])
print ortV1.component_orthogonal_to(ortV12)
print '---orthogonal1---'

projV2 = Vector([3.009, -6.172, 3.692, -2.51])
projV22 = Vector([6.404, -9.144, 2.759, 8.718])
print projV2.component_parallel_to(projV22)
print '---proj2---'
print projV2.component_orthogonal_to(projV22)
print '---orthogonal---'

crossV1 = Vector([8.462, 7.893, -8.187])
crossV12 = Vector([6.984, -5.975, 4.778])
print crossV1.cross(crossV12)
print '---cross1---'

crossV2 = Vector([-8.987, -9.838, 5.031])
crossV22 = Vector([-4.268, -1.861, -8.866])
print crossV2.area_of_parallelogram_with(crossV22)
print '---cross2---'

crossV3 = Vector([1.5, 9.547, 3.691])
crossV32 = Vector([-6.007, 0.124, 5.772])
print crossV3.area_of_triangle_with(crossV32)
print '---cross3---'