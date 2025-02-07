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


class MappingConfig(object):
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
        "source": "str",
        "target": "str",
        "strategy_config": "BaseStrategyConfig",
        "mapping_type": "str",
    }

    attribute_map = {
        "source": "source",
        "target": "target",
        "strategy_config": "strategyConfig",
        "mapping_type": "mappingType",
    }

    def __init__(
        self,
        source=None,
        target=None,
        strategy_config=None,
        mapping_type=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """MappingConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._source = None
        self._target = None
        self._strategy_config = None
        self._mapping_type = None
        self.discriminator = None

        if source is not None:
            self.source = source
        if target is not None:
            self.target = target
        if strategy_config is not None:
            self.strategy_config = strategy_config
        if mapping_type is not None:
            self.mapping_type = mapping_type

    @property
    def source(self):
        """Gets the source of this MappingConfig.  # noqa: E501


        :return: The source of this MappingConfig.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this MappingConfig.


        :param source: The source of this MappingConfig.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def target(self):
        """Gets the target of this MappingConfig.  # noqa: E501


        :return: The target of this MappingConfig.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this MappingConfig.


        :param target: The target of this MappingConfig.  # noqa: E501
        :type: str
        """

        self._target = target

    @property
    def strategy_config(self):
        """Gets the strategy_config of this MappingConfig.  # noqa: E501


        :return: The strategy_config of this MappingConfig.  # noqa: E501
        :rtype: BaseStrategyConfig
        """
        return self._strategy_config

    @strategy_config.setter
    def strategy_config(self, strategy_config):
        """Sets the strategy_config of this MappingConfig.


        :param strategy_config: The strategy_config of this MappingConfig.  # noqa: E501
        :type: BaseStrategyConfig
        """

        self._strategy_config = strategy_config

    @property
    def mapping_type(self):
        """Gets the mapping_type of this MappingConfig.  # noqa: E501


        :return: The mapping_type of this MappingConfig.  # noqa: E501
        :rtype: str
        """
        return self._mapping_type

    @mapping_type.setter
    def mapping_type(self, mapping_type):
        """Sets the mapping_type of this MappingConfig.


        :param mapping_type: The mapping_type of this MappingConfig.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "PROPERTY",
            "RELATION",
            "SUB_PROPERTY",
            "SUB_RELATION",
        ]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and mapping_type not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `mapping_type` ({0}), must be one of {1}".format(  # noqa: E501
                    mapping_type, allowed_values
                )
            )

        self._mapping_type = mapping_type

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
        if not isinstance(other, MappingConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MappingConfig):
            return True

        return self.to_dict() != other.to_dict()
