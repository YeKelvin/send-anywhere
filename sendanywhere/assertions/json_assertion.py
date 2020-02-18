#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : json_assertion.py.py
# @Time    : 2020/2/17 16:39
# @Author  : Kelvin.Ye
from sendanywhere.assertions.assertion import Assertion, AssertionResult
from sendanywhere.samplers.sample_result import SampleResult
from sendanywhere.testelement.test_element import TestElement
from sendanywhere.utils.log_util import get_logger

log = get_logger(__name__)


class JsonAssertion(Assertion, TestElement):
    JSONPATH = 'JsonAssertion.jsonpath'
    EXPECTED_VALUE = 'JsonAssertion.expected_value'

    def do_assert(self, json_str):
        pass

    def get_result(self, response: SampleResult) -> AssertionResult:
        pass
