import logging

from tracardi.config import tracardi
from tracardi.domain.live_segment import WorkflowSegmentationTrigger
from tracardi.exceptions.log_handler import log_handler
from tracardi.service.storage.mysql.mapping.segment_trigger_mapping import map_to_workflow_segmentation_trigger_table
from tracardi.service.storage.mysql.schema.table import WorkflowSegmentationTriggerTable
from tracardi.service.storage.mysql.utils.select_result import SelectResult
from tracardi.service.storage.mysql.service.table_service import TableService, where_tenant_context

logger = logging.getLogger(__name__)
logger.setLevel(tracardi.logging_level)
logger.addHandler(log_handler)


class WorkflowSegmentationTriggerService(TableService):

    async def load_all(self, search: str = None, limit: int = None, offset: int = None) -> SelectResult:
        where = None
        if search:
            where = where_tenant_context(
                WorkflowSegmentationTriggerTable,
                WorkflowSegmentationTriggerTable.name.like(f'%{search}%')
            )
        else:
            where = where_tenant_context(
                WorkflowSegmentationTriggerTable
            )

        return await self._select_query(WorkflowSegmentationTriggerTable,
                                        where=where,
                                        order_by=WorkflowSegmentationTriggerTable.name,
                                        limit=limit,
                                        offset=offset)

    async def load_by_id(self, trigger_id: str) -> SelectResult:
        return await self._load_by_id(WorkflowSegmentationTriggerTable, primary_id=trigger_id)

    async def delete_by_id(self, trigger_id: str) -> str:
        return await self._delete_by_id(WorkflowSegmentationTriggerTable, primary_id=trigger_id)

    async def insert(self, trigger: WorkflowSegmentationTrigger):
        return await self._replace(WorkflowSegmentationTriggerTable, map_to_workflow_segmentation_trigger_table(trigger))


    async def load_by_type(self, type: str, limit: int = 1000) -> SelectResult:
        where = where_tenant_context(
            WorkflowSegmentationTriggerTable,
            WorkflowSegmentationTriggerTable.type == type,
            WorkflowSegmentationTriggerTable.enabled == True
        )

        return await self._select_query(WorkflowSegmentationTriggerTable,
                                        where=where,
                                        limit=limit)