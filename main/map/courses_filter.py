from main.models.course import Course
from main.models import CourseModel


class CourseFilter():
    
    def __init__(self, course):
        self.__course = course
        self.__filters = {   "id": self.__filter_by_id,
                            "url": self.__filter_by_url,
                            "title": self.__filter_by_title,
                            "count": self.__filter_by_count,
                         }

    def __filter_by_id(self, value):
        return self.__course.filter(CourseModel.id == int(value))
    
    def __filter_by_url(self, value):
        return self.__course.filter(CourseModel.url.like(f"%{value}%"))

    def __filter_by_title(self, value):
        return self.__course.filter(CourseModel.title.like(f"%{value}%"))
    
    def __filter_by_count(self, value):
        return self.__course.filter(CourseModel.count == int(value))
    
    def apply_filter(self, key, value):
        return self.__filters[filter](value)