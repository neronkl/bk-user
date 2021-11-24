# coding: utf-8

"""
    蓝鲸用户管理 API

    蓝鲸用户管理后台服务 API  # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class GeneralLog(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'extra_value': 'object',
        'operator': 'str',
        'create_time': 'datetime',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'extra_value': 'extra_value',
        'operator': 'operator',
        'create_time': 'create_time',
        'status': 'status'
    }

    def __init__(self, id=None, extra_value=None, operator=None, create_time=None, status=None):  # noqa: E501
        """GeneralLog - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._extra_value = None
        self._operator = None
        self._create_time = None
        self._status = None
        self.discriminator = None
        self.id = id
        self.extra_value = extra_value
        self.operator = operator
        self.create_time = create_time
        self.status = status

    @property
    def id(self):
        """Gets the id of this GeneralLog.  # noqa: E501

        ID  # noqa: E501

        :return: The id of this GeneralLog.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GeneralLog.

        ID  # noqa: E501

        :param id: The id of this GeneralLog.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def extra_value(self):
        """Gets the extra_value of this GeneralLog.  # noqa: E501

        额外信息  # noqa: E501

        :return: The extra_value of this GeneralLog.  # noqa: E501
        :rtype: object
        """
        return self._extra_value

    @extra_value.setter
    def extra_value(self, extra_value):
        """Sets the extra_value of this GeneralLog.

        额外信息  # noqa: E501

        :param extra_value: The extra_value of this GeneralLog.  # noqa: E501
        :type: object
        """
        if extra_value is None:
            raise ValueError("Invalid value for `extra_value`, must not be `None`")  # noqa: E501

        self._extra_value = extra_value

    @property
    def operator(self):
        """Gets the operator of this GeneralLog.  # noqa: E501

        操作者  # noqa: E501

        :return: The operator of this GeneralLog.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this GeneralLog.

        操作者  # noqa: E501

        :param operator: The operator of this GeneralLog.  # noqa: E501
        :type: str
        """
        if operator is None:
            raise ValueError("Invalid value for `operator`, must not be `None`")  # noqa: E501

        self._operator = operator

    @property
    def create_time(self):
        """Gets the create_time of this GeneralLog.  # noqa: E501

        创建时间  # noqa: E501

        :return: The create_time of this GeneralLog.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this GeneralLog.

        创建时间  # noqa: E501

        :param create_time: The create_time of this GeneralLog.  # noqa: E501
        :type: datetime
        """
        if create_time is None:
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def status(self):
        """Gets the status of this GeneralLog.  # noqa: E501

        状态  # noqa: E501

        :return: The status of this GeneralLog.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GeneralLog.

        状态  # noqa: E501

        :param status: The status of this GeneralLog.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GeneralLog, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GeneralLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
