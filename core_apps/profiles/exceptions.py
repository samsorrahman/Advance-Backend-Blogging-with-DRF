from rest_framework.exceptions import APIException


class CantFollowYourself(APIException):
    status_code = 400
    default_detail = "You can't follow yourself"
    default_code = "cant_follow_yourself"
