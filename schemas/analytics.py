from pydantic import BaseModel


class HotspotOut(BaseModel):
    cell_or_cluster_id: str
    center_lat: float
    center_lng: float
    category_id: int | None
    complaint_count: int
    score: float
    radius_m: float


class SummaryOut(BaseModel):
    totals_by_status: dict[str, int]
    totals_by_category: dict[str, int]
    avg_resolution_time_hours: float | None
    per_department_counts: dict[str, int]