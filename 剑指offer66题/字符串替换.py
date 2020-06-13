
'''
请实现一个函数，将一个字符串中的每个空格替换成'%20'.
例如:当字符串为We Are Happy 则经过替换之后的字符串为We%20Are%20Happy
'''

class Solution:
    def replaceSpace(self,s):
        # 第一种，使用内置函数replace
        # return s.replace(' ','%20')

        # 第二种
        # str_len = len(s)
        aaa = []
        for i in s:
            if i == ' ':
                aaa.append('%20')
            else:
                aaa.append(i)
        return ''.join(aaa)

if __name__ == '__main__':
    s = Solution()
    print(s.replaceSpace('We Are Happy'))