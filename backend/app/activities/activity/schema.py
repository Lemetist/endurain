from pydantic import BaseModel


class Activity(BaseModel):
    id: int | None = None
    user_id: int | None = None
    description: str | None = None
    distance: int
    name: str
    activity_type: int
    start_time: str
    end_time: str
    timezone: str | None = None
    total_elapsed_time: float | None = None
    total_timer_time: float | None = None
    city: str | None = None
    town: str | None = None
    country: str | None = None
    created_at: str | None = None
    elevation_gain: int | None = None
    elevation_loss: int | None = None
    pace: float | None = None
    average_speed: float | None = None
    max_speed: float | None = None
    average_power: int | None = None
    max_power: int | None = None
    normalized_power: int | None = None
    average_hr: int | None = None
    max_hr: int | None = None
    average_cad: int | None = None
    max_cad: int | None = None
    workout_feeling: int | None = None
    workout_rpe: int | None = None
    calories: int | None = None
    visibility: int | None = None
    gear_id: int | None = None
    strava_gear_id: str | None = None
    strava_activity_id: int | None = None
    garminconnect_activity_id: int | None = None
    garminconnect_gear_id: str | None = None

    class Config:
        orm_mode = True


class ActivityDistances(BaseModel):
    run: float
    bike: float
    swim: float
    walk: float
    hike: float
    rowing: float
    snow_ski: float
    snowboard: float


class ActivityEdit(BaseModel):
    id: int
    description: str | None = None
    name: str
    activity_type: int
    visibility: int | None = None
    gear_id: int | None = None
