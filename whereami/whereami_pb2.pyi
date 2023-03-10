from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class WhereamiReply(_message.Message):
    __slots__ = ["backend_result", "cloud_run_instance_id", "cloud_run_service_account", "cluster_name", "metadata", "node_name", "pod_ip", "pod_name", "pod_name_emoji", "pod_namespace", "pod_service_account", "project_id", "timestamp", "zone"]
    BACKEND_RESULT_FIELD_NUMBER: _ClassVar[int]
    CLOUD_RUN_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_RUN_SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NODE_NAME_FIELD_NUMBER: _ClassVar[int]
    POD_IP_FIELD_NUMBER: _ClassVar[int]
    POD_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    POD_NAME_EMOJI_FIELD_NUMBER: _ClassVar[int]
    POD_NAME_FIELD_NUMBER: _ClassVar[int]
    POD_SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    backend_result: WhereamiReply
    cloud_run_instance_id: str
    cloud_run_service_account: str
    cluster_name: str
    metadata: str
    node_name: str
    pod_ip: str
    pod_name: str
    pod_name_emoji: str
    pod_namespace: str
    pod_service_account: str
    project_id: str
    timestamp: str
    zone: str
    def __init__(self, backend_result: _Optional[_Union[WhereamiReply, _Mapping]] = ..., cluster_name: _Optional[str] = ..., metadata: _Optional[str] = ..., node_name: _Optional[str] = ..., pod_ip: _Optional[str] = ..., pod_name: _Optional[str] = ..., pod_name_emoji: _Optional[str] = ..., pod_namespace: _Optional[str] = ..., pod_service_account: _Optional[str] = ..., project_id: _Optional[str] = ..., timestamp: _Optional[str] = ..., zone: _Optional[str] = ..., cloud_run_instance_id: _Optional[str] = ..., cloud_run_service_account: _Optional[str] = ...) -> None: ...
