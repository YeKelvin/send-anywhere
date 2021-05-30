#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : result_collector.py
# @Time    : 2020/2/18 17:20
# @Author  : Kelvin.Ye
from tasker.elements.element import TaskElement
from tasker.engine.interface import TaskGroupListener
from tasker.engine.interface import NoCoroutineClone
from tasker.engine.interface import SampleListener
from tasker.engine.interface import TaskIterationListener
from tasker.engine.interface import TaskCollectionListener
from tasker.groups.context import ContextService
from tasker.utils import time_util
from tasker.utils.log_util import get_logger


log = get_logger(__name__)


class ResultCollector(
    TaskElement,
    TaskCollectionListener,
    TaskGroupListener,
    SampleListener,
    TaskIterationListener,
    NoCoroutineClone
):

    def __init__(self):
        TaskElement.__init__(self)
        self.reportName = None
        self.startTime = 0
        self.endTime = 0
        self.groups = {}

    @property
    def __group_id(self) -> str:
        coroutine_group = ContextService.get_context().coroutine_group
        return f'{coroutine_group.name}-{coroutine_group.group_number}'

    @property
    def __group_name(self):
        return ContextService.get_context().coroutine_group.name

    def collection_started(self) -> None:
        self.startTime = time_util.timestamp_as_ms()

    def collection_ended(self) -> None:
        self.endTime = time_util.timestamp_as_ms()

    def group_started(self) -> None:
        self.groups[self.__group_id] = {
            'startTime': time_util.timestamp_as_ms(),
            'endTime': 0,
            'success': True,
            'groupName': self.__group_name,
            'samplers': []
        }

    def group_finished(self) -> None:
        self.groups[self.__group_id]['endTime'] = time_util.timestamp_as_ms()

    def sample_started(self, sample) -> None:
        pass

    def sample_ended(self, sample_result) -> None:
        if not sample_result:
            return

        self.groups[self.__group_id]['samplers'].append({
            'startTime': sample_result.start_time,
            'endTime': sample_result.end_time,
            'elapsedTime': sample_result.elapsed_time,
            'success': sample_result.success,
            'samplerName': sample_result.sample_label,
            'request': sample_result.request_body,
            'response': sample_result.response_data
        })

        if not sample_result.success:
            self.groups[self.__group_id]['success'] = False

    def task_iteration_start(self, controller) -> None:
        pass
