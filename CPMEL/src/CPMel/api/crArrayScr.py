import maya.OpenMayaAnim as om
import re
class_list = [i for i in dir(om) if not re.match(".*(Array)$", i) is None and re.match(".*_", i) is None]

class_string = r'''
class <<CLASS>>(<<MODE>>.<<CLASS>>):
    def __len__(self):
        return self.length()

    def __iter__(self):
        return MAyyayIt(self)

    def __repr__(self):
        return '{}[{}]'.format(str(self.__class__), ", ".join([i.__class__.__repr__(i) for i in self]))

    def __str__(self):
        return '{}[{}]'.format(str(self.__class__), ", ".join([i.__class__.__str__(i) for i in self]))
'''
string_list = list()
string_list.append("# " + ", ".join(class_list))
for i in class_list:
    string_list.append(
            re.sub(r"<<MODE>>", "OpenMayaAnim",
                   re.sub(r"<<CLASS>>", i, class_string)
                   )
            )
string_list.append(
        "__all__ = [" + ", ".join(['"{}"'.format(i) for i in class_list]) + "]"
                   )
print "\n".join(string_list)