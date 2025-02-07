# coding: utf-8
# Copyright 2023 OpenSPG Authors
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.


"""
    knext

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from knext.rest.configuration import Configuration


class LogicalRule(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "code": "RuleCode",
        "name": "str",
        "version": "int",
        "is_master": "bool",
        "atatus": "str",
        "content": "str",
        "creator": "UserInfo",
    }

    attribute_map = {
        "code": "code",
        "name": "name",
        "version": "version",
        "is_master": "isMaster",
        "atatus": "atatus",
        "content": "content",
        "creator": "creator",
    }

    def __init__(
        self,
        code=None,
        name=None,
        version=None,
        is_master=None,
        atatus=None,
        content=None,
        creator=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """LogicalRule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._name = None
        self._version = None
        self._is_master = None
        self._atatus = None
        self._content = None
        self._creator = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if is_master is not None:
            self.is_master = is_master
        if atatus is not None:
            self.atatus = atatus
        if content is not None:
            self.content = content
        if creator is not None:
            self.creator = creator

    @property
    def code(self):
        """Gets the code of this LogicalRule.  # noqa: E501


        :return: The code of this LogicalRule.  # noqa: E501
        :rtype: RuleCode
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this LogicalRule.


        :param code: The code of this LogicalRule.  # noqa: E501
        :type: RuleCode
        """

        self._code = code

    @property
    def name(self):
        """Gets the name of this LogicalRule.  # noqa: E501


        :return: The name of this LogicalRule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LogicalRule.


        :param name: The name of this LogicalRule.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def version(self):
        """Gets the version of this LogicalRule.  # noqa: E501


        :return: The version of this LogicalRule.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this LogicalRule.


        :param version: The version of this LogicalRule.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def is_master(self):
        """Gets the is_master of this LogicalRule.  # noqa: E501


        :return: The is_master of this LogicalRule.  # noqa: E501
        :rtype: bool
        """
        return self._is_master

    @is_master.setter
    def is_master(self, is_master):
        """Sets the is_master of this LogicalRule.


        :param is_master: The is_master of this LogicalRule.  # noqa: E501
        :type: bool
        """

        self._is_master = is_master

    @property
    def atatus(self):
        """Gets the atatus of this LogicalRule.  # noqa: E501


        :return: The atatus of this LogicalRule.  # noqa: E501
        :rtype: str
        """
        return self._atatus

    @atatus.setter
    def atatus(self, atatus):
        """Sets the atatus of this LogicalRule.


        :param atatus: The atatus of this LogicalRule.  # noqa: E501
        :type: str
        """
        allowed_values = ["INIT", "GRAY", "PROD", "OFF", "DEL"]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and atatus not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `atatus` ({0}), must be one of {1}".format(  # noqa: E501
                    atatus, allowed_values
                )
            )

        self._atatus = atatus

    @property
    def content(self):
        """Gets the content of this LogicalRule.  # noqa: E501


        :return: The content of this LogicalRule.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this LogicalRule.


        :param content: The content of this LogicalRule.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def creator(self):
        """Gets the creator of this LogicalRule.  # noqa: E501


        :return: The creator of this LogicalRule.  # noqa: E501
        :rtype: UserInfo
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this LogicalRule.


        :param creator: The creator of this LogicalRule.  # noqa: E501
        :type: UserInfo
        """

        self._creator = creator

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LogicalRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LogicalRule):
            return True

        return self.to_dict() != other.to_dict()
