import maya.OpenMaya as om
import re
mode_name = 'om'
class_list = [i for i in dir(om) if not re.match("MIt.*", i) is None and re.match(".*_", i) is None]
class_string = r'''
class <<CLASS>>(<<MODE>>.<<CLASS>>):
    def __iter__(self):
        return MItForIt(self)
'''
string_list = list()
string_list.append("# " + ", ".join(class_list))
for i in class_list:
    string_list.append(
            re.sub(r"<<MODE>>", mode_name,
                   re.sub(r"<<CLASS>>", i, class_string)
                   )
            )
string_list.append(
        "__all__ = [" + ", ".join(['"{}"'.format(i) for i in class_list]) + "]"
                   )
print "\n".join(string_list)

# import maya.OpenMaya as om
# import re
# class_list = [i for i in dir(om) if not re.match("MIt.*", i) is None and re.match(".*_", i) is None]
# mode_name = 'om'
# string_list = list()
# booy = '''        self.__CP_is_start = True
#     def __iter__(self):
#         self.reset()
#         self.__CP_is_start = True
#         return self
#     def next(self):
#         if self.__CP_is_start:
#             self.__CP_is_start = False
#         else:'''
# booyb ='''        if self.isDone():
#             raise StopIteration
#         else:
#             item = self
#             return item'''
# string_list.append(
#         "# " + ','.join(class_list)
#         )
#
# for i in class_list:
#     string_list.append(
#             "class {}({}.{}):".format(i, mode_name, i)
#             )
#     string_list.append(
#             "    def __init__(self, *args, **kwargs):"
#             )
#     string_list.append(
#             "        super({}, self).__init__(*args, **kwargs)".format(i)
#             )
#     string_list.append(
#             booy
#             )
#     string_list.append(
#             "            super({}, self).next()".format(i)
#             )
#     string_list.append(
#             booyb
#             )
# string_list.append(
#         "__all__ = [" + ",".join(['"{}"'.format(i) for i in class_list]) + "]"
#         )
# print '\n'.join(string_list)