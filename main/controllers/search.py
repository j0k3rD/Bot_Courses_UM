# from flask_restful import Resource
# from flask import request
# from main.map import SearchSchema
# from main.map import CourseSchema
# from ..repositories import SearchRepository
# from ..repositories import CourseRepository
# from main.models import SearchModel
# from .. import db


# search_schema = SearchSchema()
# search_repository = SearchRepository()

# course_schema = CourseSchema()
# course_repository = CourseRepository()

# class Search:
#     def get(self, id):
#         search = db.session.query(SearchModel).get_or_404(id)
#         return search_schema.dump(search), 201

# class Searchs:
#     def get(self):
#         searchs = db.session.query(SearchModel)
#         return search_schema.dump(searchs), 201