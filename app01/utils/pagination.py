#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/10/31 21:33
# @Author : natsume
# @File : pagination.py
# @Software: PyCharm
"""
自定义组件
"""
from django.utils.safestring import mark_safe


class Pagination(object):
    def __init__(self, request, queryset, page_size = 10, page_param = "page", plus = 5):
        """
        :param request: 请求的对象
        :param queryset: 符合条件的数据
        :param page_size: 每页显示多少条数据
        :param page_param: 在URL中传递的获取分页的参数
        :param plus: 显示当前页的前或后几页
        """

        import copy
        query_dict = copy.deepcopy(request.GET)
        query_dict._mutable = True
        self.query_dict = query_dict

        self.page_param = page_param
        page = request.GET.get(page_param, "1")
        if page.isdecimal():
            page = int(page)
        else:
            page = 1
        self.page = page
        self.page_size = page_size
        self.start = (page - 1) * page_size
        self.end = page * page_size
        self.page_queryset = queryset[self.start:self.end]

        # 数据总条数
        total_count = queryset.count()

        # 总页数
        total_page_count, div = divmod(total_count, page_size)
        # 如果余数不为0，则总页数加1
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count
        self.plus = plus

    def html(self):
        if self.total_page_count <= 2 * self.plus + 1:
            start_page = 1
            end_page = self.total_page_count
        else:
            if self.page <= self.plus:
                start_page = 1
                end_page = 2 * self.plus + 1
            else:
                if (self.page + self.plus) > self.total_page_count:
                    start_page = self.total_page_count - 2 * self.plus
                    end_page = self.total_page_count
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus

        page_str_list = []
        self.query_dict.setlist(self.page_param, [1])
        page_str_list.append('<li class="page-item"><a class="page-link" href="?{}">首页</a></li>'.format(self.query_dict.urlencode()))

        # 如果是第一页，点击上一页显示还是第一页，否则显示下一页
        if (self.page == 1):
            self.query_dict.setlist(self.page_param, [self.page])
            prev = '<li class="page-item"><a class="page-link" href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [1])
            prev = '<li class="page-item"><a class="page-link" href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(prev)

        for i in range(start_page, end_page + 1):
            self.query_dict.setlist(self.page_param, [i])
            if i == self.page:
                ele = '<li class="active page-item"><a class="page-link" href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            else:
                ele = '<li class="page-item"><a class="page-link" href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            page_str_list.append(ele)

        # 如果不是最后一页，显示下一页，否则点击下一页还是最后一页
        if self.page == self.total_page_count:
            self.query_dict.setlist(self.page_param, [self.total_page_count])
            next = '<li class="page-item"><a class="page-link" href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [self.page + 1])
            next = '<li class="page-item"><a class="page-link" href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())

        # 添加下一页
        page_str_list.append(next)

        # 尾页
        self.query_dict.setlist(self.page_param, [self.total_page_count])
        page_str_list.append('<li class="page-item"><a class="page-link" href="?{}">尾页</a></li>'.format(self.query_dict.urlencode()))

        search_string = """
                <li class="page-item">
                        <form style="float: left; margin-left: -1px" method="get">
                            <input type="text" name="page" style="position: relative; float: left; display: inline-block; width: 80px; border-radius: 0;" class="form-control" placeholder="页码">
                            <button class="btn btn-default page-link" style="border-radius: 0; margin-left: 0px;" type="submit">跳转</button>
                        </form>
                </li>
            """

        page_str_list.append(search_string);

        page_string = mark_safe("".join(page_str_list))
        return page_string